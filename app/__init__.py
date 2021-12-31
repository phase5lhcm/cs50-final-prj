from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///showroom.db'
app.config['SECRET_KEY'] = 'e92f34a96126929f18aff113'
db = SQLAlchemy(app)

from app import routes
   
