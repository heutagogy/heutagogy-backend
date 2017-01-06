from heutagogy import app
from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, username, email, password):
        self.id = username
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return "User(%s)" % self.username

    def __getitem__(self, key):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }.get(key, None)


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    url = db.Column(db.String)
    title = db.Column(db.String)
    read = db.Column(db.Boolean)

    def __init__(self, user, url, title=None, timestamp=None, read=False):
        if timestamp is None:
            timestamp = datetime.datetime.utcnow()
        if title is None:
            title = url

        self.user = user
        self.url = url
        self.title = title
        self.timestamp = timestamp
        self.read = read

    def __repr__(self):
        return '<Bookmark %r of %r>' % self.url % self.user

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'title': self.title,
            'timestamp': self.timestamp.isoformat(),
            'read': self.read,
        }


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    db.create_all()
