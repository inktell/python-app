from PyQt6 import QtWidgets,QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys
from database import *

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
        uic.loadUi("ui/login.ui",self)

        self.email = self.findChild(QLineEdit,"txt_email")
        self.password = self.findChild(QLineEdit,"txt_password")
        self.btn_login = self.findChild(QPushButton,"btn_login")
        self.btn_register = self.findChild(QPushButton,"btn_register")
        self.btn_eye_p = self.findChild(QPushButton,"btn_eye_p")

        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.show_register)
        self.btn_eye_p.clicked.connect(lambda : self.hiddenOrShow(self.password,self.btn_eye_p))

    def hiddenOrShow(self,input:QLineEdit,btn:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            btn.setIcon(QIcon("img/eye-solid.svg"))
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
        if user is not None:
            msg.success_box("Đăng nhập thành công")
            self.show_home(user["id"])
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
        uic.loadUi("ui/resgin.ui",self)

        self.name = self.findChild(QLineEdit,"txt_name")
        self.email = self.findChild(QLineEdit,"txt_email")
        self.password = self.findChild(QLineEdit,"txt_password")
        self.confirm_password = self.findChild(QLineEdit,"txt_conf_pwd")
        self.btn_register = self.findChild(QPushButton,"btn_register")
        self.btn_login = self.findChild(QPushButton,"btn_login")
        self.btn_eye_p = self.findChild(QPushButton,"btn_eye_p")
        self.btn_eye_cp = self.findChild(QPushButton,"btn_eye_cp")

        self.btn_register.clicked.connect(self.register)
        self.btn_login.clicked.connect(self.show_login)
        self.btn_eye_p.clicked.connect(lambda : self.hiddenOrShow(self.password,self.btn_eye_p))
        self.btn_eye_cp.clicked.connect(lambda : self.hiddenOrShow(self.confirm_password,self.btn_eye_cp))

    def hiddenOrShow(self,input:QLineEdit,btn:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            btn.setIcon(QIcon("img/eye-solid.svg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            btn.setIcon(QIcon("img/eye-slash-solid.svg"))

    def register(self):
        msg = MessageBox()
        name = self.name.text()
        email = self.email.text()
        password = self.password.text()
        confirm_password = self.confirm_password.text()

        if name == "":
            msg.error_box("Không thể để trống")
            self.name.setFocus()
            return
        
        if email == "":
            msg.error_box("Không thể để trống")
            self.email.setFocus()
            return
        
        if password == "":
            msg.error_box("Không thể để trống")
            self.password.setFocus()
            return
        
        if confirm_password == "":
            msg.error_box("Không thể để trống")
            self.confirm_password.setFocus()
            return
        
        if password != confirm_password:
            msg.error_box("Mật khẩu không trùng khớp")
            self.password.setFocus()
            return
        
        if not self.validate_email(email):
            msg.error_box("Email không hợp lệ")
            self.email.setFocus()
            return
        
        check_email = get_user_by_email(email)
        if check_email is not None:
            msg.error_box("Email đã tồn tại")

            return
        
        create_user(name,email,password)
        msg.success_box("Đăng ký thành công")
        self.show_login()

    def validate_email(self,s):
        idx_at = s.find("@")
        if idx_at == -1:
            return False
        return '.' in s[idx_at+1:]

    def show_login(self):
        self.login = Login()
        self.login.show()
        self.close()
        
class Home(QMainWindow):
    def __init__(self,user_id):
        super(Home,self).__init__()
        uic.loadUi("ui/menu.ui",self)

        self.main_window = self.findChild(QStackedWidget,"main_window")
        self.btn_account_info = self.findChild(QPushButton,"btn_account")

        self.account_widget = self.findChild(QStackedWidget,"account_widget")
        self.btn_nap_account = self.findChild(QPushButton,"btn_nap_account")
        self.btn_nap_bell = self.findChild(QPushButton,"btn_nap_bell")
        self.btn_nap_lock = self.findChild(QPushButton,"btn_nap_lock")
        self.btn_nap_bag = self.findChild(QPushButton,"btn_nap_bag")
        self.btn_nap_setting = self.findChild(QPushButton,"btn_nap_setting")

        self.user_id = user_id
        self.user = get_user_by_id(user_id)
        self.loadAccountInfo()
        self.btn_account_info.clicked.connect(lambda : self.navMainScreen(1))

        self.btn_nap_account.clicked.connect(lambda : self.navAccountScreen(0))
        self.btn_nap_bell.clicked.connect(lambda : self.navAccountScreen(2))
        self.btn_nap_lock.clicked.connect(lambda : self.navAccountScreen(3))
        self.btn_nap_bag.clicked.connect(lambda : self.navAccountScreen(4))
        self.btn_nap_setting.clicked.connect(lambda : self.navAccountScreen(1))
    
    def navMainScreen(self, index):
        self.main_window.setCurrentIndex(index)

    def navAccountScreen(self, index):
        self.account_widget.setCurrentIndex(index)

    def loadAccountInfo(self):
        self.txt_name = self.findChild(QLineEdit,"txt_name")
        self.txt_email = self.findChild(QLineEdit,"txt_email")
        self.txt_name.setText(self.user["name"])
        self.txt_email.setText(self.user["email"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())