from heutagogy import app
import heutagogy.persistence

from flask import request, jsonify, Response
import flask_login
import json
import datetime
import sqlite3

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/api/v1/bookmarks', methods=['POST'])
@flask_login.login_required
def bookmarks_post():
    r = request.get_json(force=True)

    bookmark = dict()
    try:
        bookmark['url'] = r['url']
    except:
        return jsonify(error='url field is mandatory'), 400

    bookmark['title'] = r['title'] if 'title' in r else bookmark['url']
    bookmark['timestamp'] = r['timestamp'] if 'timestamp' in r else datetime.datetime.utcnow().isoformat(' ')
    bookmark['read'] = r.get('read', False)

    result = heutagogy.persistence.save_bookmark(bookmark)
    return jsonify(**result), 201

@app.route('/api/v1/bookmarks', methods=['GET'])
@flask_login.login_required
def bookmarks_get():
    result = heutagogy.persistence.get_bookmarks()
    return Response(json.dumps(result), mimetype='application/json')

@app.route('/api/v1/bookmark/<int:id>/read', methods=['PUT'])
@flask_login.login_required
def bookmark_read_put(id):
    read = request.get_json()['read']
    result = heutagogy.persistence.set_read(id, read)
    return jsonify(**result)

@app.route('/api/v1/bookmark/<int:id>', methods=['GET'])
@flask_login.login_required
def bookmark_get(id):
    bookmark = heutagogy.persistence.get_bookmark(id)
    return jsonify(**bookmark)
