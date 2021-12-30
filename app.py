from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///showroom.db'
#database setup
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False,unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False,unique=True)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)
    
    def __repr__(self):
        return f'Product {self.name}'
   

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("Homepage.html")

@app.route('/showroom')
def showroom():
    #let's return all Products in db
    items = Product.query.all()
    return render_template('showroom.html', items=items)
    

