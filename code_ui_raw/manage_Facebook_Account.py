# Form implementation generated from reading ui file './ui_raw/manage_Facebook_Account.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Manage_Facebook_Account(object):
    def setupUi(self, Manage_Facebook_Account):
        Manage_Facebook_Account.setObjectName("Manage_Facebook_Account")
        Manage_Facebook_Account.resize(889, 806)
        self.verticalLayout = QtWidgets.QVBoxLayout(Manage_Facebook_Account)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(Manage_Facebook_Account)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_filter_uid = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_filter_uid.setText("")
        self.checkBox_filter_uid.setObjectName("checkBox_filter_uid")
        self.horizontalLayout_5.addWidget(self.checkBox_filter_uid)
        self.lineEdit_filter_uid = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_filter_uid.setObjectName("lineEdit_filter_uid")
        self.horizontalLayout_5.addWidget(self.lineEdit_filter_uid)
        self.horizontalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_filter_user_code = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox_filter_user_code.setText("")
        self.checkBox_filter_user_code.setObjectName("checkBox_filter_user_code")
        self.horizontalLayout_6.addWidget(self.checkBox_filter_user_code)
        self.lineEdit_filter_user_code = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_filter_user_code.setObjectName("lineEdit_filter_user_code")
        self.horizontalLayout_6.addWidget(self.lineEdit_filter_user_code)
        self.checkBox_ignore_trash = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox_ignore_trash.setChecked(True)
        self.checkBox_ignore_trash.setObjectName("checkBox_ignore_trash")
        self.horizontalLayout_6.addWidget(self.checkBox_ignore_trash)
        self.horizontalLayout_2.addWidget(self.groupBox_8)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_filter_name = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_filter_name.setText("")
        self.checkBox_filter_name.setObjectName("checkBox_filter_name")
        self.horizontalLayout_4.addWidget(self.checkBox_filter_name)
        self.lineEdit_filter_name = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_filter_name.setObjectName("lineEdit_filter_name")
        self.horizontalLayout_4.addWidget(self.lineEdit_filter_name)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_filter_state = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_filter_state.setText("")
        self.checkBox_filter_state.setObjectName("checkBox_filter_state")
        self.horizontalLayout_3.addWidget(self.checkBox_filter_state)
        self.comboBox_filter_state = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_filter_state.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_filter_state.setObjectName("comboBox_filter_state")
        self.horizontalLayout_3.addWidget(self.comboBox_filter_state)
        self.horizontalLayout_2.addWidget(self.groupBox_7)
        self.pushButton_reset = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.horizontalLayout_2.addWidget(self.pushButton_reset)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.scrollArea_list_facebook_account = QtWidgets.QScrollArea(Manage_Facebook_Account)
        self.scrollArea_list_facebook_account.setWidgetResizable(True)
        self.scrollArea_list_facebook_account.setObjectName("scrollArea_list_facebook_account")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 869, 420))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_list_facebook_account = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_list_facebook_account.setObjectName("verticalLayout_list_facebook_account")
        self.tableWidget_list_account = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_list_account.sizePolicy().hasHeightForWidth())
        self.tableWidget_list_account.setSizePolicy(sizePolicy)
        self.tableWidget_list_account.setObjectName("tableWidget_list_account")
        self.tableWidget_list_account.setColumnCount(0)
        self.tableWidget_list_account.setRowCount(0)
        self.verticalLayout_list_facebook_account.addWidget(self.tableWidget_list_account)
        self.label_status = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_status.setObjectName("label_status")
        self.verticalLayout_list_facebook_account.addWidget(self.label_status)
        self.scrollArea_list_facebook_account.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea_list_facebook_account)
        self.groupBox_statistics = QtWidgets.QGroupBox(Manage_Facebook_Account)
        self.groupBox_statistics.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_statistics.setObjectName("groupBox_statistics")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_statistics)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_state = QtWidgets.QScrollArea(self.groupBox_statistics)
        self.scrollArea_state.setWidgetResizable(True)
        self.scrollArea_state.setObjectName("scrollArea_state")
        self.scrollAreaWidgetContents_statistics = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_statistics.setGeometry(QtCore.QRect(0, 0, 849, 165))
        self.scrollAreaWidgetContents_statistics.setObjectName("scrollAreaWidgetContents_statistics")
        self.verticalLayout_statistics = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_statistics)
        self.verticalLayout_statistics.setObjectName("verticalLayout_statistics")
        self.list_statistics_state_child = QtWidgets.QListWidget(self.scrollAreaWidgetContents_statistics)
        self.list_statistics_state_child.setObjectName("list_statistics_state_child")
        self.verticalLayout_statistics.addWidget(self.list_statistics_state_child)
        self.scrollArea_state.setWidget(self.scrollAreaWidgetContents_statistics)
        self.verticalLayout_4.addWidget(self.scrollArea_state)
        self.verticalLayout.addWidget(self.groupBox_statistics)
        self.groupBox = QtWidgets.QGroupBox(Manage_Facebook_Account)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Reload = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Reload.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_Reload.setObjectName("pushButton_Reload")
        self.horizontalLayout.addWidget(self.pushButton_Reload)
        self.pushButton_OpenBrower = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_OpenBrower.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_OpenBrower.setObjectName("pushButton_OpenBrower")
        self.horizontalLayout.addWidget(self.pushButton_OpenBrower)
        self.pushButton_login = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_login.setEnabled(False)
        self.pushButton_login.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.pushButton_login)
        self.verticalLayout.addWidget(self.groupBox)
        self.label_result_api = QtWidgets.QLabel(Manage_Facebook_Account)
        self.label_result_api.setText("")
        self.label_result_api.setObjectName("label_result_api")
        self.verticalLayout.addWidget(self.label_result_api)

        self.retranslateUi(Manage_Facebook_Account)
        QtCore.QMetaObject.connectSlotsByName(Manage_Facebook_Account)

    def retranslateUi(self, Manage_Facebook_Account):
        _translate = QtCore.QCoreApplication.translate
        Manage_Facebook_Account.setWindowTitle(_translate("Manage_Facebook_Account", "Facebook_Account"))
        self.groupBox_4.setTitle(_translate("Manage_Facebook_Account", "filler"))
        self.groupBox_5.setTitle(_translate("Manage_Facebook_Account", "Filter by uid"))
        self.lineEdit_filter_uid.setPlaceholderText(_translate("Manage_Facebook_Account", "enter the uid"))
        self.groupBox_8.setTitle(_translate("Manage_Facebook_Account", "Filter by user code"))
        self.lineEdit_filter_user_code.setPlaceholderText(_translate("Manage_Facebook_Account", "enter the user code"))
        self.checkBox_ignore_trash.setText(_translate("Manage_Facebook_Account", "Ignore Trash"))
        self.groupBox_6.setTitle(_translate("Manage_Facebook_Account", "Filter by name"))
        self.lineEdit_filter_name.setPlaceholderText(_translate("Manage_Facebook_Account", "Enter the Name"))
        self.groupBox_7.setTitle(_translate("Manage_Facebook_Account", "Filter by State"))
        self.pushButton_reset.setText(_translate("Manage_Facebook_Account", "Reset"))
        self.label_status.setText(_translate("Manage_Facebook_Account", "Status."))
        self.groupBox_statistics.setTitle(_translate("Manage_Facebook_Account", "statistics"))
        self.pushButton_Reload.setText(_translate("Manage_Facebook_Account", "Reload"))
        self.pushButton_OpenBrower.setText(_translate("Manage_Facebook_Account", "Open Brower"))
        self.pushButton_login.setText(_translate("Manage_Facebook_Account", "Login"))
