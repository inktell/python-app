from PyQt6 import QtWidgets,Qtcore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys
from setup_db import *

class MessageBox():
    def success_box(self,message):
        box = QMessageBox()
        box.setWindowTitle("Success")
        box.setText(message)
        box.setIcon(QMessageBox.Icon.Information)
        box.exec()
    def error_box(self,message):
        box = QMessageBox()
        box.setWindowTitle("Error")
        box.setText(message)
        box.setIcon(QMessageBox.Icon.Critical)
        box.exec()
    
class Login(QMainWindow):
    def __init__(self):
        super(Login,self).__init__()
        uic.loadUi("login.ui",self)

        self.email = self.findChild(QLineEdit,"email")
        self.password = self.findChild(QLineEdit,"password")
        self.btn_login = self.findChild(QPushButton,"btn_login")
        self.btn_register = self.findChild(QPushButton,"btn_register")
        self.btn_eye_p = self.findChild(QPushButton,"btn_eye_p")

        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.register)
        self.btn_eye_p.clicked.connect(lambda : self.hiddenOrShow(self.password,self.btn_eye_p))

    def hiddenOrShow(self,input:QLineEdit,btn:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Normal:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            btn.setIcon(QIcon("img/eye-solid.png"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            btn.setIcon(QIcon("img/eye-slash-solid.svg"))

    def login(self):
        msg = MessageBox()
        email = self.email.text()
        password = self.password.text()

        if email == "":
            msg.error_box("không thể để trống")
            self.email.setFocus()
            return

        if password == "":
            msg.error_box("không thể để trống")
            self.password.setFocus()
            return
        
        user = get_user_by_email_and_password(email,password)
        if user is None:
            msg.success_box("Đăng nhập thành công")
            self.show_home(user{"id"})
            return

        msg.error_box("Đăng nhập thất bại")

    def show_home(self,user_id):
        self.home = Home(user_id)
        self.home.show()
        self.close()

    def show_register(self):
        self.register = Register()
        self.register.show()
        self.close()
    
    def show_register(self):
        self.register = Register()
        self.register.show()
        self.close()

class Register(QMainWindow):
    def __init__(self):
        super(Register,self).__init__()
        uic.loadUi("register.ui",self)

        self.email = self.findChild(QLineEdit,"email")
        self.password = self.findChild(QLineEdit,"password")
        self.btn_register = self.findChild(QPushButton,"btn_register")
        self.btn_login = self.findChild(QPushButton,"btn_login")
        self.btn_eye_p = self.findChild(QPushButton,"btn_eye_p")

        self.btn_register.clicked.connect(self.register)
        self.btn_login.clicked.connect(self.login)
        self.btn_eye_p.clicked.connect(lambda : self.hiddenOrShow(self.password,self.btn_eye_p))