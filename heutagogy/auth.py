from heutagogy import app
from flask import jsonify
import flask_login

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(flask_login.UserMixin):
    pass

@login_manager.unauthorized_handler
def unauthorized_handler():
    return jsonify(message='Unauthorized'), 401

@login_manager.request_loader
def request_loader(request):
    if not request.authorization:
        return None

    username = request.authorization.username
    password = request.authorization.password

    if username == app.config['BASIC_AUTH_USERNAME'] and \
       password == app.config['BASIC_AUTH_PASSWORD']:
        user = User()
        user.id = username
        return user

    return None
