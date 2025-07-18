import sys
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap, QFont
from ui.pro_item_ui import Ui_ProductCard
import database


class ProductCard(QWidget):
    """
    Modern product card widget with gradient design and improved UX
    """
    
    # Signals for user interactions
    buy_now_clicked = pyqtSignal(int)    # product_id
    like_clicked = pyqtSignal(int)       # product_id
    card_clicked = pyqtSignal(int)       # product_id
    
    def __init__(self, product_data=None, parent=None):
        super().__init__(parent)
        
        # Setup UI
        self.ui = Ui_ProductCard()
        self.ui.setupUi(self)
        
        # Initialize product data
        self.product_data = product_data or {}
        self.product_id = self.product_data.get('id', 0)
        self.is_liked = False
        
        # Connect signals
        self.ui.buyNowBtn.clicked.connect(self._on_buy_now_clicked)
        self.ui.likeBtn.clicked.connect(self._on_like_clicked)
        
        # Make the entire card clickable
        self.mousePressEvent = self._on_card_clicked
        
        # Update display if product data is provided
        if product_data:
            self.update_product_data(product_data)
    
    def update_product_data(self, product_data):
        """Update the card with new product data"""
        self.product_data = product_data
        self.product_id = product_data.get('id', 0)
        
        # Update product name
        title = product_data.get('title', 'Tên sản phẩm')
        # Truncate long titles
        if len(title) > 50:
            title = title[:47] + "..."
        self.ui.productName.setText(title)
        
        # Helper chuyển số
        def safe_float(val):
            try:
                return float(str(val).replace(',', '').strip())
            except Exception:
                return 0.0

        # Update prices
        current_price = safe_float(product_data.get('price', 0))
        original_price = safe_float(product_data.get('original_price', 0))
        
        # Format price with K/M suffix
        current_price_text = self._format_price(current_price)
        self.ui.currentPrice.setText(f"₫{current_price_text}")
        
        if original_price and original_price > current_price:
            original_price_text = self._format_price(original_price)
            self.ui.oldPrice.setText(f"₫{original_price_text}")
            self.ui.oldPrice.setVisible(True)
        else:
            self.ui.oldPrice.setVisible(False)
        
        # Update rating
        rating = product_data.get('rate', 0)
        try:
            rating = float(rating)
        except (ValueError, TypeError):
            rating = 0.0
        rating_stars = self._get_rating_stars(rating)
        self.ui.ratingDisplay.setText(f"{rating_stars} {rating:.1f}")
        
        # Update sales count
        sold = product_data.get('sold', 0)
        sold_text = self._format_sold_count(sold)
        self.ui.salesCount.setText(f"Đã bán {sold_text}")
        
        # Update image
        image_path = product_data.get('img', '')
        self._load_product_image(image_path)
    
    def _format_price(self, price):
        """Format price with K/M suffix"""
        # Convert price to float if it's a string
        try:
            price = float(price)
        except (ValueError, TypeError):
            price = 0.0
            
        if price >= 1000000:
            return f"{price/1000000:.1f}M"
        elif price >= 1000:
            return f"{price/1000:.0f}K"
        else:
            return str(int(price))
    
    def _get_rating_stars(self, rating):
        """Convert rating to star display"""
        full_stars = int(rating)
        has_half_star = rating % 1 >= 0.5
        empty_stars = 5 - full_stars - (1 if has_half_star else 0)
        
        stars = "⭐" * full_stars
        if has_half_star:
            stars += "⭐"
        stars += "☆" * empty_stars
        
        return stars
    
    def _format_sold_count(self, sold):
        """Format sold count for display"""
        # Convert sold to float if it's a string
        try:
            sold = float(sold)
        except (ValueError, TypeError):
            sold = 0.0
            
        if sold >= 1000000:
            return f"{sold/1000000:.1f}M"
        elif sold >= 1000:
            return f"{sold/1000:.1f}k"
        else:
            return str(int(sold))
    
    def _load_product_image(self, image_path):
        """Load and display product image"""
        if image_path:
            try:
                pixmap = QPixmap(image_path)
                if not pixmap.isNull():
                    # Scale pixmap to fit the container while maintaining aspect ratio
                    scaled_pixmap = pixmap.scaled(
                        self.ui.imageContainer.size(),
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                    self.ui.imageContainer.setPixmap(scaled_pixmap)
                else:
                    self._set_default_image()
            except Exception as e:
                print(f"Error loading image {image_path}: {e}")
                self._set_default_image()
        else:
            self._set_default_image()
    
    def _set_default_image(self):
        """Set default placeholder image"""
        self.ui.imageContainer.setText("📦\nKhông có ảnh")
        self.ui.imageContainer.setStyleSheet("""
            QLabel#imageContainer {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #f8f9fa, stop:1 #e9ecef);
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 8px;
                font-size: 20px;
                color: #6c757d;
            }
        """)
    
    def set_like_state(self, is_liked):
        """Set the like button state"""
        self.is_liked = is_liked
        if is_liked:
            self.ui.likeBtn.setText("❤️")
            self.ui.likeBtn.setStyleSheet("""
                QPushButton#likeBtn {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 #e74c3c, stop:1 #c0392b);
                    border: 1px solid #c0392b;
                    border-radius: 8px;
                    font-size: 16px;
                    color: white;
                }
                QPushButton#likeBtn:hover {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 #c0392b, stop:1 #a93226);
                    border-color: #a93226;
                }
            """)
        else:
            self.ui.likeBtn.setText("💖")
            self.ui.likeBtn.setStyleSheet("""
                QPushButton#likeBtn {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 #ecf0f1, stop:1 #bdc3c7);
                    border: 1px solid #bdc3c7;
                    border-radius: 8px;
                    font-size: 16px;
                    color: #7f8c8d;
                }
                QPushButton#likeBtn:hover {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 #e74c3c, stop:1 #c0392b);
                    color: white;
                    border-color: #c0392b;
                }
            """)
    
    def _on_buy_now_clicked(self):
        """Handle buy now button click"""
        self.buy_now_clicked.emit(self.product_id)
    
    def _on_like_clicked(self):
        """Handle like button click"""
        self.set_like_state(not self.is_liked)
        self.like_clicked.emit(self.product_id)
    
    def _on_card_clicked(self, event):
        """Handle card click for product details"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.card_clicked.emit(self.product_id)
        super().mousePressEvent(event)


# Example usage and testing
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create a sample product item
    sample_product = {
        'id': 1,
        'title': 'Ví nam Playboy kẻ, Combo Ví da nam nhỏ gọn & Bọc Căn Cước Công Dân DODANA dáng ngang da PU',
        'price': 1900,
        'original_price': 10000,
        'rate': 4.6,
        'sold': 78600,
        'img': 'img_pro/vi.webp'
    }
    
    # Create and show the widget
    widget = ProductCard(sample_product)
    widget.show()
    
    # Connect signals for testing
    widget.buy_now_clicked.connect(lambda product_id: print(f"Buy now: Product {product_id}"))
    widget.like_clicked.connect(lambda product_id: print(f"Like: Product {product_id}"))
    widget.card_clicked.connect(lambda product_id: print(f"Card clicked: Product {product_id}"))
    
    sys.exit(app.exec()) 