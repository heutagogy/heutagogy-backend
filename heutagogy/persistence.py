from heutagogy import app
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy(app)


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
