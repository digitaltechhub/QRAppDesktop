# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt
from PIL import Image
from qrgenerator import qr_gen


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 459)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.qr_code_icon = QtWidgets.QLabel(self.centralwidget)
        self.qr_code_icon.setGeometry(QtCore.QRect(30, 30, 231, 211))
        self.qr_code_icon.setObjectName("qr_code_icon")

        self.dateEdit_in = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_in.setGeometry(QtCore.QRect(430, 120, 181, 26))
        self.dateEdit_in.setObjectName("dateEdit_in")
        self.dateEdit_in.setDateTime(QtCore.QDateTime.currentDateTime())

        self.start_time_in = QtWidgets.QTimeEdit(self.centralwidget)
        self.start_time_in.setGeometry(QtCore.QRect(430, 170, 181, 26))
        self.start_time_in.setObjectName("start_time_in")
        self.start_time_in.setTime(QtCore.QTime.currentTime())

        self.end_time_in = QtWidgets.QTimeEdit(self.centralwidget)
        self.end_time_in.setGeometry(QtCore.QRect(430, 210, 181, 26))
        self.end_time_in.setObjectName("end_time_in")
        # TODO: change the +3 below to a user defined value for flexibility
        self.end_time_in.setTime(QtCore.QTime(QtCore.QTime.currentTime().hour()+3, QtCore.QTime.currentTime().minute()))

        self.course_code_in = QtWidgets.QLineEdit(self.centralwidget)
        self.course_code_in.setGeometry(QtCore.QRect(360, 80, 251, 25))
        self.course_code_in.setText("")
        self.course_code_in.setPlaceholderText("Enter course code")
        self.course_code_in.setObjectName("course_code_in")
        self.course_name_in = QtWidgets.QLineEdit(self.centralwidget)
        self.course_name_in.setGeometry(QtCore.QRect(360, 30, 251, 25))
        self.course_name_in.setText("")
        self.course_name_in.setPlaceholderText("Enter course name")
        self.course_name_in.setObjectName("course_name_in")

        self.time_start_label = QtWidgets.QLabel(self.centralwidget)
        self.time_start_label.setGeometry(QtCore.QRect(360, 170, 71, 21))
        self.time_start_label.setObjectName("time_start_label")

        self.end_time_label = QtWidgets.QLabel(self.centralwidget)
        self.end_time_label.setGeometry(QtCore.QRect(360, 210, 61, 21))
        self.end_time_label.setObjectName("end_time_label")

        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(360, 120, 71, 21))
        self.date_label.setObjectName("date_label")

        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(70, 280, 89, 25))
        self.save_btn.setObjectName("pushButton")

        self.export_btn = QtWidgets.QPushButton(self.centralwidget)
        self.export_btn.setGeometry(QtCore.QRect(70, 330, 89, 25))
        self.export_btn.setObjectName("pushButton_2")

        self.create_new_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_new_btn.setGeometry(QtCore.QRect(430, 320, 89, 25))
        self.create_new_btn.setObjectName("pushButton_3")

        self.create_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_btn.setGeometry(QtCore.QRect(430, 270, 89, 25))
        self.create_btn.clicked.connect(self.on_create_clicked)
        self.create_btn.setObjectName("pushButton_4")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 22))
        self.menubar.setObjectName("menubar")

        self.menuQRDesk = QtWidgets.QMenu(self.menubar)
        self.menuQRDesk.setObjectName("menuQRDesk")

        self.menuReports = QtWidgets.QMenu(self.menubar)
        self.menuReports.setObjectName("menuReports")

        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionCreate_QR_Code = QtWidgets.QAction(MainWindow)
        self.actionCreate_QR_Code.setObjectName("actionCreate_QR_Code")

        self.actionView_Reports = QtWidgets.QAction(MainWindow)
        self.actionView_Reports.setObjectName("actionView_Reports")

        self.actionUser_Settings = QtWidgets.QAction(MainWindow)
        self.actionUser_Settings.setObjectName("actionUser_Settings")

        self.actionCheck_for_updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_updates.setObjectName("actionCheck_for_updates")

        self.menuQRDesk.addAction(self.actionCreate_QR_Code)

        self.menuReports.addAction(self.actionView_Reports)

        self.menuSettings.addAction(self.actionUser_Settings)
        self.menuSettings.addAction(self.actionCheck_for_updates)

        self.menubar.addAction(self.menuQRDesk.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.qr_code_icon.setText(_translate("MainWindow", "Generated QR Code"))
        self.time_start_label.setText(_translate("MainWindow", "Starts at :"))
        self.end_time_label.setText(_translate("MainWindow", "Ends at :"))
        self.date_label.setText(_translate("MainWindow", "Date :"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.export_btn.setText(_translate("MainWindow", "Export"))
        self.create_new_btn.setText(_translate("MainWindow", "Create New"))
        self.create_btn.setText(_translate("MainWindow", "Create"))
        self.menuQRDesk.setTitle(_translate("MainWindow", "QRDesk"))
        self.menuReports.setTitle(_translate("MainWindow", "Reports"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionCreate_QR_Code.setText(_translate("MainWindow", "Create QR Code"))
        self.actionView_Reports.setText(_translate("MainWindow", "View Reports"))
        self.actionUser_Settings.setText(_translate("MainWindow", "User Settings"))
        self.actionCheck_for_updates.setText(_translate("MainWindow", "Check for updates"))

    def on_create_clicked(self):
        course_name = self.course_name_in.text()
        course_code = self.course_code_in.text()
        start_time = self.start_time_in.time()
        start_time = str(start_time)
        end_time = self.end_time_in.time()
        end_time = str(end_time)
        date = self.dateEdit_in.date()
        date = date.toPyDate()

        string = (course_name + course_code + start_time + str(date))
        string = str(string)
        filename = str(str(date) + "-" + course_name + course_code + "-" + start_time)

        code = qr_gen(string, filename)

        pixmap = QPixmap(code)
        self.qr_code_icon.resize(pixmap.width(), pixmap.height())
        self.qr_code_icon.setPixmap(pixmap)
        self.qr_code_icon.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
