from app import app
from flask import render_template
from app.models import Product

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("Homepage.html")

@app.route('/showroom')
def showroom():
    #let's return all Products in db9
    items = Product.query.all()
    return render_template('showroom.html', items=items)