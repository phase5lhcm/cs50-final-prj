from app import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from app.models import Product, User
from app.forms import LoginForm, RegisterForm
from app import db
from flask_login import login_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("Homepage.html")

@app.route('/showroom')
@login_required
def showroom():
    #let's return all Products in db
    products = Product.query.all()
   # print('products', products)
    return render_template('showroom.html', products=products)

@app.route("/register", methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user = User(username=form.username.data, 
                           email=form.email.data, 
                           password=form.password1.data)
        db.session.add(create_user)
        db.session.commit()
        print(create_user)
        # login_user(user_login)
        # flash(f"Welcome! You are now logged in as {user_login.username}", category="success")
        # print('create_user', create_user)
        return redirect(url_for('showroom'))
    #Let's check if there are form errors per the validators
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Error creating user: {err_msg}', category='danger')
    return render_template('registerPage.html', form=form)
    
@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user_login = User.query.filter_by(username=form.email.data).first()
        # print(f"user: {user_login}")
        if user_login and user_login.verify_password(check_pwrd=form.password.data
        ):
            login_user(user_login)
            flash(f"{user_login}, you have successfully logged in.")
            return redirect(url_for('showroom'))
        else:
            flash('Incorrect email and password combination. Please try again, or register for an account', category="danger")
    return render_template('loginPage.html', form=form)
    
@app.route("/logout", methods=['POST'])
def logout_page():
    logout_user()
    flash("Logout successful", category="info")
    return redirect(url_for("home_page"))