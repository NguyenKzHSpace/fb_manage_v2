import requests
from code_ui_over.manage_Facebook_Account import Ui_Manage_Facebook_Account_Over
from code_ui_raw.mainWindown import Ui_LoginWindow
from code_ui_raw.manage_Facebook_Account import Ui_Manage_Facebook_Account
from main_utils.file import pop_data_configs, put_data_configs, read_data_configs
import threading
from PyQt6.QtWidgets import  QMessageBox,QWidget
from PyQt6.QtCore import Qt
class Ui_LoginWindow_Over(Ui_LoginWindow):
    
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.widget = MainWindow
        self.manage_window_QWidget = None
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
        ##
        # 
        # Remove old token
        # #
        pop_data_configs("token")
        
        ##
        # 
        # Login
        # 
        # #
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()
        server = self.lineEdit_server.text()
        ##
        # check url of server
        # #
        if server.startswith("http://") == False and server.startswith("http://") == False:
            return
        ##
        # Save data login
        # #
        put_data_configs(key = "email",data = email)
        put_data_configs(key = "password",data = password)
        put_data_configs(key = "server",data = server)
        ##
        # Call API login
        # #
        url = f"{server}/login"
        data = {
            "email": email,
            "password": password
        }
        def __inner__(url:str,data:dict):
            ##
            # Call API
            # 
            # #
            try:
                res = requests.post(url=url, json=data,timeout=20)
            except:
                dialog = QMessageBox(parent=self.widget, text=f"Login failed: server timeout.")
                dialog.setWindowTitle("Login")
                ret = dialog.exec()  
                return False
            ##
            # Response error
            # #
            if res.status_code != 200:
                dialog = QMessageBox(parent=self.widget, text=f"Login failed: {res.text}")
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
                dialog = QMessageBox(parent=self.widget, text=f"Login Succesfull.")
                dialog.setWindowTitle("Login")
                ret = dialog.exec()  
                self.open_manager_account_window()
            except Exception as ex:
                print(f"Error: {ex} ")
                dialog = QMessageBox(parent=self.widget, text=f"Login Failed: {ex}.")
                dialog.setWindowTitle("Login")
                ret = dialog.exec()  
                
        __inner__(url=url,data=data)
            
    def open_manager_account_window(self):
        if self.manage_window_QWidget is None:
            self.manage_window_QWidget = QWidget()
            manage_window = Ui_Manage_Facebook_Account_Over()
            manage_window.set_login_window_widget(login_window=self.widget)
            manage_window.setupUi(qwidget = self.manage_window_QWidget)
            self.manage_window_QWidget.show()
            self.widget.close()
            