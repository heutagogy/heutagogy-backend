from heutagogy import app
from flask_jwt import JWT
from werkzeug.security import safe_str_cmp


class User(object):
    def __init__(self, id, username, password):
        self.id = id
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


def get_users():
    users = []
    for i, x in enumerate(app.config['USERS']):
        users.append(User(i+1, x['username'], x['password']))
    return users


def authenticate(username, password):
    users = get_users()
    username_table = {u.username: u for u in users}
    user = username_table.get(username, None)
    if user and safe_str_cmp(
        user.password.encode('utf-8'),
        password.encode('utf-8')
    ):
        return user


def identity(payload):
    users = get_users()
    userid_table = {u.id: u for u in users}
    user_id = payload['identity']
    return userid_table.get(user_id, None)


jwt = JWT(app, authenticate, identity)
