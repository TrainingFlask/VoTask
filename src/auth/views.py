from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user

from . import bp_auth
from src.auth.forms import LoginForm, RegisterForm


@bp_auth.route('/sign_in', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        flash("You sign in to your account")
    return render_template("auth/login.html", form=form)


@bp_auth.route('/sign_up', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        flash("You sign up with {} email".format(form.email.data))
    return render_template("auth/register.html", form=form)
