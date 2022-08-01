from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
 
 
class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui_raw/mainWindow.ui", self)
        
app = QApplication([])
window = UI()
window.show()
app.exec()