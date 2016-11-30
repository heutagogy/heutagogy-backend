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

def save_bookmark(bookmark):
    def save_fn(conn):
        c = conn.cursor()
        c.execute('''
            INSERT INTO bookmarks(timestamp, url, title)
            VALUES (?, ?, ?)
            ''',
            (bookmark['timestamp'], bookmark['url'], bookmark['title']))
        return dict(bookmark, id=c.lastrowid)
    return with_connection(save_fn)

def get_bookmarks():
    def row_to_bookmark(r):
        return {
            'id': r[0],
            'timestamp': r[1],
            'url': r[2],
            'title': r[3],
        }

    def get_fn(conn):
        c = conn.cursor()
        c.execute('SELECT rowid, timestamp, url, title FROM bookmarks')
        return list(map(row_to_bookmark, c.fetchall()))

    return with_connection(get_fn)
