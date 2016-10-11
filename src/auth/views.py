from flask import render_template, redirect, url_for
from flask_login import login_user

from . import bp_auth
from src.auth.forms import LoginForm


@bp_auth.route('/sign_in', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("auth/login.html", form=form)


@bp_auth.route('/sign_up')
def register():
    return render_template("auth/register.html")
