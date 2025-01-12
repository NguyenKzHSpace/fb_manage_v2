from typing import List
from code_ui_raw.manage_Facebook_Account import Ui_Manage_Facebook_Account
from main_utils.api import call_api
from PyQt6.QtWidgets import  QWidget
import threading
import unidecode
from PyQt6 import QtGui
from PyQt6.QtWidgets import QTableWidgetItem
from code_ui_over.open_Brower import Ui_OpenBrower_Over
from code_ui_over.login_Facebook import Ui_Login_Facebook_Over
class Ui_Manage_Facebook_Account_Over(Ui_Manage_Facebook_Account):
    
    def remove_accent(self,text,down_case:bool = True):
        result = unidecode.unidecode(text)
        if down_case:
            result = str(result).lower()
        return result
    def set_login_window_widget(self,login_window):
        self.login_window = login_window
        
    def setupUi(self, qwidget):
        self.qwidget = qwidget
        super().setupUi(qwidget)
        self.cursor = None
        self.driver = None
        self.thread_get_data = None
        self.thread_update_gui = None
        self.list_account_from_server = []
        self.list_account_filter = []
        self.list_state = []
        self.statictis_state = {}
        
        self.get_data()
        
        self.is_fillter = False
        self.checkBox_filter_name.stateChanged.connect(self.filter_account)
        self.checkBox_filter_state.stateChanged.connect(self.filter_account)
        self.checkBox_filter_user_code.stateChanged.connect(self.filter_account)
        self.checkBox_filter_uid.stateChanged.connect(self.filter_account)
        self.checkBox_filter_proxy.stateChanged.connect(self.filter_account)
        self.checkBox_ignore_trash.stateChanged.connect(self.filter_account)
        
        self.lineEdit_filter_name.textChanged.connect(lambda x: self.filter_account())
        self.lineEdit_filter_uid.textChanged.connect(lambda x: self.filter_account())
        self.comboBox_filter_state.currentTextChanged.connect(lambda x: self.filter_account())
        self.lineEdit_filter_user_code.textChanged.connect(lambda x: self.filter_account())
        self.lineEdit_filter_proxy.textChanged.connect(lambda x: self.filter_account())

        self.pushButton_reset.clicked.connect(self.reset_filter)
        self.pushButton_Reload.clicked.connect(self.get_data)
        
        self.tableWidget_list_account.currentItemChanged.connect(self.load_login_button)
        self.tableWidget_list_account.doubleClicked.connect(self.dubleClicked)
        self.pushButton_login.clicked.connect(self.login_to_fb_account)
        self.pushButton_OpenBrower.clicked.connect(self.open_new_brower_with_proxy)
    
    def dubleClicked(self):
        
        row = self.tableWidget_list_account.currentRow()    
        if len(self.list_account_filter)<=row:
            self.pushButton_login.setEnabled(False)
            return
        
        account = self.list_account_filter[row]
        proxy = account.get("proxy")
        
        if self.checkBox_filter_proxy.isChecked()==False:
            proxy_value = "None"
            if account.get("proxy"):
                proxy = account.get("proxy")
                proxy_value = f"{proxy.get('ip')}:{proxy.get('port')}"
            self.lineEdit_filter_proxy.setText(proxy_value)
        
        if self.checkBox_filter_user_code.isChecked()==False:
            self.lineEdit_filter_user_code.setText(account.get("user_code"))
           
        
    def load_login_button(self):
        
        row = self.tableWidget_list_account.currentRow()    
        if len(self.list_account_filter)<=row:
            self.pushButton_login.setEnabled(False)
            return
        
        account = self.list_account_filter[row]
        proxy = account.get("proxy")
        if proxy is None:
            self.pushButton_login.setEnabled(False)
            return
        else:
            self.pushButton_login.setEnabled(True)
           
            
    def login_to_fb_account(self):
        ##
        # 
        # Open brower and put cookies, proxy to brower
        # 
        # #
        row = self.tableWidget_list_account.currentRow()    
        if len(self.list_account_filter)<=row:
            self.pushButton_login.setEnabled(False)
            return
        
        account = self.list_account_filter[row]
        print(f"{row}  -{len( self.list_account_filter)} - {account.get('uid')}")
        cookies = account.get("cookies")
        proxy = account.get("proxy")
        name = account.get("name")
        uid = account.get("uid")
        
        self.login_facebook_QWidget = QWidget()
        login_facebook = Ui_Login_Facebook_Over()
        login_facebook.set_info_login(proxy=proxy,cookies=cookies,name=name,uid=uid,ip=proxy.get("ip"))
        login_facebook.setupUi(self.login_facebook_QWidget)
        self.login_facebook_QWidget.show()
        
        
    def open_new_brower_with_proxy(self):
        row = self.tableWidget_list_account.currentRow()    
        uid = None
        proxy_value = None
        password = None
        if len(self.list_account_filter)>=row and row>=0:
            account = self.list_account_filter[row]
            uid = account.get("uid")
            proxy = account.get("proxy")
            if proxy is not None:
                proxy_value = f"{proxy.get('ip')}:{proxy.get('port')}:{proxy.get('user_name')}:{proxy.get('password')}"
                password = account.get("password")
                
        
        self.manage_window_QWidget = QWidget()
        open_brower_fr = Ui_OpenBrower_Over()
        open_brower_fr.setupUi(self.manage_window_QWidget)
        
        if uid is not None:
            open_brower_fr.lineEdit_input_uid.setText(str(uid))
            
        if proxy_value is not None:
            open_brower_fr.lineEdit_input.setText(proxy_value)
        
        if password is not None:
            open_brower_fr.lineEdit_input_password.setText(password) 
            
        self.manage_window_QWidget.show()
        
        
        
    def reset_filter(self):
        self.checkBox_filter_name.setChecked(False)
        self.checkBox_filter_uid.setChecked(False)
        self.checkBox_filter_user_code.setChecked(False)
        self.checkBox_filter_state.setChecked(False)
        
        self.lineEdit_filter_name.setText("")
        self.lineEdit_filter_uid.setText("")
        self.lineEdit_filter_user_code.setText("")
        self.comboBox_filter_state.setCurrentText("")
        
    def filter_account(self,**kwargs):
        self.is_fillter = True
        if self.thread_update_gui is not None and self.thread_update_gui.is_alive()==False or self.thread_update_gui is None:
            self.thread_update_gui = threading.Thread(target=self.filter_data)
            self.thread_update_gui.start()
  
    def filter_data(self):
        if self.is_fillter:
            self.cleardata(clear_state = False)
            if self.checkBox_ignore_trash.isChecked():
                self.list_account_filter = []
                for account in self.list_account_from_server:
                    if account.get("user_code")=="trash":
                        continue
                    self.list_account_filter.append(account)
            else:
                self.list_account_filter = self.list_account_from_server.copy()
            
            self.is_fillter = False
            self.list_state.clear()
            if self.checkBox_filter_name.isChecked():
                self.filter_name()
            if self.checkBox_filter_state.isChecked():
                self.filter_state()
            if self.checkBox_filter_uid.isChecked():
                self.filter_uid()
            if self.checkBox_filter_user_code.isChecked():
                self.filter_user_code()
            if self.checkBox_filter_proxy.isChecked():
                self.filter_proxy()
                
            self.insert_data(data = self.list_account_filter)
            
            self.list_statistics_state_child.clear()
            list_account = [account for account in self.list_account_filter if self.checkBox_ignore_trash.isChecked() and account.get('user_code')!='trash'  or self.checkBox_ignore_trash.isChecked()==False]
            self.list_statistics_state_child.addItem(f"Tổng: {len(list_account)}")
            for state in self.statictis_state:
                self.list_statistics_state_child.addItem(f"{state}: {self.statictis_state[state]}")
                
    
    def filter_name(self):
        text = self.lineEdit_filter_name.text()
        if len(text) > 0:
            text =self.remove_accent(text)
            list_temp = []
            for account in self.list_account_filter:
                if self.remove_accent(str(account.get("name"))).find(text) >= 0:
                    list_temp.append(account)
            self.list_account_filter = list_temp
    
    
    def filter_uid(self):
        text = self.lineEdit_filter_uid.text()
        if len(text) > 0:
            list_temp = []
            for account in self.list_account_filter:
                if str(account.get("uid")).find(text) >= 0:
                    list_temp.append(account)
            self.list_account_filter = list_temp
    
    def filter_proxy(self):
        text = self.lineEdit_filter_proxy.text()
        if len(text) > 0:
            list_temp = []
            for account in self.list_account_filter:
                proxy_value = "None"
                if account.get("proxy"):
                    proxy = account.get("proxy")
                    proxy_value = f"{proxy.get('ip')}:{proxy.get('port')}:{proxy.get('user_name')}:{proxy.get('password')}"
                if proxy_value.find(text) >= 0:
                    list_temp.append(account)
                    
                        
            self.list_account_filter = list_temp
            
    def filter_state(self):
        text = self.comboBox_filter_state.currentText()
        if len(text) > 0:
            list_temp = []
            for account in self.list_account_filter:
                if str(account.get("state_vn"))==text:
                    list_temp.append(account)
            self.list_account_filter = list_temp
            
    def filter_user_code(self):
        text = self.lineEdit_filter_user_code.text()
        if len(text) > 0:
            list_temp = []
            for account in self.list_account_filter:
                if str(account.get("user_code")).find(text) >= 0:
                    list_temp.append(account)
            self.list_account_filter = list_temp     
            
    def get_data(self):
        self.cleardata()
        self.thread_get_data = threading.Thread(target=self.__get_data__)
        self.thread_get_data.start()
    
    def cleardata(self,clear_state = True):
        self.current_state = self.comboBox_filter_state.currentText()
        self.tableWidget_list_account.clear()
        self.list_account_filter.clear()
        self.statictis_state.clear()
        #
        self.tableWidget_list_account.setRowCount(0)
        if clear_state:
            self.comboBox_filter_state.clear()
        
    def __get_data__(self):
        self.list_account_from_server.clear()
        self.statictis_state.clear()
        api = "get_facebook_account"
        self.label_status.setText("Loading")
        self.checkBox_filter_name.setEnabled(False)
        self.checkBox_filter_uid.setEnabled(False)
        self.checkBox_filter_user_code.setEnabled(False)
        self.checkBox_filter_proxy.setEnabled(False)
        self.tableWidget_list_account.clear()
        self.checkBox_filter_state.setEnabled(False)
        self.pushButton_login.setEnabled(False)
        self.pushButton_Reload.setEnabled(False)
        self.pushButton_reset.setEnabled(False)
        self.cursor = None
        try:
            while True:
            
                data = {
                    "cursor": self.cursor,
                    "limit":50,
                    "is_get_page_info":False
                }
                try:
                    res = call_api(method="post",api=api,data=data,timeout=10)
                    
                    if res.status_code != 200:
                        print(res.status_code)
                        print(res.text)
                        self.comboBox_filter_state.clear()
                        self.comboBox_filter_state.insertItems(1,self.list_state)    
                        self.comboBox_filter_state.setCurrentText("")
                        self.label_status.setText(f"Error.: {res.status_code} - {res.text}")
                        self.checkBox_filter_name.setEnabled(True)
                        self.checkBox_filter_uid.setEnabled(True)
                        self.checkBox_filter_user_code.setEnabled(True)
                        self.checkBox_filter_proxy.setEnabled(True)
                        self.checkBox_filter_state.setEnabled(True)
                        self.tableWidget_list_account.resizeColumnsToContents()
                        self.pushButton_Reload.setEnabled(True)
                        self.pushButton_reset.setEnabled(True)
                        
                        self.list_statistics_state_child.clear()
                        list_account = [account for account in self.list_account_from_server if self.checkBox_ignore_trash.isChecked() and account.get('user_code')!='trash'  or self.checkBox_ignore_trash.isChecked()==False]
                        self.list_account_filter = list_account
                        self.list_statistics_state_child.addItem(f"Tổng: {len(list_account)}")
                        for state in self.statictis_state:
                            self.list_statistics_state_child.addItem(f"{state}: {self.statictis_state[state]}")
                            
                        return True, res.status_code
                    
                    res = res.json()
                    
                    data = res.get("data")
                    self.cursor = res.get("cursor")
                    have_next_page = res.get("have_next_page")
                    
                    for account in data:
                        self.list_account_from_server.append(account)
                        
                    self.insert_data(data=data)
                    
                        
                    if have_next_page == False:
                        self.comboBox_filter_state.clear()
                        self.comboBox_filter_state.insertItems(1,self.list_state)    
                        self.comboBox_filter_state.setCurrentText("")
                        self.label_status.setText("Complete.")
                        self.checkBox_filter_name.setEnabled(True)
                        self.checkBox_filter_uid.setEnabled(True)
                        self.checkBox_filter_user_code.setEnabled(True)
                        self.checkBox_filter_proxy.setEnabled(True)
                        self.checkBox_filter_state.setEnabled(True)
                        self.tableWidget_list_account.resizeColumnsToContents()
                        self.pushButton_Reload.setEnabled(True)
                        self.pushButton_reset.setEnabled(True)
                        
                        self.list_statistics_state_child.clear()
                        list_account = [account for account in self.list_account_from_server if self.checkBox_ignore_trash.isChecked() and account.get('user_code')!='trash'  or self.checkBox_ignore_trash.isChecked()==False]
                        self.list_account_filter = list_account
                        self.list_statistics_state_child.addItem(f"Tổng: {len(list_account)}")
                        for state in self.statictis_state:
                            self.list_statistics_state_child.addItem(f"{state}: {self.statictis_state[state]}")
                            
                        return
             
                    text_loading = self.label_status.text()
                    if len(text_loading)>len("Loading.")+4:
                        text_loading= "Loading."
                    text_loading+="."
                    self.label_status.setText(text_loading)
                    self.list_statistics_state_child.clear()
                    self.list_statistics_state_child.addItem(f"Got: {len(self.list_account_from_server)} (account)")
                except Exception as ex:
                    self.comboBox_filter_state.clear()
                    self.comboBox_filter_state.insertItems(1,self.list_state)    
                    self.comboBox_filter_state.setCurrentText("")
                    self.label_status.setText(f"Error.: {ex}")
                    self.checkBox_filter_name.setEnabled(True)
                    self.checkBox_filter_uid.setEnabled(True)
                    self.checkBox_filter_user_code.setEnabled(True)
                    self.checkBox_filter_proxy.setEnabled(True)
                    self.checkBox_filter_state.setEnabled(True)
                    self.tableWidget_list_account.resizeColumnsToContents()
                    self.pushButton_Reload.setEnabled(True)
                    self.pushButton_reset.setEnabled(True)
                
                    self.list_statistics_state_child.clear()
                    list_account = [account for account in self.list_account_from_server if self.checkBox_ignore_trash.isChecked() and account.get('user_code')!='trash'  or self.checkBox_ignore_trash.isChecked()==False]
                    self.list_account_filter = list_account
                    self.list_statistics_state_child.addItem(f"Tổng: {len(list_account)}")
                    for state in self.statictis_state:
                        self.list_statistics_state_child.addItem(f"{state}: {self.statictis_state[state]}")
                    return
            
        except Exception as ex:
            print(ex)
            
        
        
    def insert_data(self,data,list_header:List[str] = []):
        _data = []
        for account in data:
            if self.checkBox_ignore_trash.isChecked(): 
                    if account.get("user_code") =="trash":
                        continue
            _data.append(account)
        data = _data
        for account in data:
            count_column = 0
            for key in account:
                if key not in list_header:
                    if key in ["pages_info","state"]:
                        continue
                    
                    list_header.append(key)
                
                count_column+=1
            if str(account.get("state_vn")) not in self.list_state and len(str(account.get("state_vn")))>0:
                self.list_state.append(str(account.get("state_vn")))
                
            if self.tableWidget_list_account.columnCount()<count_column:
                self.tableWidget_list_account.setColumnCount(count_column)
                
        self.tableWidget_list_account.setHorizontalHeaderLabels(list_header)
        current_row_count = self.tableWidget_list_account.rowCount()
        self.tableWidget_list_account.setRowCount(current_row_count+len(data))
        
        for row,account in enumerate(data):    
            has_proxy = account.get("proxy") is not None
            if self.statictis_state.get(account.get("state_vn")) is None:
                self.statictis_state[account.get("state_vn")] = 0
            self.statictis_state[account.get("state_vn")]+=1
            
            for index,key in enumerate(list_header):
                
                newitem = None
                if key == "proxy":
                    value = str(account.get(key))
                    if account.get(key) is not None:
                        value = f"{account.get(key).get('ip')}:{account.get(key).get('port')}:{account.get(key).get('user_name')}:{account.get(key).get('password')}"
                    newitem = QTableWidgetItem(value)
              
                    self.tableWidget_list_account.setItem(row+current_row_count, index, newitem)
                if key == "cookies":
                    value = str(account.get(key))
                    if  account.get(key) is not None:
                        value = ""
                        for cookie in account.get(key):
                            value += f"{cookie['name']}={cookie['value']}; "
                    value = value[:-2]
                    newitem = QTableWidgetItem(value)
              
                    self.tableWidget_list_account.setItem(row+current_row_count, index, newitem)
                else:
                    value = str(account.get(key))
                    newitem = QTableWidgetItem(value)
                    self.tableWidget_list_account.setItem(row+current_row_count, index, newitem)
            
                if has_proxy == False and newitem:
                    font = QtGui.QFont()
                    font.setBold(True)
                    newitem.setFont(font)

        
        