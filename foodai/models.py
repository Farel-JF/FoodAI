from flask_login import UserMixin
from datetime import datetime
from foodai import db  # Import db from __init__.py
from sqlalchemy import CheckConstraint  # Import CheckConstraint
from werkzeug.security import generate_password_hash, check_password_hash

# Define your models...
class User(db.Model, UserMixin):
    __tablename__ = 'Users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    goal = db.Column(db.String(255))
    diet_preference = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    orders = db.relationship("Orders", back_populates="user")
    recommendations = db.relationship("Recommendations", back_populates="user")
    reviews = db.relationship("Reviews", back_populates="user")

    def __repr__(self):
        return f"User('{self.user_id}', '{self.name}', '{self.email}')"



# Rest of the models...



class Categories(db.Model):
    __tablename__ = 'Categories'

    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    products = db.relationship("Products", back_populates="category")


class Products(db.Model):
    __tablename__ = 'Products'

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('Categories.category_id'))
    stock_quantity = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255))

    category = db.relationship("Categories", back_populates="products")
    order_items = db.relationship("Order_Items", back_populates="product")
    recommendations = db.relationship("Recommendations", back_populates="product")
    reviews = db.relationship("Reviews", back_populates="product")


class Diet_Preferences(db.Model):
    __tablename__ = 'Diet_Preferences'

    preference_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)


class Orders(db.Model):
    __tablename__ = 'Orders'

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(50))

    user = db.relationship("User", back_populates="orders")
    order_items = db.relationship("Order_Items", back_populates="order")


class Order_Items(db.Model):
    __tablename__ = 'Order_Items'

    order_item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('Orders.order_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('Products.product_id'))
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)

    order = db.relationship("Orders", back_populates="order_items")
    product = db.relationship("Products", back_populates="order_items")


class Recommendations(db.Model):
    __tablename__ = 'Recommendations'

    recommendation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('Products.product_id'))
    reason = db.Column(db.Text)

    user = db.relationship("User", back_populates="recommendations")
    product = db.relationship("Products", back_populates="recommendations")


class Reviews(db.Model):
    __tablename__ = 'Reviews'

    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('Products.product_id'), nullable=False)
    rating = db.Column(db.Integer, CheckConstraint('rating BETWEEN 1 AND 5'), nullable=False)
    comment = db.Column(db.Text)
    review_date = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="reviews")
    product = db.relationship("Products", back_populates="reviews")
