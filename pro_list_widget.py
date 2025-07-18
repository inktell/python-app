import sys
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, 
                             QScrollArea, QFrame, QApplication)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
from product_item_widget import ProductCard
import database


class ProductListWidget(QWidget):
    """
    Scrollable widget that displays a grid of product cards
    """
    
    # Signals for product interactions
    product_clicked = pyqtSignal(int)      # product_id
    product_liked = pyqtSignal(int)        # product_id
    product_buy_now = pyqtSignal(int)      # product_id
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.products = []
        self.product_cards = []
        self.setup_ui()
        self.load_products()
    
    def setup_ui(self):
        """Setup the UI with scrollable grid layout"""
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        
        # Create container widget for grid
        self.container_widget = QWidget()
        self.container_widget.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
            }
        """)
        
        # Create grid layout for products
        self.grid_layout = QGridLayout(self.container_widget)
        self.grid_layout.setSpacing(15)  # Space between cards
        self.grid_layout.setContentsMargins(15, 15, 15, 15)
        
        # Set scroll area widget
        self.scroll_area.setWidget(self.container_widget)
        main_layout.addWidget(self.scroll_area)
    
    def load_products(self):
        """Load products from database and create cards"""
        # Get all products from database
        self.products = database.get_all_products()
        
        # Create product cards
        self.create_product_cards()
    
    def create_product_cards(self):
        """Create ProductCard widgets and arrange them in grid"""
        # Clear existing cards
        for card in self.product_cards:
            card.deleteLater()
        self.product_cards.clear()
        
        # Calculate grid dimensions
        card_width = 220  # Width of each ProductCard
        card_height = 320  # Height of each ProductCard
        spacing = 15  # Space between cards
        margin = 15  # Margin around the grid
        
        # Calculate how many cards fit in a row
        available_width = 931 - (2 * margin)  # 931 is the widget width
        cards_per_row = max(1, (available_width + spacing) // (card_width + spacing))
        
        # Create and position cards
        for i, product in enumerate(self.products):
            # Create product card
            card = ProductCard(product, self)
            
            # Connect signals
            card.card_clicked.connect(lambda product_id: self.product_clicked.emit(product_id))
            card.like_clicked.connect(lambda product_id: self.product_liked.emit(product_id))
            card.buy_now_clicked.connect(lambda product_id: self.product_buy_now.emit(product_id))
            
            # Calculate grid position
            row = i // cards_per_row
            col = i % cards_per_row
            
            # Add to grid layout
            self.grid_layout.addWidget(card, row, col)
            
            # Store reference
            self.product_cards.append(card)
    
    def refresh_products(self):
        """Refresh the product list"""
        self.load_products()
    
    def filter_products_by_category(self, category):
        """Filter products by category"""
        if category.lower() == "tất cả":
            self.load_products()
            return
        
        # Get filtered products from database
        self.products = database.get_products_by_category(category)
        
        # Recreate cards
        self.create_product_cards()
    
    def search_products(self, search_text):
        """Search products by title"""
        if not search_text.strip():
            self.load_products()
            return
        
        # Get searched products from database
        self.products = database.search_products_by_title(search_text)
        
        # Recreate cards
        self.create_product_cards()
    
    def sort_products_by_price(self, ascending=True):
        """Sort products by price"""
        self.products = database.get_products_sorted_by_price(ascending)
        # Recreate cards
        self.create_product_cards()
    
    def sort_products_by_rating(self, ascending=True):
        """Sort products by rating"""
        self.products = database.get_products_sorted_by_rating(ascending)
        # Recreate cards
        self.create_product_cards()
    
    def sort_products_by_sold(self, ascending=True):
        """Sort products by sold count"""
        self.products = database.get_products_sorted_by_sold(ascending)
        # Recreate cards
        self.create_product_cards()


# Example usage and testing
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create and show the widget
    widget = ProductListWidget()
    widget.resize(931, 400)
    widget.show()
    
    # Connect signals for testing
    widget.product_clicked.connect(lambda product_id: print(f"Product clicked: {product_id}"))
    widget.product_liked.connect(lambda product_id: print(f"Product liked: {product_id}"))
    widget.product_buy_now.connect(lambda product_id: print(f"Buy now: {product_id}"))
    
    sys.exit(app.exec()) 