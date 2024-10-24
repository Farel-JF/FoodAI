from foodai.models import User
from flask import render_template, url_for, flash, redirect, request
from foodai.form import RegistrationForm, LoginForm
from foodai import app, bcrypt, db, login_manager
from flask_login import (
    login_required,
    login_user,
    current_user,
    logout_user,
    login_required,
)



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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Define your routes...
@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
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

def load_user(user_id):
    return User.query.get(int(user_id))

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




















