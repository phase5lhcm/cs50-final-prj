from app import db, login_manager
from app import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), nullable=False,unique=True)
    email = db.Column(db.String(),nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000) 
    products = db.relationship('Product', backref='owner',lazy=True)
    
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password): 
         bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def verify_password(self, check_pwrd):
        #check_password_hash returns a bool
        return bcrypt.check_password_hash(self.password, check_pwrd)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False,unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False,unique=True)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)
    owner_id = db.Column(db.String(), db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f'Product {self.name}'
    