from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, BooleanField
from flask_wtf.html5 import EmailField


class LoginForm(FlaskForm):
    
    email = EmailField(label='Email',
                       validators=[validators.DataRequired("Enter email address for this account"),
                                   validators.Email("Should be email address like: example@example.com")])

    password = PasswordField(label='Password', validators=[validators.DataRequired()])

    remember_me = BooleanField(label='Remember me', default=False)


class RegisterForm(FlaskForm):

    name = StringField(label='Name', validators=[validators.DataRequired("Enter your first name")])

    family = StringField(label='Family', validators=[validators.DataRequired("Enter your family name")])

    email = EmailField(label='Email',
                       validators=[validators.DataRequired("Enter your email address to sign up"),
                                   validators.Email("Should be email address like: example@example.com")])

    password = PasswordField(label='Password',
                             validators=[validators.DataRequired(),
                                         validators.Length(min=6,
                                                           max=20,
                                                           message='Should be more than 6 character')])

    confirm_password = PasswordField(label='Confirm password',
                                     validators=[validators.DataRequired(
                                         "Enter your password again to confirm that password")])
