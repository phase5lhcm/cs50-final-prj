from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[Length(min=2, max=20), DataRequired()])
    email = StringField(label='Email', validators=[Email(message="A legit email is required"), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password_confirmation = PasswordField(label='Confirm password', validators=[EqualTo('password1'), DataRequired()])
    submitBtn = SubmitField(label='Create Account')