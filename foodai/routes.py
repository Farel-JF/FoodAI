from flask import render_template, url_for, flash, redirect, request, session
from flask_login import login_user, logout_user, current_user, login_required
from foodai import app, bcrypt, db, login_manager
from foodai.models import User
from foodai.form import RegistrationForm, LoginForm
from foodai.models import Products

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
    # Logic to fetch and display all products
    return render_template('products.html', title="Products")

@app.route('/product/<int:product_id>')
def product(product_id):
    # Fetch the product from the database
    product_details = Products.query.get(product_id)

    # Check if the product exists
    if product_details is None:
        flash("Product not found.", "danger")
        return redirect(url_for('home'))  # Redirect to home if not found

    return render_template('product.html', product=product_details)



def get_product_by_id(product_id):
    return Product.query.get(product_id)  # Assuming Product is your model


@app.route('/healthy_meals')
def healthy_meals():
    return render_template('healthy_meals.html')

@app.route('/energy_drinks')
def energy_drinks():
    return render_template('energy_drinks.html')

@app.route('/ai_helper')
def ai_helper():
    return render_template('ai_helper.html')

app.secret_key = 'Farel275&'  # Remplacez par une clé secrète réelle

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    cart = session.get('cart', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart)
    total_price_formatted = "{:.2f}".format(total_price)

    if request.method == 'POST':
        # Handle payment processing logic here
        session.pop('cart', None)  # Clear the cart after payment
        flash("Payment successful!", "success")
        return redirect(url_for('home'))

    return render_template('payment.html', total_price=total_price_formatted)

@app.route('/cart', methods=['GET'])
def cart():
    cart = session.get('cart', [])
    return render_template('cart.html', cart=cart)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Logic to add the product to the cart
    product = Products.query.get(product_id)
    if product:
        # Assuming you have logic to initialize the cart
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
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check credentials", "danger")

    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
