import requests
from code_ui_raw.manage_Facebook_Account import Ui_Manage_Facebook_Account
from main_utils.file import pop_data_configs, put_data_configs, read_data_configs
from PyQt6.QtWidgets import  QMessageBox,QWidget
from PyQt6.QtCore import Qt

class Ui_Manage_Facebook_Account_Over(Ui_Manage_Facebook_Account):
    
    def set_login_window_widget(self,login_window):
        self.login_window = login_window
        
    def setupUi(self, qwidget):
        super().setupUi(qwidget)
        