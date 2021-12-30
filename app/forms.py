from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='Username')
    email = StringField(label='Email')
    password1 = PasswordField(label='Password')
    password_confirmation = PasswordField(label='Confirm password')
    submitBtn = SubmitField(label='Create Account')