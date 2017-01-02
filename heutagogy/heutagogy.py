from heutagogy import app
import heutagogy.persistence
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
    DATABASE=os.path.join(app.root_path, 'heutagogy.sqlite3'),
    DEBUG=True))
app.config.from_envvar('HEUTAGOGY_SETTINGS', silent=True)

if not app.config['SECRET_KEY']:
    app.config['SECRET_KEY'] = 'super-secret'


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    heutagogy.persistence.initialize()


with app.app_context():
    if not os.path.isfile(app.config['DATABASE']):
        heutagogy.persistence.initialize()
