from heutagogy import app
from heutagogy.persistence import User
from flask_jwt import JWT, jwt_required, current_identity
import flask_login


def get_user(username):
    return User.query.filter_by(username=username).first()


def authenticate(username, password):
    user = get_user(username)
    if user and user.check_password(password):
        return user


def identity(payload):
    user = get_user(payload['identity'])
    if user:
        # this field is needed for Flask-Login
        user.is_authenticated = True
    return user


jwt = JWT(app, authenticate, identity)


login_manager = flask_login.LoginManager(app)


@login_manager.request_loader
@jwt_required()
def load_user_from_request(request):
    return current_identity
