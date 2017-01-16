"""We have two authentication methods in use now.

First one is JWT tokens and is main authentication method used by all
API methods.

Second method is session-based and is used by local user-management
interface. (The pages for user registration, log-in, change username
and password.)

This module provides integration of Flask-JWT and Flask-User.
"""
from heutagogy import app
from heutagogy.persistence import db
from flask_jwt import JWT, JWTError, jwt_required, current_identity
import flask_login
import flask_user


class User(db.Model, flask_user.UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    email = db.Column(db.String(255), unique=True)
    confirmed_at = db.Column(db.DateTime())

    active = db.Column('is_active', db.Boolean(), nullable=False,
                       server_default='0')
    first_name = db.Column(db.String(255), nullable=False, server_default='')
    last_name = db.Column(db.String(255), nullable=False, server_default='')

    def set_password(self, password):
        self.password = user_manager.hash_password(password)


def get_user(user_id):
    return user_manager.get_user_by_id(user_id)


def authenticate(username, password):
    user = user_manager.find_user_by_username(username)
    if user and user_manager.verify_password(password, user):
        return user


def identity(payload):
    user = get_user(payload['identity'])
    return user


jwt = JWT(app, authenticate, identity)
login_manager = flask_login.LoginManager()
db_adapter = flask_user.SQLAlchemyAdapter(db, User)
user_manager = flask_user.UserManager(db_adapter, app,
                                      login_manager=login_manager)


@login_manager.request_loader
def load_user_from_request(request):
    """This function is called by login manager to get user info from
    the request (JWT authorization) when there is no info in the
    session.

    The trick here is that we don't want it to error when there is no
    JWT token, as otherwise the user can never access registration
    page.
    """
    @jwt_required()
    def get_user():
        return current_identity

    try:
        return get_user()
    except JWTError as e:
        # Don't error when no JWT token is provided
        if e.error == 'Authorization Required':
            return login_manager.anonymous_user()
        else:
            raise


def token_required(f):
    """We define our own wrapper for the function, that do require JWT
    token. We don't want to use default @login_required provided by
    Flask-User as it redirects to login page. We don't want this to
    happen for our API methods and want to return proper 401
    Unauthorized response.
    """
    def wrapper(*args, **kwargs):
        if not flask_user.access.is_authenticated():
            raise JWTError(
                'Authorization Required',
                'Request does not contain an access token',
                headers={
                    'WWW-Authenticate':
                    'JWT realm="%s"' % app.config['JWT_DEFAULT_REALM']
                })
        return f(*args, **kwargs)
    return wrapper
