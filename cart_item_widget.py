from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QPixmap

class CartItemWidget(QWidget):
    remove_clicked = pyqtSignal(int)  # product_id

    def __init__(self, cart_item, parent=None):
        super().__init__(parent)
        self.cart_item = cart_item
        self.product_id = cart_item['product_id']
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(12)

        # Ảnh
        img_label = QLabel()
        img_label.setFixedSize(64, 64)
        img_label.setStyleSheet('background: #f8f9fa; border: 1px solid #eee; border-radius: 8px;')
        if self.cart_item['img']:
            pixmap = QPixmap(self.cart_item['img'])
            img_label.setPixmap(pixmap.scaled(64, 64, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        layout.addWidget(img_label)

        # Thông tin
        info_layout = QVBoxLayout()
        title = QLabel(self.cart_item['title'])
        title.setStyleSheet('font-weight: bold; font-size: 15px; color: #222;')
        price = QLabel(f"₫{int(float(str(self.cart_item['price']).replace(',', ''))):,}")
        price.setStyleSheet('color: #ee4d2d; font-size: 14px; font-weight: bold;')
        info_layout.addWidget(title)
        info_layout.addWidget(price)
        layout.addLayout(info_layout)

        # Spacer
        layout.addStretch()

        # Nút xóa
        remove_btn = QPushButton('Xóa')
        remove_btn.setStyleSheet('background: #fff; color: #ee4d2d; border: 1px solid #ee4d2d; border-radius: 6px; padding: 6px 16px; font-weight: bold;')
        remove_btn.clicked.connect(lambda: self.remove_clicked.emit(self.product_id))
        layout.addWidget(remove_btn) 