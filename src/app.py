from flask import render_template, url_for, redirect

from src import create_app, login_manager


app = create_app('develop')


@app.route('/')
def index():
    return render_template("index.html")


@login_manager.user_loader
def load_user(user_id):
    if user_id is None:
        return redirect(url_for('auth.login'))
