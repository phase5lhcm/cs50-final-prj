from app import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from app.models import Product, User
from app.forms import LoginForm, RegisterForm
from app import db
from flask_login import login_user

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("Homepage.html")

@app.route('/showroom')
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
                           password_hash=form.password1.data)
        db.session.add(create_user)
        db.session.commit()
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
        user_login = User.query.filter_by(email=form.email.data).first()
        if user_login and user_login.verify_password(check_pwrd=form.password.data):
            login_user(user_login)
            flash(f"{user_login}, you have successfully logged in.")
            return redirect(url_for("showroom"))
        else:
            flash('Incorrect email and password combination. Please try again, or register for an account', category="danger")
    return render_template('loginPage.html', form=form)