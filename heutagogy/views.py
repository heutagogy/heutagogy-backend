from heutagogy import app
from flask import request, jsonify
import sqlite3
import datetime

conn = sqlite3.connect('heutagogy.sqlite3')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS bookmarks
             (date text, url text, title text)''')
conn.commit()

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/api/v1/bookmarks', methods=['POST'])
def bookmark_post():
    r = request.get_json()

    try:
        url = r['url']
        title = r['title']
    except:
        return jsonify(message='Request error'), 400

    if 'timestamp' in r:
        timestamp = r['timestamp']
    else:
        timestamp = datetime.datetime.utcnow().isoformat(' ')

    conn = sqlite3.connect('heutagogy.sqlite3')
    c = conn.cursor()
    c.execute('INSERT INTO bookmarks VALUES (?, ?, ?)', (timestamp, url, title))
    bookmark_id = c.lastrowid
    conn.commit()

    bookmark = {
        'id': bookmark_id,
        'url': url,
        'title': title,
        'timestamp': timestamp,
    }

    return jsonify(**bookmark), 201
