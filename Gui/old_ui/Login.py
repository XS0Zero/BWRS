# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(250, 60, 321, 301))
        self.widget.setStyleSheet("#widget{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(30, 10, 271, 201))
        self.listWidget.setStyleSheet("background-color: rgb(216, 216, 216,180);\n"
"border-radius:25px;")
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 191, 31))
        self.lineEdit.setStyleSheet("border-radius:5px")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 120, 191, 31))
        self.lineEdit_2.setStyleSheet("border-radius:5px")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(60, 240, 81, 31))
        self.pushButton.setStyleSheet("#pushButton{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border:1px solid rgb(0,0,0);\n"
"    border-radius:8px;\n"
"}\n"
"#pushButton:hover{\n"
"    \n"
"    background-color: rgb(158, 158, 158);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#pushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 240, 81, 31))
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border:1px solid rgb(0,0,0);\n"
"    border-radius:8px;\n"
"}\n"
"#pushButton_2:hover{\n"
"    \n"
"    background-color: rgb(158, 158, 158);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#pushButton_2:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.label.setMaximumSize(QtCore.QSize(600, 400))
        self.label.setStyleSheet("opacity:0.5;\n"
"background-color: rgb(255, 255, 255,0);\n"
"border-image: url(:/images/resource/images/2.png);\n"
"border-radius:15px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "用户名："))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "密码："))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.label.setProperty("setWindowOpacity", _translate("MainWindow", "0.7"))
import resource_rc
