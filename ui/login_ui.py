# Form implementation generated from reading ui file '/Users/pinxun/Documents/MindX/PTA/PTA08/LeTien/python-app/ui/login.ui'
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
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.email = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.email.setGeometry(QtCore.QRect(400, 210, 271, 51))
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
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 270, 271, 51))
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
        self.login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login.setGeometry(QtCore.QRect(440, 350, 191, 51))
        self.login.setStyleSheet("background-color: rgb(249, 79, 47);\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s ease;")
        self.login.setObjectName("login")
        self.google = QtWidgets.QPushButton(parent=self.centralwidget)
        self.google.setGeometry(QtCore.QRect(380, 440, 151, 51))
        self.google.setStyleSheet("background-color: #ffffff; /* Nền trắng */\n"
"    color: #000000; /* Chữ màu đen */\n"
"    border: 1px solid #cccccc; /* Viền xám nhạt */\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/LeTien/python-app/ui/../img/download.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.google.setIcon(icon)
        self.google.setObjectName("google")
        self.face = QtWidgets.QPushButton(parent=self.centralwidget)
        self.face.setGeometry(QtCore.QRect(540, 440, 151, 51))
        self.face.setStyleSheet("background-color: #ffffff; /* Nền trắng */\n"
"    color: #000000; /* Chữ màu đen */\n"
"    border: 1px solid #cccccc; /* Viền xám nhạt */\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/LeTien/python-app/ui/../img/download (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.face.setIcon(icon1)
        self.face.setObjectName("face")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 410, 221, 20))
        self.label_4.setStyleSheet("    color: #a0a0a0; /* Màu xám nhạt */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    background: transparent;")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 170, 211, 20))
        self.label_6.setStyleSheet("\n"
"    font-size: 14px;\n"
"    font-weight: normal;\n"
"    color: #a0a0a0; /* Màu xám nhạt */")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 140, 171, 41))
        self.label_5.setStyleSheet("    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #000000; /* Màu đen */\n"
"    margin-bottom: 8px;")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 50, 381, 471))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/LeTien/python-app/ui/../img/12.png"))
        self.label_7.setObjectName("label_7")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 748, 609))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(570, 500, 71, 16))
        self.label_2.setStyleSheet("    color: #ffa14a; /* Màu cam */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    cursor: pointer;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(430, 500, 141, 16))
        self.label_3.setStyleSheet("    color: #a0a0a0; /* Màu chữ xám nhạt */\n"
"    font-size: 14px;\n"
"    font-weight: normal;")
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(parent=self.frame)
        self.label_8.setGeometry(QtCore.QRect(440, 60, 321, 81))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/LeTien/python-app/ui/../img/44.png"))
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(560, 320, 131, 31))
        self.label.setStyleSheet("    color: #a0a0a0; /* Màu chữ xám nhạt */\n"
"    font-size: 14px;\n"
"    font-weight: normal;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 270, 61, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/LeTien/python-app/ui/../img/mắt mở.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.frame.raise_()
        self.email.raise_()
        self.lineEdit_2.raise_()
        self.login.raise_()
        self.google.raise_()
        self.face.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.pushButton.raise_()
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
        self.email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.google.setText(_translate("MainWindow", "Google"))
        self.face.setText(_translate("MainWindow", "Facebook"))
        self.label_4.setText(_translate("MainWindow", "or login with"))
        self.label_6.setText(_translate("MainWindow", " Please login to your account"))
        self.label_5.setText(_translate("MainWindow", "Welcome Back"))
        self.label_2.setText(_translate("MainWindow", "Signup"))
        self.label_3.setText(_translate("MainWindow", "Don\'t have an account"))
        self.label.setText(_translate("MainWindow", "Forgot a pasword?"))
