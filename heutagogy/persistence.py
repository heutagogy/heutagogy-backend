import sqlite3

def with_connection(f):
    conn = sqlite3.connect('heutagogy.sqlite3')
    result = f(conn)
    conn.commit()
    conn.close()
    return result

def initialize():
    def init_fn(conn):
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS bookmarks
            (timestamp text, url text, title text)''')
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
