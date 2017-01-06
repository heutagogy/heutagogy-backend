from heutagogy import app
from heutagogy.persistence import User
from flask_jwt import JWT
from werkzeug.security import safe_str_cmp


def get_user(username):
    return User.query.filter_by(username=username).first()


def authenticate(username, password):
    user = get_user(username)
    if user and safe_str_cmp(
            user.password.encode('utf-8'),
            password.encode('utf-8')):
        return user


def identity(payload):
    return get_user(payload['identity'])


jwt = JWT(app, authenticate, identity)
