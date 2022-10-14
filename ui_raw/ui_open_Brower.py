# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'open_Brower.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_OpenBrower(object):
    def setupUi(self, OpenBrower):
        if not OpenBrower.objectName():
            OpenBrower.setObjectName(u"OpenBrower")
        OpenBrower.resize(510, 293)
        self.verticalLayout = QVBoxLayout(OpenBrower)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(OpenBrower)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setBold(True)
        self.groupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_input = QLineEdit(self.groupBox)
        self.lineEdit_input.setObjectName(u"lineEdit_input")
        font1 = QFont()
        font1.setPointSize(14)
        self.lineEdit_input.setFont(font1)

        self.verticalLayout_2.addWidget(self.lineEdit_input)

        self.checkBox_get_from_db = QCheckBox(self.groupBox)
        self.checkBox_get_from_db.setObjectName(u"checkBox_get_from_db")

        self.verticalLayout_2.addWidget(self.checkBox_get_from_db)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(OpenBrower)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEdit_input_uid = QLineEdit(self.groupBox_3)
        self.lineEdit_input_uid.setObjectName(u"lineEdit_input_uid")
        self.lineEdit_input_uid.setFont(font1)

        self.verticalLayout_3.addWidget(self.lineEdit_input_uid)

        self.lineEdit_input_password = QLineEdit(self.groupBox_3)
        self.lineEdit_input_password.setObjectName(u"lineEdit_input_password")
        self.lineEdit_input_password.setFont(font1)

        self.verticalLayout_3.addWidget(self.lineEdit_input_password)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.lineEdit_text_input = QLineEdit(OpenBrower)
        self.lineEdit_text_input.setObjectName(u"lineEdit_text_input")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.lineEdit_text_input.setFont(font2)

        self.verticalLayout.addWidget(self.lineEdit_text_input)

        self.groupBox_2 = QGroupBox(OpenBrower)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_open = QPushButton(self.groupBox_2)
        self.pushButton_open.setObjectName(u"pushButton_open")
        self.pushButton_open.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_open)

        self.pushButton_update = QPushButton(self.groupBox_2)
        self.pushButton_update.setObjectName(u"pushButton_update")
        self.pushButton_update.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_update)

        self.checkBox_auto_login = QCheckBox(self.groupBox_2)
        self.checkBox_auto_login.setObjectName(u"checkBox_auto_login")

        self.horizontalLayout.addWidget(self.checkBox_auto_login)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(OpenBrower)

        QMetaObject.connectSlotsByName(OpenBrower)
    # setupUi

    def retranslateUi(self, OpenBrower):
        OpenBrower.setWindowTitle(QCoreApplication.translate("OpenBrower", u"Open Brower", None))
        self.groupBox.setTitle(QCoreApplication.translate("OpenBrower", u"Proxy", None))
        self.lineEdit_input.setInputMask("")
        self.lineEdit_input.setPlaceholderText(QCoreApplication.translate("OpenBrower", u"IP:PORT:USER_NAME:PASSWORD", None))
        self.checkBox_get_from_db.setText(QCoreApplication.translate("OpenBrower", u"Get proxy from DB", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("OpenBrower", u"Facebook Account", None))
        self.lineEdit_input_uid.setInputMask("")
        self.lineEdit_input_uid.setText("")
        self.lineEdit_input_uid.setPlaceholderText(QCoreApplication.translate("OpenBrower", u"UID", None))
        self.lineEdit_input_password.setInputMask("")
        self.lineEdit_input_password.setText("")
        self.lineEdit_input_password.setPlaceholderText(QCoreApplication.translate("OpenBrower", u"PASSWORD", None))
        self.lineEdit_text_input.setText("")
        self.lineEdit_text_input.setPlaceholderText(QCoreApplication.translate("OpenBrower", u"USERNAME PASSWORD PROXY", None))
        self.groupBox_2.setTitle("")
        self.pushButton_open.setText(QCoreApplication.translate("OpenBrower", u"Open", None))
        self.pushButton_update.setText(QCoreApplication.translate("OpenBrower", u"Update", None))
        self.checkBox_auto_login.setText(QCoreApplication.translate("OpenBrower", u"Auto login", None))
    # retranslateUi

