import sys

from PyQt6 import QtWidgets
from code_ui_over.mainWindown import Ui_LoginWindow_Over




class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_LoginWindow_Over()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
