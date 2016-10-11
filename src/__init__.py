from flask import Flask
from flask_login import LoginManager

from config import config
from src.auth import bp_auth


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    app.register_blueprint(bp_auth, url_prefix='/auth')

    login_manager.init_app(app)

    return app
