from heutagogy import app
import heutagogy.persistence

from flask import request, jsonify, Response
import json
import datetime
import sqlite3

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/api/v1/bookmarks', methods=['POST'])
def bookmarks_post():
    r = request.get_json()

    bookmark = dict()
    try:
        bookmark['url'] = r['url']
    except:
        return jsonify(message='url field is mandatory'), 400

    bookmark['title'] = r['title'] if 'title' in r else bookmark['url']
    bookmark['timestamp'] = r['timestamp'] if 'timestamp' in r else datetime.datetime.utcnow().isoformat(' ')

    result = heutagogy.persistence.save_bookmark(bookmark)
    return jsonify(**result), 201

@app.route('/api/v1/bookmarks', methods=['GET'])
def bookmarks_get():
    result = heutagogy.persistence.get_bookmarks()
    return Response(json.dumps(result), mimetype='application/json')
