from flask import render_template, url_for, flash, redirect, request, session
from flask_login import login_user, logout_user, current_user
from foodai.models import User, Products
from foodai.forms import RegistrationForm, LoginForm
from foodai import app, bcrypt, db, login_manager

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/protein')
def protein():
    return render_template('protein.html')

@app.route('/products')  # Endpoint for listing all products
def products():
    return render_template('products.html', title="Products")

@app.route('/product/<int:product_id>')
def product(product_id):
    product = Products.query.get(product_id)  # Fetch the product from the database
    if product is None:
        flash('Product not found!', 'danger')
        return redirect(url_for('home'))  # Redirect to home if product doesn't exist
    return render_template('product.html', product=product)

def calculate_total_price(cart_items):
    total_price = 0
    for item in cart_items:
        total_price += float(item['price']) * item['quantity']
    return total_price

@app.route('/healthy_meals')
def healthy_meals():
    return render_template('healthy_meals.html')

@app.route('/energy_drinks')
def energy_drinks():
    return render_template('energy_drinks.html')

@app.route('/ai_helper')
def ai_helper():
    return render_template('ai_helper.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if current_user.is_authenticated:
        cart_items = session.get('cart', [])
        total_price = calculate_total_price(cart_items)
        total_price_formatted = f"{total_price:.2f}"
        # Payment processing logic...
        return render_template('payment.html', total_price=total_price_formatted)
    else:
        flash("Please log in to proceed with payment.", "warning")
        return redirect(url_for('login'))  # Redirect to the login page

@app.route('/cart', methods=['GET'])
def cart():
    cart = session.get('cart', [])
    return render_template('cart.html', cart=cart)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = Products.query.get(product_id)
    if product:
        item = {
            'product_id': product.product_id,
            'product_name': product.name,
            'price': str(product.price),  # Store as string for session
            'quantity': 1  # Default to 1 for simplicity
        }
        # Initialize cart if it doesn't exist
        if 'cart' not in session:
            session['cart'] = []
        # Append product to cart
        session['cart'].append(item)
        session.modified = True
        flash(f"{product.name} has been added to your cart!", "success")
        return redirect(url_for('product', product_id=product.product_id))

    flash("Product not found.", "danger")
    return redirect(url_for('home'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created successfully for {form.name.data}", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))  # Redirect if already logged in

    form = LoginForm()  # Initialize the form

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')  # Get the next page to redirect to
            flash("You have been logged in!", "success")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check credentials", "danger")

    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
