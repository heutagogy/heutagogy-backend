from heutagogy import app
from flask import g
import sqlite3


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def get_db():
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()


def with_connection(f):
    conn = get_db()
    result = f(conn)
    conn.commit()
    return result


def initialize():
    def init_fn(db):
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
    with_connection(init_fn)


def save_bookmark(user_id, bookmark):
    def save_fn(conn):
        c = conn.cursor()
        c.execute('''
                  INSERT INTO bookmarks(user, timestamp, url, title, read)
                  VALUES (?, ?, ?, ?, ?)
                  ''',
                  (user_id,
                   bookmark['timestamp'],
                   bookmark['url'],
                   bookmark['title'],
                   bookmark['read']))
        return dict(bookmark, id=c.lastrowid)
    return with_connection(save_fn)


def row_to_bookmark(r):
    return {
        'id': r[0],
        'timestamp': r[1],
        'url': r[2],
        'title': r[3],
        'read': r[4],
    }


def get_bookmarks(user_id):
    def get_fn(conn):
        c = conn.cursor()
        c.execute(
            '''
            SELECT rowid, timestamp, url, title, read
            FROM bookmarks
            WHERE user = ?
            ''',
            (user_id,))
        return list(map(row_to_bookmark, c.fetchall()))
    return with_connection(get_fn)


def get_bookmark(user_id, bookmark_id):
    def get_fn(conn):
        c = conn.cursor()
        c.execute(
            '''
            SELECT rowid, timestamp, url, title, read
            FROM bookmarks
            WHERE rowid = ? AND user = ?
            ''',
            (bookmark_id, user_id))
        result = list(map(row_to_bookmark, c.fetchall()))
        if len(result) == 0:
            return None
        else:
            return result[0]
    return with_connection(get_fn)


def set_read(bookmark_id, read):
    def set_fn(conn):
        c = conn.cursor()
        c.execute(
            '''
            UPDATE bookmarks
            SET read = ?
            WHERE rowid = ?
            ''',
            (read, bookmark_id))
        return {'read': read}

    return with_connection(set_fn)
