from flask import render_template, url_for, flash, redirect, request
from flask_login import (
    login_user,
    logout_user,
    current_user,
    login_required,
)
from foodai import app, bcrypt, db, login_manager
from foodai.models import User
from foodai.form import RegistrationForm, LoginForm

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

@app.route('/healthy_meals')
def healthy_meals():
    return render_template('healthy_meals.html')

@app.route('/energy_drinks')
def energy_drinks():
    return render_template('energy_drinks.html')

@app.route('/ai_helper')
def ai_helper():
    return render_template('ai_helper.html')

app.secret_key = 'votre_cle_secrete'  # Remplacez par une clé secrète réelle

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    # Obtenez le panier de la session
    cart = session.get('cart', [])

    # Calculez le prix total
    total_price = sum(item['price'] * item['quantity'] for item in cart)

    # Formatage du prix total en tant que chaîne avec deux décimales
    total_price_formatted = "{:.2f}".format(total_price)

    if request.method == 'POST':
        # Gérer la logique de paiement ici
        pass  # Remplacez par votre logique de traitement de paiement

    # Rendre la page de paiement avec le prix total
    return render_template('payment.html', total_price=total_price_formatted)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item = {
        'product': request.form['product'],
        'price': float(request.form['price']),
        'quantity': int(request.form['quantity'])
    }

    # Initialisez le panier si ce n'est pas encore fait
    if 'cart' not in session:
        session['cart'] = []

    # Ajoutez l'item au panier
    session['cart'].append(item)
    session.modified = True  # Indiquez que la session a été modifiée

    return redirect(url_for('home'))  # Redirigez vers la page d'accueil ou une autre page

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = RegistrationForm()  # Initialize the form
    if form.validate_on_submit():
        # Hash the password within the context of the route
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(
            name=form.name.data,
            email=form.email.data,
            password=hashed_password,
        )
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
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check credentials", "danger")

    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
