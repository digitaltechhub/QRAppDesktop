# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import signup
import main_window
import os,sys
sys.path.append(os.path.abspath('../database'))
import sql_connect

# TODO: Check if user is connected to the internet
# TODO: add a table for last login details, updates on successful login
# TODO: implement forgot password dialog


class Ui_login_frame(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.reg = signup.Ui_Signup()
        self.main_window = main_window.Ui_MainWindow()
        self.setupUi(self)

    def setupUi(self, login_frame):
        login_frame.setObjectName("login_frame")
        login_frame.resize(334, 387)
        # login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # login_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.user_icon = QtWidgets.QLabel(login_frame)
        self.user_icon.setGeometry(QtCore.QRect(140, 40, 71, 81))
        self.user_icon.setObjectName("user_icon")
        image = QtGui.QImage("../images/icons8-user-96.png")
        pp = QtGui.QPixmap.fromImage(image)
        self.user_icon.setPixmap(pp)
        self.user_icon.resize(pp.width(), pp.height())
        self.user_icon.show()

        self.user_name_in = QtWidgets.QLineEdit(login_frame)
        self.user_name_in.setGeometry(QtCore.QRect(100, 160, 161, 25))
        self.user_name_in.setText("")
        self.user_name_in.setObjectName("user_name_in")
        self.user_name_in.setPlaceholderText("Enter Username")
        self.user_name_in.textChanged.connect(self.enable_button)

        self.user_pwd_in = QtWidgets.QLineEdit(login_frame)
        self.user_pwd_in.setGeometry(QtCore.QRect(100, 210, 161, 25))
        self.user_pwd_in.setText("")
        self.user_pwd_in.setObjectName("user_pwd_in")
        self.user_pwd_in.setPlaceholderText("Enter Password")
        self.user_pwd_in.setEchoMode(QtWidgets.QLineEdit.Password)
        self.user_pwd_in.textChanged.connect(self.enable_button)

        self.login_btn = QtWidgets.QPushButton(login_frame)
        self.login_btn.setGeometry(QtCore.QRect(130, 260, 89, 25))
        self.login_btn.setObjectName("login_btn")
        self.login_btn.setDisabled(True)
        self.login_btn.setToolTip('Fill all fields to enable')
        self.login_btn.clicked.connect(self.onLoginBtnClicked)

        self.register_btn = QtWidgets.QPushButton(login_frame)
        self.register_btn.setGeometry(QtCore.QRect(130, 300, 89, 25))
        self.register_btn.setObjectName("register_btn")
        self.register_btn.clicked.connect(self.on_register_btn)

        self.retranslateUi(login_frame)
        QtCore.QMetaObject.connectSlotsByName(login_frame)

    def on_register_btn(self):
        self.close()
        self.reg.show()

    def onLoginBtnClicked(self):
        Username = self.user_name_in.text()
        Password = self.user_pwd_in.text()

        if sql_connect.login_user(Username, Password):
            self.close()
            self.main_window.show()

    def enable_button(self):
        if len(self.user_name_in.text()) > 0 and len(self.user_pwd_in.text()) > 0:
            self.login_btn.setDisabled(False)

    def retranslateUi(self, login_frame):
        _translate = QtCore.QCoreApplication.translate
        login_frame.setWindowTitle(_translate("login_frame", "User Login"))
        # self.user_icon.setText(_translate("login_frame", "user icon"))
        self.login_btn.setText(_translate("login_frame", "Login"))
        self.register_btn.setText(_translate("login_frame", "Register"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_login_frame()
    ui.show()
    sys.exit(app.exec_())
