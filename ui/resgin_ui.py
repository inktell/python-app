# Form implementation generated from reading ui file '/Users/pinxun/Documents/MindX/PTA/PTA08/LeTien/python-app/ui/resgin.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 609)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 50, 381, 471))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/LeTien/python-app/ui/../img/12.png"))
        self.label_7.setObjectName("label_7")
        self.login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login.setGeometry(QtCore.QRect(430, 440, 191, 51))
        self.login.setStyleSheet("background-color: rgb(250, 79, 48);\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s ease;")
        self.login.setObjectName("login")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 748, 609))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.checkBox = QtWidgets.QCheckBox(parent=self.frame)
        self.checkBox.setGeometry(QtCore.QRect(380, 410, 231, 22))
        self.checkBox.setStyleSheet("    color: #a0a0a0; /* Màu xám nhạt */\n"
"    font-size: 14px;\n"
"    font-weight: normal;\n"
"    spacing: 8px; /* Khoảng cách giữa ô checkbox và văn bản */")
        self.checkBox.setObjectName("checkBox")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 350, 271, 51))
        self.lineEdit_2.setAccessibleName("")
        self.lineEdit_2.setAccessibleDescription("")
        self.lineEdit_2.setStyleSheet("    background-color: #f9f9f9;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    color: #333;")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.email = QtWidgets.QLineEdit(parent=self.frame)
        self.email.setGeometry(QtCore.QRect(370, 290, 271, 51))
        self.email.setAccessibleName("")
        self.email.setAccessibleDescription("")
        self.email.setStyleSheet("    background-color: #f9f9f9;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    color: #333;")
        self.email.setInputMask("")
        self.email.setText("")
        self.email.setObjectName("email")
        self.email_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.email_2.setGeometry(QtCore.QRect(370, 230, 271, 51))
        self.email_2.setAccessibleName("")
        self.email_2.setAccessibleDescription("")
        self.email_2.setStyleSheet("    background-color: #f9f9f9;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    color: #333;")
        self.email_2.setInputMask("")
        self.email_2.setText("")
        self.email_2.setObjectName("email_2")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(380, 510, 151, 16))
        self.label.setStyleSheet("    color: #a0a0a0; /* Màu xám nhạt */\n"
"    font-size: 14px;\n"
"    font-weight: normal;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(530, 510, 49, 16))
        self.label_3.setStyleSheet("color: rgb(250, 79, 48);\n"
"    font-weight: bold;\n"
"    text-decoration: underline; /* Gạch chân khi hover */")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(390, 170, 271, 51))
        self.label_6.setStyleSheet("\n"
"    font-size: 14px;\n"
"    font-weight: normal;\n"
"    color: #a0a0a0; /* Màu xám nhạt */")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(470, 140, 171, 41))
        self.label_5.setStyleSheet("    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #000000; /* Màu đen */\n"
"    margin-bottom: 8px;")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(420, 50, 311, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/LeTien/python-app/ui/../img/44.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(580, 350, 61, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/LeTien/python-app/ui/../img/mắt mở.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.frame.raise_()
        self.label_7.raise_()
        self.login.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login.setText(_translate("MainWindow", "Signup"))
        self.checkBox.setText(_translate("MainWindow", "I agree to the Terms & Privacy"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.email_2.setPlaceholderText(_translate("MainWindow", "Full name"))
        self.label.setText(_translate("MainWindow", "Already have an account?"))
        self.label_3.setText(_translate("MainWindow", "Login"))
        self.label_6.setText(_translate("MainWindow", "Enter your details below to creater\n"
" account and get started"))
        self.label_5.setText(_translate("MainWindow", "Signup"))
