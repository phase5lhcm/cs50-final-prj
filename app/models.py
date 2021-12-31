from enum import unique
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), nullable=False,unique=True)
    email = db.Column(db.String(),nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000) 
    products = db.relationship('Product', backref='owner',lazy=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False,unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False,unique=True)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)
    owner_id = db.Column(db.String(), db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f'Product {self.name}'
    