import os
from PyQt6 import QtWidgets,QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys
from database import *
from pro_list_widget import ProductListWidget
from cart_item_widget import CartItemWidget

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
        email = self.email.text().strip()
        password = self.password.text().strip()

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
        name = self.name.text().strip()
        email = self.email.text().strip()
        password = self.password.text().strip()
        confirm_password = self.confirm_password.text().strip()

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
        self.btn_bag = self.findChild(QPushButton,"btn_bag")
        self.btn_shopee = self.findChild(QPushButton,"btn_shopee")
        self.btn_bell = self.findChild(QPushButton,"btn_bell")

        self.account_widget = self.findChild(QStackedWidget,"account_widget")
        self.btn_nap_account = self.findChild(QPushButton,"btn_nap_account")
        self.btn_nap_bell = self.findChild(QPushButton,"btn_nap_bell")
        self.btn_nap_lock = self.findChild(QPushButton,"btn_nap_lock")
        self.btn_nap_bag = self.findChild(QPushButton,"btn_nap_bag")
        self.btn_nap_setting = self.findChild(QPushButton,"btn_nap_setting")

        self.danhmuc_widget = self.findChild(QStackedWidget,"danhmuc_widget")

        self.user_id = user_id
        self.user = get_user_by_id(user_id)
        
        self.loadAccountInfo()
        self.btn_account_info.clicked.connect(lambda : self.navMainScreen(1))
        self.btn_bag.clicked.connect(lambda : self.navMainScreen(4))
        self.btn_shopee.clicked.connect(lambda : self.navMainScreen(0))
        self.btn_bell.clicked.connect(lambda : self.navMainScreen(1))

        self.btn_avatar = self.findChild(QPushButton,"btn_avatar")
        self.btn_avatar.clicked.connect(self.update_avatar)

        self.btn_account_info.clicked.connect(lambda : self.navAccountScreen(0))
        self.btn_nap_account.clicked.connect(lambda : self.navAccountScreen(0))
        self.btn_nap_bell.clicked.connect(lambda : self.navAccountScreen(1))
        self.btn_nap_lock.clicked.connect(lambda : self.navAccountScreen(2))
        self.btn_nap_bag.clicked.connect(lambda : self.navAccountScreen(3))
        self.btn_nap_setting.clicked.connect(lambda : self.navAccountScreen(4))
        self.btn_bell.clicked.connect(lambda : self.navAccountScreen(1))

        self.btn_luu = self.findChild(QPushButton,"btn_save")
        self.btn_luu.clicked.connect(self.update_info)
        self.btn_luu.clicked.connect(lambda :self.navAccountScreen(0))

        self.txt_pass_old = self.findChild(QLineEdit,"txt_pass_old")
        self.txt_pass_new = self.findChild(QLineEdit,"txt_pass_new")
        self.txt_pass_new2 = self.findChild(QLineEdit,"txt_pass_new2")
        self.btn_up_pass = self.findChild(QPushButton,"btn_up_pass")
        self.btn_eye_p = self.findChild(QPushButton,"btn_eye_p")
        self.btn_eye_p_2 = self.findChild(QPushButton,"btn_eye_p_2")
        self.btn_eye_p_3 = self.findChild(QPushButton,"btn_eye_p_3")
        
        self.btn_up_pass.clicked.connect(self.update_password)
        self.btn_eye_p.clicked.connect(lambda : self.hiddenOrShow(self.txt_pass_old,self.btn_eye_p))
        self.btn_eye_p_2.clicked.connect(lambda : self.hiddenOrShow(self.txt_pass_new,self.btn_eye_p_2))
        self.btn_eye_p_3.clicked.connect(lambda : self.hiddenOrShow(self.txt_pass_new2,self.btn_eye_p_3))

        self.btn_re_user = self.findChild(QPushButton,"btn_re_user")
        self.btn_re_user.clicked.connect(self.remove_user)

        # Initialize product list widget
        self.pro_list_widget = self.findChild(QWidget,"pro_list_widget")
        self.product_list = ProductListWidget()
        
        # Create layout for pro_list_widget
        pro_list_layout = QVBoxLayout(self.pro_list_widget)
        pro_list_layout.setContentsMargins(0, 0, 0, 0)
        pro_list_layout.addWidget(self.product_list)
        
        # Connect product list signals
        self.product_list.product_clicked.connect(self.on_product_clicked)
        self.product_list.product_liked.connect(self.on_product_liked)
        self.product_list.product_buy_now.connect(self.on_product_buy_now)

        # Cart widget
        self.cart_widget = self.findChild(QWidget, "cart_widget")
        self.cart_layout = QVBoxLayout(self.cart_widget)
        self.cart_layout.setContentsMargins(8, 8, 8, 8)
        self.cart_layout.setSpacing(8)
        # Kết nối chuyển tab cart
        self.main_window.currentChanged.connect(self.on_main_window_changed)

    def navMainScreen(self, index):
        self.main_window.setCurrentIndex(index)

    def navAccountScreen(self, index):
        self.account_widget.setCurrentIndex(index)

    def loadAccountInfo(self):
        self.txt_name = self.findChild(QLineEdit,"txt_name")
        self.txt_email = self.findChild(QLineEdit,"txt_email")
        self.cb_gender = self.findChild(QComboBox,"cb_gender")

        if self.user["avatar"]:
            self.btn_avatar.setIcon(QIcon(self.user["avatar"]))

        if not self.user["gender"]:
            self.cb_gender.setCurrentIndex(0)
        elif self.user["gender"] == "Nam":
            self.cb_gender.setCurrentIndex(1)
        elif self.user["gender"] == "Nữ":
            self.cb_gender.setCurrentIndex(2)
        else:
            self.cb_gender.setCurrentIndex(3)

        self.txt_name.setText(self.user["name"])
        self.txt_email.setText(self.user["email"])

    def update_avatar(self):
            file = QFileDialog.getOpenFileName(self, "Chọn ảnh đại diện", "", "Images (*.png *.jpg *.jpeg)")[0]
            if file:
                self.user["avatar"] = file
                self.btn_avatar.setIcon(QIcon(file))
                update_avatar_user(self.user_id, file)
                
    def update_info(self):
        self.msg = MessageBox()
        name = self.txt_name.text().strip()
        email = self.txt_email.text().strip()
        gender = self.cb_gender.currentText()

        update_user(self.user_id, name, email, gender)
        self.msg.success_box("Cập nhật thông tin thành công")

    def hiddenOrShow(self,input:QLineEdit,btn:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            btn.setIcon(QIcon("img/eye-solid.svg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            btn.setIcon(QIcon("img/eye-slash-solid.svg"))

    def update_password(self):
        self.msg = MessageBox()
        old_pass = self.txt_pass_old.text().strip()
        new_pass = self.txt_pass_new.text().strip()
        new_pass2 = self.txt_pass_new2.text().strip()

        if old_pass == "" or new_pass == "" or new_pass2 == "":
            self.msg.error_box("Không thể để trống")
            return
        
        if new_pass != new_pass2:
            self.msg.error_box("Mật khẩu mới không trùng khớp")
            return
        
        user = get_user_by_id(self.user_id)
        if user["password"] != old_pass:
            self.msg.error_box("Mật khẩu cũ không đúng")
            return
        
        update_password_user(self.user_id, new_pass)
        self.msg.success_box("Cập nhật mật khẩu thành công")
        
    def remove_user(self):
        self.msg = MessageBox()

        remove_user(self.user_id)
        self.msg.success_box("Xóa tài khoản thành công")
        self.show_login()

    def show_login(self):
        self.login = Login()
        self.login.show()
        self.close()

    def on_product_clicked(self, product_id):
        """Handle product card click"""
        product = get_product_by_id(product_id)
        if product:
            self.fill_detail(product)
            self.navMainScreen(3)

    def fill_detail(self, product):
        # Lấy widget detail
        detail_widget = self.main_window.widget(3)
        # Lấy các thành phần
        img_label = detail_widget.findChild(QLabel, "detailImage")
        title_label = detail_widget.findChild(QLabel, "detailTitle")
        price_label = detail_widget.findChild(QLabel, "detailPrice")
        old_price_label = detail_widget.findChild(QLabel, "detailOldPrice")
        rating_label = detail_widget.findChild(QLabel, "detailRating")
        sold_label = detail_widget.findChild(QLabel, "detailSold")
        category_label = detail_widget.findChild(QLabel, "detailCategory")
        desc_label = detail_widget.findChild(QLabel, "detailDescription")
        shipping_label = detail_widget.findChild(QLabel, "detailShipping")
        # Helper chuyển số
        def safe_float(val):
            try:
                return float(str(val).replace(",", "").strip())
            except:
                return 0.0
        # Ảnh
        if product['img']:
            pixmap = QPixmap(product['img'])
            img_label.setPixmap(pixmap.scaled(img_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        else:
            img_label.setText("No Image")
        # Tên
        title_label.setText(product['title'])
        # Giá
        price = safe_float(product['price'])
        price_label.setText(f"₫{int(price):,}")
        # Giá gốc
        original_price = safe_float(product['original_price'])
        if product['original_price'] and original_price > price:
            old_price_label.setText(f"₫{int(original_price):,}")
            old_price_label.setVisible(True)
        else:
            old_price_label.setVisible(False)
        # Đánh giá
        rating = safe_float(product['rate'])
        rating_label.setText(f"⭐ {rating:.1f}")
        # Đã bán
        sold = safe_float(product['sold'])
        sold_label.setText(f"Đã bán {sold:,.0f}")
        # Danh mục
        category_label.setText(product['category'] or "")
        # Mô tả
        desc_label.setText(product['description'] or "")
        # Vận chuyển
        shipping_label.setText("Miễn phí vận chuyển toàn quốc")
        # Kết nối nút thêm vào giỏ hàng
        add_btn = detail_widget.findChild(QPushButton, "detailAddToCartBtn")
        add_btn.clicked.connect(lambda: self.add_product_to_cart(product))

    def on_product_liked(self, product_id):
        """Handle product like button click"""
        self.msg = MessageBox()
        self.msg.success_box(f"Đã thêm sản phẩm ID: {product_id} vào danh sách yêu thích")
        # TODO: Add to favorites list
    
    def on_product_buy_now(self, product_id):
        """Handle product buy now button click"""
        self.msg = MessageBox()
        self.msg.success_box(f"Đã thêm sản phẩm ID: {product_id} vào giỏ hàng")
        # TODO: Add to cart

    def add_product_to_cart(self, product):
        add_to_cart(self.user_id, product)
        self.msg = MessageBox()
        self.msg.success_box("Đã thêm vào giỏ hàng!")

    def on_main_window_changed(self, index):
        # Nếu chuyển sang tab cart (index 4), load lại cart
        if index == 4:
            self.load_cart()

    def load_cart(self):
        # Xóa widget cũ
        while self.cart_layout.count():
            item = self.cart_layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()
        # Lấy cart
        cart = get_cart_by_user(self.user_id)
        for item in cart:
            w = CartItemWidget(item)
            w.remove_clicked.connect(lambda pid, uid=self.user_id: self.remove_cart_item(uid, pid))
            self.cart_layout.addWidget(w)
        self.cart_layout.addStretch()

    def remove_cart_item(self, user_id, product_id):
        remove_from_cart(user_id, product_id)
        self.load_cart()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    # login = Home(1)
    login.show()
    sys.exit(app.exec())