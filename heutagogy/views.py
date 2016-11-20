from heutagogy import app
from flask import request, jsonify, Response
import json
import datetime
import sqlite3

conn = sqlite3.connect('heutagogy.sqlite3')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS bookmarks
             (timestamp text, url text, title text)''')
conn.commit()

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/api/v1/bookmarks', methods=['POST'])
def bookmarks_post():
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

@app.route('/api/v1/bookmarks', methods=['GET'])
def bookmarks_get():
    conn = sqlite3.connect('heutagogy.sqlite3')
    c = conn.cursor()
    c.execute('SELECT rowid, timestamp, url, title FROM bookmarks')

    def row_to_bookmark(r):
        return {
            'id': r[0],
            'timestamp': r[1],
            'url': r[2],
            'title': r[3],
        }

    result = list(map(row_to_bookmark, c.fetchall()))

    return Response(json.dumps(result), mimetype='application/json')
