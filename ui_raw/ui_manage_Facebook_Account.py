# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manage_Facebook_Account.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QScrollArea,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Manage_Facebook_Account(object):
    def setupUi(self, Manage_Facebook_Account):
        if not Manage_Facebook_Account.objectName():
            Manage_Facebook_Account.setObjectName(u"Manage_Facebook_Account")
        Manage_Facebook_Account.resize(1165, 806)
        self.verticalLayout = QVBoxLayout(Manage_Facebook_Account)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_4 = QGroupBox(Manage_Facebook_Account)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_5 = QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_filter_uid = QCheckBox(self.groupBox_5)
        self.checkBox_filter_uid.setObjectName(u"checkBox_filter_uid")

        self.horizontalLayout_5.addWidget(self.checkBox_filter_uid)

        self.lineEdit_filter_uid = QLineEdit(self.groupBox_5)
        self.lineEdit_filter_uid.setObjectName(u"lineEdit_filter_uid")

        self.horizontalLayout_5.addWidget(self.lineEdit_filter_uid)


        self.horizontalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_8 = QGroupBox(self.groupBox_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox_filter_user_code = QCheckBox(self.groupBox_8)
        self.checkBox_filter_user_code.setObjectName(u"checkBox_filter_user_code")

        self.horizontalLayout_6.addWidget(self.checkBox_filter_user_code)

        self.lineEdit_filter_user_code = QLineEdit(self.groupBox_8)
        self.lineEdit_filter_user_code.setObjectName(u"lineEdit_filter_user_code")

        self.horizontalLayout_6.addWidget(self.lineEdit_filter_user_code)

        self.checkBox_ignore_trash = QCheckBox(self.groupBox_8)
        self.checkBox_ignore_trash.setObjectName(u"checkBox_ignore_trash")
        self.checkBox_ignore_trash.setChecked(True)

        self.horizontalLayout_6.addWidget(self.checkBox_ignore_trash)


        self.horizontalLayout_2.addWidget(self.groupBox_8)

        self.groupBox_6 = QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_filter_name = QCheckBox(self.groupBox_6)
        self.checkBox_filter_name.setObjectName(u"checkBox_filter_name")

        self.horizontalLayout_4.addWidget(self.checkBox_filter_name)

        self.lineEdit_filter_name = QLineEdit(self.groupBox_6)
        self.lineEdit_filter_name.setObjectName(u"lineEdit_filter_name")

        self.horizontalLayout_4.addWidget(self.lineEdit_filter_name)


        self.horizontalLayout_2.addWidget(self.groupBox_6)

        self.groupBox_9 = QGroupBox(self.groupBox_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_filter_proxy = QCheckBox(self.groupBox_9)
        self.checkBox_filter_proxy.setObjectName(u"checkBox_filter_proxy")

        self.horizontalLayout_7.addWidget(self.checkBox_filter_proxy)

        self.lineEdit_filter_proxy = QLineEdit(self.groupBox_9)
        self.lineEdit_filter_proxy.setObjectName(u"lineEdit_filter_proxy")

        self.horizontalLayout_7.addWidget(self.lineEdit_filter_proxy)


        self.horizontalLayout_2.addWidget(self.groupBox_9)

        self.groupBox_7 = QGroupBox(self.groupBox_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_filter_state = QCheckBox(self.groupBox_7)
        self.checkBox_filter_state.setObjectName(u"checkBox_filter_state")

        self.horizontalLayout_3.addWidget(self.checkBox_filter_state)

        self.comboBox_filter_state = QComboBox(self.groupBox_7)
        self.comboBox_filter_state.setObjectName(u"comboBox_filter_state")
        self.comboBox_filter_state.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.comboBox_filter_state)


        self.horizontalLayout_2.addWidget(self.groupBox_7)

        self.pushButton_reset = QPushButton(self.groupBox_4)
        self.pushButton_reset.setObjectName(u"pushButton_reset")

        self.horizontalLayout_2.addWidget(self.pushButton_reset)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.scrollArea_list_facebook_account = QScrollArea(Manage_Facebook_Account)
        self.scrollArea_list_facebook_account.setObjectName(u"scrollArea_list_facebook_account")
        self.scrollArea_list_facebook_account.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1145, 420))
        self.verticalLayout_list_facebook_account = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_list_facebook_account.setObjectName(u"verticalLayout_list_facebook_account")
        self.tableWidget_list_account = QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget_list_account.setObjectName(u"tableWidget_list_account")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_list_account.sizePolicy().hasHeightForWidth())
        self.tableWidget_list_account.setSizePolicy(sizePolicy)

        self.verticalLayout_list_facebook_account.addWidget(self.tableWidget_list_account)

        self.label_status = QLabel(self.scrollAreaWidgetContents)
        self.label_status.setObjectName(u"label_status")

        self.verticalLayout_list_facebook_account.addWidget(self.label_status)

        self.scrollArea_list_facebook_account.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea_list_facebook_account)

        self.groupBox_statistics = QGroupBox(Manage_Facebook_Account)
        self.groupBox_statistics.setObjectName(u"groupBox_statistics")
        self.groupBox_statistics.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_statistics)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_state = QScrollArea(self.groupBox_statistics)
        self.scrollArea_state.setObjectName(u"scrollArea_state")
        self.scrollArea_state.setWidgetResizable(True)
        self.scrollAreaWidgetContents_statistics = QWidget()
        self.scrollAreaWidgetContents_statistics.setObjectName(u"scrollAreaWidgetContents_statistics")
        self.scrollAreaWidgetContents_statistics.setGeometry(QRect(0, 0, 1125, 165))
        self.verticalLayout_statistics = QVBoxLayout(self.scrollAreaWidgetContents_statistics)
        self.verticalLayout_statistics.setObjectName(u"verticalLayout_statistics")
        self.list_statistics_state_child = QListWidget(self.scrollAreaWidgetContents_statistics)
        self.list_statistics_state_child.setObjectName(u"list_statistics_state_child")

        self.verticalLayout_statistics.addWidget(self.list_statistics_state_child)

        self.scrollArea_state.setWidget(self.scrollAreaWidgetContents_statistics)

        self.verticalLayout_4.addWidget(self.scrollArea_state)


        self.verticalLayout.addWidget(self.groupBox_statistics)

        self.groupBox = QGroupBox(Manage_Facebook_Account)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Reload = QPushButton(self.groupBox)
        self.pushButton_Reload.setObjectName(u"pushButton_Reload")
        self.pushButton_Reload.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_Reload)

        self.pushButton_OpenBrower = QPushButton(self.groupBox)
        self.pushButton_OpenBrower.setObjectName(u"pushButton_OpenBrower")
        self.pushButton_OpenBrower.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_OpenBrower)

        self.pushButton_login = QPushButton(self.groupBox)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setEnabled(False)
        self.pushButton_login.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_login)


        self.verticalLayout.addWidget(self.groupBox)

        self.label_result_api = QLabel(Manage_Facebook_Account)
        self.label_result_api.setObjectName(u"label_result_api")

        self.verticalLayout.addWidget(self.label_result_api)


        self.retranslateUi(Manage_Facebook_Account)

        QMetaObject.connectSlotsByName(Manage_Facebook_Account)
    # setupUi

    def retranslateUi(self, Manage_Facebook_Account):
        Manage_Facebook_Account.setWindowTitle(QCoreApplication.translate("Manage_Facebook_Account", u"Facebook_Account", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Manage_Facebook_Account", u"filler", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Manage_Facebook_Account", u"Filter by uid", None))
        self.checkBox_filter_uid.setText("")
        self.lineEdit_filter_uid.setPlaceholderText(QCoreApplication.translate("Manage_Facebook_Account", u"enter the uid", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Manage_Facebook_Account", u"Filter by user code", None))
        self.checkBox_filter_user_code.setText("")
        self.lineEdit_filter_user_code.setPlaceholderText(QCoreApplication.translate("Manage_Facebook_Account", u"enter the user code", None))
        self.checkBox_ignore_trash.setText(QCoreApplication.translate("Manage_Facebook_Account", u"Ignore Trash", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Manage_Facebook_Account", u"Filter by name", None))
        self.checkBox_filter_name.setText("")
        self.lineEdit_filter_name.setPlaceholderText(QCoreApplication.translate("Manage_Facebook_Account", u"Enter the Name", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Manage_Facebook_Account", u"Filter by proxy", None))
        self.checkBox_filter_proxy.setText("")
        self.lineEdit_filter_proxy.setPlaceholderText(QCoreApplication.translate("Manage_Facebook_Account", u"Enter the Name", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Manage_Facebook_Account", u"Filter by State", None))
        self.checkBox_filter_state.setText("")
        self.pushButton_reset.setText(QCoreApplication.translate("Manage_Facebook_Account", u"Reset", None))
        self.label_status.setText(QCoreApplication.translate("Manage_Facebook_Account", u"Status.", None))
        self.groupBox_statistics.setTitle(QCoreApplication.translate("Manage_Facebook_Account", u"statistics", None))
        self.groupBox.setTitle("")
        self.pushButton_Reload.setText(QCoreApplication.translate("Manage_Facebook_Account", u"Reload", None))
        self.pushButton_OpenBrower.setText(QCoreApplication.translate("Manage_Facebook_Account", u"Open Brower", None))
        self.pushButton_login.setText(QCoreApplication.translate("Manage_Facebook_Account", u"Login", None))
        self.label_result_api.setText("")
    # retranslateUi

