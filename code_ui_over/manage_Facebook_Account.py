from typing import List
import requests
from code_ui_raw.manage_Facebook_Account import Ui_Manage_Facebook_Account
from main_utils.file import get_data_configs, pop_data_configs, put_data_configs, read_data_configs
from PyQt6.QtWidgets import  QMessageBox,QWidget
from PyQt6.QtCore import Qt
from threading import Thread
import threading
import time
import unidecode

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem
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
        self.thread_get_data = None
        self.thread_update_gui = None
        self.list_account_from_server = []
        self.list_account_filter = []
        self.list_state = []
        
        self.get_data()
        
        self.is_fillter = False
        self.checkBox_filter_name.stateChanged.connect(self.filter_account)
        self.checkBox_filter_state.stateChanged.connect(self.filter_account)
        self.checkBox_filter_user_code.stateChanged.connect(self.filter_account)
        self.checkBox_filter_uid.stateChanged.connect(self.filter_account)
        
        self.lineEdit_filter_name.textChanged.connect(lambda x: self.filter_account(type_ev="name"))
        self.lineEdit_filter_uid.textChanged.connect(lambda x: self.filter_account(type_ev="uid"))
        self.comboBox_filter_state.currentTextChanged.connect(lambda x: self.filter_account(type_ev="state"))
        self.lineEdit_filter_user_code.textChanged.connect(lambda x: self.filter_account(type_ev="user_code"))

        self.pushButton_reset.clicked.connect(self.reset_filter)
        self.pushButton_Reload.clicked.connect(self.get_data)
        
        self.tableWidget_list_account.currentItemChanged.connect(self.load_login_button)

    def load_login_button(self):
        
        row = self.tableWidget_list_account.currentRow()    
        if len(self.list_account_filter)<=row:
            self.pushButton_login.setEnabled(False)
            return
        
        account = self.list_account_filter[row]
        
        cookies = account.get("cookies")
        proxy = account.get("proxy")
        
        if proxy is None:
            self.pushButton_login.setEnabled(False)
            return
        else:
            self.pushButton_login.setEnabled(True)
        
        ##
        # 
        # Open brower and put cookies, proxy to brower
        # 
        # #
        
        
        
        
        
        
    def reset_filter(self):
        self.checkBox_filter_name.setChecked(False)
        self.checkBox_filter_uid.setChecked(False)
        self.checkBox_filter_user_code.setChecked(False)
        self.checkBox_filter_state.setChecked(False)
        
        self.lineEdit_filter_name.setText("")
        self.lineEdit_filter_uid.setText("")
        self.lineEdit_filter_user_code.setText("")
        self.comboBox_filter_state.setCurrentText("")
        
    def filter_account(self,type_ev:str = None):
        if type_ev =="name":
            if self.checkBox_filter_name.isChecked():
                self.is_fillter = True
        elif type_ev =="uid":
            if self.checkBox_filter_uid.isChecked():
                self.is_fillter = True
        elif type_ev =="state":
            if self.checkBox_filter_state.isChecked():
                self.is_fillter = True
        elif type_ev =="user_code":
            if self.checkBox_filter_user_code.isChecked():
                self.is_fillter = True
        else:     
            self.is_fillter = True
        
        if self.is_fillter ==True  is not None and self.thread_update_gui is not None and self.thread_update_gui.is_alive()==False or self.thread_update_gui is None:
            self.thread_update_gui = threading.Thread(target=self.filter_data)
            self.thread_update_gui.start()
  
    def filter_data(self):
        if self.is_fillter:
            self.cleardata(clear_state = False)
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
            self.insert_data(data = self.list_account_filter)
            
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
            
    def filter_state(self):
        text = self.comboBox_filter_state.currentText()
        if len(text) > 0:
            list_temp = []
            for account in self.list_account_filter:
                if str(account.get("state")).find(text) >= 0:
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
        self.tableWidget_list_account.setRowCount(0)
        if clear_state:
            self.comboBox_filter_state.clear()
        
    def __get_data__(self):
        data_configs = read_data_configs()
        api = "get_facebook_account"
        last_time_update_ui = time.time()
        self.label_status.setText("Loading")
        current_row = 0
        self.checkBox_filter_name.setEnabled(False)
        self.checkBox_filter_uid.setEnabled(False)
        self.checkBox_filter_user_code.setEnabled(False)
        self.checkBox_filter_state.setEnabled(False)
        self.pushButton_login.setEnabled(False)
        self.pushButton_Reload.setEnabled(False)
        self.pushButton_reset.setEnabled(False)
        self.pushButton_OpenBrower.setEnabled(False)
        self.cursor = None
        try:
            while self.qwidget.isVisible():
            
                data = {
                    "cursor": self.cursor,
                    "limit":40,
                    "is_get_page_info":False
                }
                url = f"{data_configs.get('server')}/{api}"

                header = {
                    "Authorization": data_configs.get('token'),
                    "s-key": data_configs.get('s_key')
                }
                
                res = requests.post(url, json=data, headers=header, timeout=5)
                
                if res.status_code == 401:
                    get_data_configs(key = "email")
                    get_data_configs(key = "password")
                    server_url = get_data_configs(key = "server")
                    url = f"{server_url}/login"
                    data = {
                        "email": get_data_configs(key = "email"),
                        "password": get_data_configs(key = "password")
                    }
                    res = requests.post(url=url, json=data,timeout=5)
                    ##
                    # Response error
                    # #
                    if res.status_code != 200:
                        dialog = QMessageBox(parent=self.qwidget, text=f"Login failed: {res.text}")
                        dialog.setWindowTitle("Login")
                        ret = dialog.exec()  
                        return False
                    try:
                        ##
                        # Response Ok => Read data
                        # #
                        
                        res = res.json()
                        s_key = res.get("secret_key")
                        token = res.get("token").get("token_type")+" " + \
                            res.get("token").get("access_token")
                        code = res.get("code")
                        put_data_configs(key = "s_key",data = s_key)
                        put_data_configs(key = "token",data = token)
                        put_data_configs(key = "code",data = code)
                        print(f"Token: {token} ")
                        data_configs = read_data_configs()
                        continue
                    
                    except Exception as ex:
                        print(f"Error: {ex} ")
                        dialog = QMessageBox(parent=self.qwidget, text=f"Login Failed: {ex}.")
                        dialog.setWindowTitle("Login")
                        ret = dialog.exec()  
                        return
                                    
                if res.status_code != 200:
                    print(res.status_code)
                    print(res.text)
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
                    self.checkBox_filter_state.setEnabled(True)
                    self.tableWidget_list_account.resizeColumnsToContents()
                    self.pushButton_Reload.setEnabled(True)
                    self.pushButton_reset.setEnabled(True)
                    self.pushButton_OpenBrower.setEnabled(True)
                    self.list_account_filter = self.list_account_from_server.copy()
                    return
                if time.time()-last_time_update_ui>0.5:
                    last_time_update_ui = time.time()
                    text_loading = self.label_status.text()
                    if len(text_loading)>len("Loading.")+4:
                        text_loading= "Loading."
                    text_loading+="."
                    self.label_status.setText(text_loading)
                
            
        except Exception as ex:
            print(ex)
            
        
        
    def insert_data(self,data,list_header:List[str] = []):
        
        for account in data:
            count_column = 0
            for key in account:
                if key not in list_header:
                    if key in ["cookies","pages_info"]:
                        continue
                    list_header.append(key)
                count_column+=1
            if str(account.get("state")) not in self.list_state and len(str(account.get("state")))>0:
                self.list_state.append(str(account.get("state")))
                
            if self.tableWidget_list_account.columnCount()<count_column:
                self.tableWidget_list_account.setColumnCount(count_column)
                
        self.tableWidget_list_account.setHorizontalHeaderLabels(list_header)
        current_row_count = self.tableWidget_list_account.rowCount()
        self.tableWidget_list_account.setRowCount(current_row_count+len(data))
        
        for row,account in enumerate(data):    
            has_proxy = account.get("proxy") is not None
            account_ok = account.get("state") =="OK"
            for index,key in enumerate(list_header):
                value = str(account.get(key))
                if key == "proxy":
                    if has_proxy:
                        value = "Yes"
                    else:
                        value = "No"
                
                newitem = QTableWidgetItem(value)
                if has_proxy == False:
                    font = QtGui.QFont()
                    font.setBold(True)
                    newitem.setFont(font)
                # if account_ok:
                #     newitem.setForeground(QBrush(QColor(0, 255, 0)))
                self.tableWidget_list_account.setItem(row+current_row_count, index, newitem)
        
        

        
        