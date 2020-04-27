# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginwindow(object):
    def setupUi(self, loginwindow):
        loginwindow.setObjectName("loginwindow")
        loginwindow.resize(1023, 948)
        self.centralwidget = QtWidgets.QWidget(loginwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 300, 61, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 380, 68, 19))
        self.label_2.setObjectName("label_2")
        self.user_name = QtWidgets.QLineEdit(self.centralwidget)
        self.user_name.setGeometry(QtCore.QRect(370, 320, 191, 25))
        self.user_name.setObjectName("user_name")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setGeometry(QtCore.QRect(370, 380, 191, 25))
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(390, 450, 112, 34))
        self.login.setObjectName("login")
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setGeometry(QtCore.QRect(640, 340, 112, 34))
        self.register_2.setObjectName("register_2")
        self.disp1 = QtWidgets.QLabel(self.centralwidget)
        self.disp1.setGeometry(QtCore.QRect(400, 560, 68, 19))
        self.disp1.setObjectName("disp1")
        loginwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1023, 30))
        self.menubar.setObjectName("menubar")
        loginwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginwindow)
        self.statusbar.setObjectName("statusbar")
        loginwindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginwindow)
        QtCore.QMetaObject.connectSlotsByName(loginwindow)

    def retranslateUi(self, loginwindow):
        _translate = QtCore.QCoreApplication.translate
        loginwindow.setWindowTitle(_translate("loginwindow", "登录"))
        self.label.setText(_translate("loginwindow", "用户名"))
        self.label_2.setText(_translate("loginwindow", "密码"))
        self.login.setText(_translate("loginwindow", "登录"))
        self.register_2.setText(_translate("loginwindow", "注册"))
        self.disp1.setText(_translate("loginwindow", "TextLabel"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1076, 949)
        MainWindow.setSizeIncrement(QtCore.QSize(5, 5))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 290, 151, 19))
        self.label.setBaseSize(QtCore.QSize(5, 5))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 360, 111, 19))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(400, 290, 261, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 360, 261, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 470, 112, 34))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1076, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "注册"))
        self.label.setText(_translate("MainWindow", "输入你的用户名"))
        self.label_2.setText(_translate("MainWindow", "输入你的密码"))
        self.pushButton.setText(_translate("MainWindow", "注册"))