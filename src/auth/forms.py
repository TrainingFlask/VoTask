from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, BooleanField
from flask_wtf.html5 import EmailField


class LoginForm(FlaskForm):
    
    email = StringField(label='Email', validators=[validators.DataRequired()])
    password = PasswordField(label='Password', validators=[validators.DataRequired()])
    remember_me = BooleanField(label='Remember me', default=False)


class RegisterForm(FlaskForm):

    name = StringField(label='Name', validators=[validators.DataRequired()])
    family = StringField(label='Family', validators=[validators.DataRequired()])
    email = EmailField(label='Email', validators=[validators.DataRequired()])
    password = PasswordField(label='Password', validators=[validators.DataRequired()])
    confirm_password = PasswordField(label='Confirm password', validators=[validators.DataRequired()])
