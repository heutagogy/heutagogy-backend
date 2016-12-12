from heutagogy import app
from flask import jsonify
import flask_login

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(flask_login.UserMixin):
    pass

@login_manager.unauthorized_handler
def unauthorized_handler():
    return jsonify(error='Unauthorized'), 401

@login_manager.request_loader
def request_loader(request):
    if not request.authorization:
        return None

    users = app.config['USERS']
    username = request.authorization.username
    password = request.authorization.password

    if username in users and password == users[username]['password']:
        user = User()
        user.id = username
        return user

    return None
