
import re
import time
from code_ui_raw.open_Brower import Ui_OpenBrower
from main_utils.api import call_api
from main_utils.driver import init_Chrome_Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PyQt6.QtWidgets import  QMessageBox
from PyQt6.QtCore import QThread

class Thr(QThread):
    def __init__(self, fun):
        super().__init__()
        self.fun = fun
    def run(self):
        self.fun()
                
                
class Ui_OpenBrower_Over(Ui_OpenBrower):
    def setupUi(self, widget):
        super().setupUi(widget)
        self.driver = None
        self.widget = widget
        self.checkBox_get_from_db.toggled.connect(lambda x: self.disable_input())
        self.checkBox_get_from_db.setChecked(True)
        self.pushButton_open.clicked.connect(self.open_brower)
        self.pushButton_update.clicked.connect(self.update_cookie)
        self.lineEdit_text_input.textChanged.connect(self.read_text)
        self.thr = None
        
    def read_text(self):
        text = self.lineEdit_text_input.text()
        result = re.search(r"([\d]+.[\d]+.[\d]+.[\d]+:[\d]+:.+)",text)
        if result:
            proxy = result.group(1)
            text = text[:-len(proxy)-1]
            result = re.search(r"([\w.@_]+) ",text)
            if result:
                username = result.group(1)
                passwrod = text[len(username)+1:]
                self.lineEdit_input_password.setText(passwrod)
                self.lineEdit_input_uid.setText(username)
                self.lineEdit_input.setText(proxy)
                self.checkBox_get_from_db.setChecked(False)
                


        
    def update_cookie(self):
        if self.driver is None or len(self.driver.window_handles)<=0:
            return
        cookies = self.driver.get_cookies()
        cookie = {}
        for _cookie in cookies:
            if _cookie['name']=="xs":
                cookie["xs"] =  _cookie['value']
                
            if _cookie['name']=="sb":
                cookie["sb"] =  _cookie['value']
                
            if _cookie['name']=="c_user":
                cookie["c_user"] =  _cookie['value']
        if not all([cookie.get("xs"),cookie.get("sb"),cookie.get("c_user")]) :
            dialog = QMessageBox(parent=self.widget, text=f"Cookie not correct.")
            dialog.setWindowTitle("Proxy")
            ret = dialog.exec() 
            return
        passwrod = self.lineEdit_input_password.text()
        if len(passwrod)<=0:
            passwrod = None
        res = call_api(method="put",api="insert_cookie_for_master_user",
            data={
                "cookies":cookie,
                "password":passwrod,
                "proxy":self.proxy,
                "is_update":True,
                "upsert":True
            }
        )
        if res.status_code == 200:
            dialog = QMessageBox(parent=self.widget, text=f"Update cookie successfull.")
            dialog.setWindowTitle("Cookies")
            ret = dialog.exec() 
            return
        dialog = QMessageBox(parent=self.widget, text=f"Update cookie failed: {res.status_code}-{res.text}.")
        dialog.setWindowTitle("Cookies")
        ret = dialog.exec() 
    
    def open_brower(self):
        self.proxy = None
        if self.checkBox_auto_login.isChecked():
            if len(self.lineEdit_input_uid.text())<=2 or len(self.lineEdit_input_password.text())<=2:
                dialog = QMessageBox(parent=self.widget, text=f"Username or passord is wrong.")
                dialog.setWindowTitle("Login Info")
                ret = dialog.exec()  
                return
            
            
        if self.checkBox_get_from_db.isChecked():
            res = call_api(method="post",api="get_proxy",data={"getRandomOne":True})
            if res.status_code == 200:
                try:
                    data = res.json()["data"]
                    if len(data)>0:
                        self.proxy = data[0]
                    else:
                        dialog = QMessageBox(parent=self.widget, text=f"Proxy in DB not found.")
                        dialog.setWindowTitle("Proxy")
                        ret = dialog.exec()  
                        return
                    
                except:
                    pass
            else:
                dialog = QMessageBox(parent=self.widget, text=f"Get proxy from db error: {res.status_code} - {{res.text}}")
                dialog.setWindowTitle("Proxy")
                ret = dialog.exec()  
                return
        else:
            proxy_text = self.lineEdit_input.text().split(":")
            if len(proxy_text)!=4:
                dialog = QMessageBox(parent=self.widget, text=f"Proxy {self.lineEdit_input} has the wrong format.")
                dialog.setWindowTitle("Proxy")
                ret = dialog.exec()  
                return
            
                
            self.proxy = {
                "ip":proxy_text[0],
                "port":proxy_text[1],
                "user_name":proxy_text[2],
                "password":proxy_text[3]  
            }
        
        if self.proxy is None:
            dialog = QMessageBox(parent=self.widget, text=f"Proxy in DB not found.")
            dialog.setWindowTitle("Proxy")
            ret = dialog.exec()  
            return
    
        self.thr = Thr(self.open_sele)
        self.thr.start()
    
    def open_sele(self):    
        self.driver,msg = init_Chrome_Driver(proxy_user_name=self.proxy["user_name"],proxy_password=self.proxy["password"],proxy_ip=self.proxy["ip"],proxy_port=self.proxy["port"])
        if self.driver is None:
            dialog = QMessageBox(parent=self.widget, text=msg)
            dialog.setWindowTitle("Error")
            ret = dialog.exec() 
            return
        self.driver.get("https://www.facebook.com")
        
        if self.checkBox_auto_login.isChecked():
            element_email = self.driver.find_element(by = By.ID,value="email")
            element_email.click()
            actions = ActionChains(self.driver)
            self.send_keys(action=actions,keys_to_send=self.lineEdit_input_uid.text())
            element_pass = self.driver.find_element(by = By.ID,value="pass")
            element_pass.click()
            self.send_keys(action=actions,keys_to_send=self.lineEdit_input_password.text())
            time.sleep(5)
            element_login = self.driver.find_element(by=By.NAME,value="login")
            element_login.click()
        
        while True:
            try:
                self.driver.title()
            except:
                break
        
    def send_keys(self, action: ActionChains, keys_to_send:str):
        """
        Sends keys to current focused element.

        :Args:
         - keys_to_send: The keys to send.  Modifier keys constants can be found in the
           'Keys' class.
        """
        # typing = keys_to_typing(keys_to_send)

        for key in keys_to_send:
            action = ActionChains(self.driver)
            action.key_down(key)
            action.key_up(key)
            action.perform()
            action.pause(0.1)    
    def disable_input(self):
        self.lineEdit_input.setEnabled(not self.checkBox_get_from_db.isChecked())
        
            
        