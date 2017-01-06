from heutagogy import app
import os
from datetime import timedelta

app.config.from_object(__name__)
app.config.update(dict(
    USERS={
        'myuser': {'password': 'mypassword'},
        'user2': {'password': 'pass2'},
    },
    JWT_AUTH_URL_RULE='/api/v1/login',
    JWT_EXPIRATION_DELTA=timedelta(seconds=2592000),  # 1 month
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.root_path,
                                                        'heutagogy.sqlite3'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    DEBUG=True))
app.config.from_envvar('HEUTAGOGY_SETTINGS', silent=True)

if not app.config['SECRET_KEY']:
    app.config['SECRET_KEY'] = 'super-secret'
