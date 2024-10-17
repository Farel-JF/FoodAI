from flask import Flask, request, jsonify
from models import db, User, Product, Order, Review

app = Flask(__name__)

# Routes for Users
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(Name=data['name'], Email=data['email'], Password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    output = [{'User_id': user.User_id, 'Name': user.Name, 'Email': user.Email} for user in users]
    return jsonify(output), 200

# Routes for Products
@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(Name=data['name'], Description=data['description'], Price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    output = [{'Product_id': product.Product_id, 'Name': product.Name, 'Description': product.Description, 'Price': product.Price} for product in products]
    return jsonify(output), 200

# Routes for Orders
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    new_order = Order(User_id=data['user_id'], Status=data.get('status', 'Pending'), Total_amount=data['total_amount'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order placed successfully'}), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    output = [{'Order_id': order.Order_id, 'User_id': order.User_id, 'Status': order.Status, 'Total_amount': order.Total_amount, 'Order_date': order.Order_date} for order in orders]
    return jsonify(output), 200

# Routes for Reviews
@app.route('/reviews', methods=['POST'])
def create_review():
    data = request.json
    new_review = Review(User_id=data['user_id'], Product_id=data['product_id'], Rating=data['rating'], Comment=data['comment'])
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review submitted successfully'}), 201

@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    output = [{'Reviews_id': review.Reviews_id, 'User_id': review.User_id, 'Product_id': review.Product_id, 'Rating': review.Rating, 'Comment': review.Comment, 'Review_date': review.Review_date} for review in reviews]
    return jsonify(output), 200
