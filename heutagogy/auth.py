from heutagogy import app
from heutagogy.persistence import User
from flask_jwt import JWT
from werkzeug.security import safe_str_cmp


def get_user(username):
    return User.query.filter_by(username=username).first()


def authenticate(username, password):
    user = get_user(username)
    if user and user.check_password(password):
        return user


def identity(payload):
    return get_user(payload['identity'])


jwt = JWT(app, authenticate, identity)
