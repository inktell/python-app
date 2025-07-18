import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect_db():
    conn = sqlite3.connect('data/database.db')
    conn.row_factory = dict_factory
    return conn

def create_user(name, email, password, gender="", avatar=""):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, email, password, gender, avatar)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, email, password, gender, avatar))
    conn.commit()
    conn.close()

def get_user_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, email, password, gender, avatar FROM users WHERE id = ?', (id,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_email(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, email, password, gender, avatar FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_name(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, email, password, gender, avatar FROM users WHERE name = ?', (name,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_email_and_password(email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, password, gender, avatar FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user

def update_avatar_user(id, avatar):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET avatar = ? WHERE id = ?", (avatar, id))
    conn.commit()
    conn.close()

def update_user(id, name, email, gender):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, email = ?, gender = ? WHERE id = ?", (name, email, gender, id))
    conn.commit()
    conn.close()

def remove_user(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update_password_user(id, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = ? WHERE id = ?", (password, id))
    conn.commit()
    conn.close()

# Product functions
def get_all_products():
    """Get all products from database"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product ORDER BY id DESC')
    products = cursor.fetchall()
    conn.close()
    return products

def get_products_by_category(category):
    """Get products filtered by category"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product WHERE category = ? ORDER BY id DESC', (category,))
    products = cursor.fetchall()
    conn.close()
    return products

def search_products_by_title(search_text):
    """Search products by title"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product WHERE title LIKE ? ORDER BY id DESC', (f'%{search_text}%',))
    products = cursor.fetchall()
    conn.close()
    return products

def get_product_by_id(product_id):
    """Get product by ID"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product

def get_products_sorted_by_price(ascending=True):
    """Get products sorted by price"""
    conn = connect_db()
    cursor = conn.cursor()
    if ascending:
        cursor.execute('SELECT * FROM product ORDER BY CAST(price AS REAL) ASC')
    else:
        cursor.execute('SELECT * FROM product ORDER BY CAST(price AS REAL) DESC')
    products = cursor.fetchall()
    conn.close()
    return products

def get_products_sorted_by_rating(ascending=True):
    """Get products sorted by rating"""
    conn = connect_db()
    cursor = conn.cursor()
    if ascending:
        cursor.execute('SELECT * FROM product ORDER BY CAST(rate AS REAL) ASC')
    else:
        cursor.execute('SELECT * FROM product ORDER BY CAST(rate AS REAL) DESC')
    products = cursor.fetchall()
    conn.close()
    return products

def get_products_sorted_by_sold(ascending=True):
    """Get products sorted by sold count"""
    conn = connect_db()
    cursor = conn.cursor()
    if ascending:
        cursor.execute('SELECT * FROM product ORDER BY CAST(sold AS REAL) ASC')
    else:
        cursor.execute('SELECT * FROM product ORDER BY CAST(sold AS REAL) DESC')
    products = cursor.fetchall()
    conn.close()
    return products

def get_categories():
    """Get all unique categories"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT category FROM product WHERE category IS NOT NULL AND category != "" ORDER BY category')
    categories = [row['category'] for row in cursor.fetchall()]
    conn.close()
    return categories

def create_cart_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            title TEXT,
            price REAL,
            img TEXT,
            quantity INTEGER DEFAULT 1
        )
    ''')
    conn.commit()
    conn.close()

def add_to_cart(user_id, product):
    conn = connect_db()
    cursor = conn.cursor()
    # Check if product already in cart for this user
    cursor.execute('SELECT id FROM cart WHERE user_id = ? AND product_id = ?', (user_id, product['id']))
    if cursor.fetchone() is None:
        cursor.execute('''
            INSERT INTO cart (user_id, product_id, title, price, img, quantity)
            VALUES (?, ?, ?, ?, ?, 1)
        ''', (user_id, product['id'], product['title'], product['price'], product['img']))
        conn.commit()
    conn.close()

def get_cart_by_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cart WHERE user_id = ?', (user_id,))
    cart = cursor.fetchall()
    conn.close()
    return cart

def remove_from_cart(user_id, product_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cart WHERE user_id = ? AND product_id = ?', (user_id, product_id))
    conn.commit()
    conn.close()