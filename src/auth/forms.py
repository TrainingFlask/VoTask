from flask_wtf import Form
from wtforms import StringField, validators, PasswordField


class LoginForm(Form):
    
    email = StringField(label='Email', validator=[validators.DataRequired()])
    password = PasswordField(label='Password', validator=[validators.DataRequired()])
