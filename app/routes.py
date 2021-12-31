from app import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from app.models import Product, User
from app.forms import LoginForm, RegisterForm
from app import db

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
                           password=form.password1.data)
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
    return render_template('loginPage.html', form=form)