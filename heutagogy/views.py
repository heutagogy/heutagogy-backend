from heutagogy import app
import heutagogy.persistence

from flask import request, jsonify, Response
import json
import datetime
import sqlite3

heutagogy.persistence.initialize()

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/api/v1/bookmarks', methods=['POST'])
def bookmarks_post():
    r = request.get_json()

    bookmark = dict()
    try:
        bookmark['url'] = r['url']
        bookmark['title'] = r['title']
    except:
        return jsonify(message='Request error'), 400

    if 'timestamp' in r:
        bookmark['timestamp'] = r['timestamp']
    else:
        bookmark['timestamp'] = datetime.datetime.utcnow().isoformat(' ')

    result = heutagogy.persistence.save_bookmark(bookmark)
    return jsonify(**result), 201

@app.route('/api/v1/bookmarks', methods=['GET'])
def bookmarks_get():
    result = heutagogy.persistence.get_bookmarks()
    return Response(json.dumps(result), mimetype='application/json')
