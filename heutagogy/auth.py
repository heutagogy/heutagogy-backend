from heutagogy import app
from flask_jwt import JWT
from werkzeug.security import safe_str_cmp


class User(object):
    def __init__(self, username, password):
        self.id = username
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

    def __getitem__(self, key):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }.get(key, None)


def get_user(username):
    record = app.config['USERS'].get(username, None)
    if record:
        return User(username, record['password'])
    else:
        return None


def authenticate(username, password):
    user = get_user(username)
    if user and safe_str_cmp(
            user.password.encode('utf-8'),
            password.encode('utf-8')):
        return user


def identity(payload):
    return get_user(payload['identity'])


jwt = JWT(app, authenticate, identity)
