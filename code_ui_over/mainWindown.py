import requests
from code_ui_raw.mainWindown import Ui_LoginWindow
from main_utils.file import put_data_configs, read_data_configs
import threading
from PyQt6.QtWidgets import  QMessageBox,QWidget
from PyQt6.QtCore import Qt
class Ui_LoginWindow_Over(Ui_LoginWindow):
    
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.widget = MainWindow
        self.thread_login = None
        config_data = read_data_configs()
        if config_data.get("email") is not None:
            self.lineEdit_email.setText(config_data.get("email"))
        if config_data.get("password") is not None:
            self.lineEdit_password.setText(config_data.get("password"))
        if config_data.get("server") is not None:
            self.lineEdit_server.setText(config_data.get("server"))
            
        self.lineEdit_email.textChanged.connect(self.save_data_login)
        self.lineEdit_password.textChanged.connect(self.save_data_login)
        self.lineEdit_server.textChanged.connect(self.save_data_login)
        
        self.pushButton_login.clicked.connect(self.login)
        
    def save_data_login(self):
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()
        server = self.lineEdit_server.text()
        put_data_configs(key = "email",data = email)
        put_data_configs(key = "password",data = password)
        put_data_configs(key = "server",data = server)
            
    def login(self):
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()
        server = self.lineEdit_server.text()
        if server.startswith("http://") == False and server.startswith("http://") == False:
            return
        
        put_data_configs(key = "email",data = email)
        put_data_configs(key = "password",data = password)
        put_data_configs(key = "server",data = server)
        url = f"{server}/login"
        data = {
            "email": email,
            "password": password
        }
        def __inner__(url:str,data:dict):
            res = requests.post(url=url, json=data)
            if res.status_code != 200:
                return False
            try:
                res = res.json()
                s_key = res.get("secret_key")
                token = res.get("token").get("token_type")+" " + \
                    res.get("token").get("access_token")
                code = res.get("code")
                put_data_configs(key = "s_key",data = s_key)
                put_data_configs(key = "token",data = token)
                put_data_configs(key = "code",data = code)
                dialog = QMessageBox(parent=self.widget, text="Please wait!")
                dialog.setWindowTitle("Login")
                dialog.show()
            except Exception as ex:
                print(ex)
        
        if self.thread_login is not None and self.thread_login.is_alive():
            dialog = QMessageBox(parent=self.widget, text="Please wait!")
            dialog.setWindowTitle("Login")
            ret = dialog.exec()   
        else:
            self.thread_login = threading.Thread(target=__inner__, kwargs={"url":url,"data":data})
            self.thread_login.start()
            
    def don(self):
        pass