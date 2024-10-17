from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    User_id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(45))
    Email = db.Column(db.String(45), unique=True, nullable=False)
    Password = db.Column(db.String(45), nullable=False)
    Goal = db.Column(db.Text)
    Diet_preference = db.Column(db.Integer)
    Created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Product(db.Model):
    __tablename__ = 'products'
    Product_id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(45), nullable=False)
    Description = db.Column(db.String(200))
    Price = db.Column(db.Float, nullable=False)

class Order(db.Model):
    __tablename__ = 'orders'
    Order_id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('users.User_id'), nullable=False)
    Status = db.Column(db.String(45), default='Pending')
    Total_amount = db.Column(db.Float)
    Order_date = db.Column(db.DateTime, default=datetime.utcnow)

class Review(db.Model):
    __tablename__ = 'reviews'
    Reviews_id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('users.User_id'), nullable=False)
    Product_id = db.Column(db.Integer, db.ForeignKey('products.Product_id'), nullable=False)
    Rating = db.Column(db.Integer)
    Comment = db.Column(db.String(500))
    Review_date = db.Column(db.DateTime, default=datetime.utcnow)
