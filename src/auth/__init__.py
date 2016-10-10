from flask import Blueprint


bp_auth = Blueprint('auths', __name__)

from . import views
