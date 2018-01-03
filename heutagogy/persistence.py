from heutagogy import db
from heutagogy.auth import User
import datetime
import pytz

import sqlalchemy.dialects.postgresql as postgresql


# The database doesn't store timezones, so we convert all timestamps
# to UTC to not save incorrect info.
def to_utc(t):
    """Convert datetime to UTC."""
    if t is None:
        return t

    if t.tzinfo is None or t.tzinfo.utcoffset(t) is None:
        # t is naive datetime (not aware of timezone)
        return t

    return t.astimezone(pytz.utc).replace(tzinfo=None)


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    notes = db.Column(db.String, nullable=True)
    read = db.Column(db.DateTime)
    tags = db.Column(postgresql.ARRAY(db.Text))
    content_html = db.deferred(db.Column(db.Text, nullable=True))
    content_text = db.deferred(db.Column(db.Text, nullable=True))

    def __init__(
            self, user, url,
            title=None, timestamp=None, read=None,
            tags=None, notes=None):

        if timestamp is None:
            timestamp = datetime.datetime.utcnow()
        if title is None:
            title = url

        self.user = user
        self.url = url
        self.title = title
        self.timestamp = to_utc(timestamp)
        self.read = to_utc(read)
        self.tags = tags if tags else []
        self.notes = notes if notes else ''

    def __repr__(self):
        return '<Bookmark %r of %r>' % self.url % self.user

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'title': self.title,
            'timestamp': self.timestamp.isoformat(),
            'read': self.read.isoformat() if self.read else None,
            'tags': self.tags,
            'notes': self.notes
        }
