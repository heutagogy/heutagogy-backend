from heutagogy import app
import heutagogy.persistence
import os

app.config.from_object(__name__)
app.config.update(dict(
    USERS={
        'myuser': {'password': 'mypassword'},
        'user2': {'password': 'pass2'},
    },
    DATABASE=os.path.join(app.root_path, 'heutagogy.sqlite3'),
    DEBUG=True))
app.config.from_envvar('HEUTAGOGY_SETTINGS', silent=True)


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    heutagogy.persistence.initialize()
