from heutagogy import app
import heutagogy.persistence

from flask import request
from flask_restful import Resource, Api, abort
import flask_login
import datetime

api = Api(app)


@app.route('/')
def index():
    return 'Hello, world!'


class Bookmarks(Resource):
    @flask_login.login_required
    def get(self):
        current_user_id = flask_login.current_user.id
        result = heutagogy.persistence.get_bookmarks(current_user_id)
        return result

    @flask_login.login_required
    def post(self):
        r = request.get_json()

        if 'url' not in r:
            return {'error': 'url field is mandatory'}, 400

        bookmark = dict()
        bookmark['url'] = r['url']
        bookmark['title'] = r['title'] if 'title' in r else bookmark['url']

        if 'timestamp' in r:
            bookmark['timestamp'] = r['timestamp']
        else:
            bookmark['timestamp'] = datetime.datetime.utcnow().isoformat(' ')

        bookmark['read'] = r.get('read', False)

        current_user_id = flask_login.current_user.id
        result = heutagogy.persistence.save_bookmark(current_user_id, bookmark)
        return result, 201


class Bookmark(Resource):
    @flask_login.login_required
    def get(self, id):
        current_user_id = flask_login.current_user.id
        bookmark = heutagogy.persistence.get_bookmark(current_user_id, id)
        if bookmark is None:
            abort(404)
        return bookmark

    @flask_login.login_required
    def post(self, id):
        user_id = flask_login.current_user.id
        bookmark = heutagogy.persistence.get_bookmark(user_id, id)
        if bookmark is None:
            return {'error': 'Not found'}, 404

        read = request.get_json()['read']
        result = heutagogy.persistence.set_read(id, read)
        return result


api.add_resource(Bookmarks, '/api/v1/bookmarks')
api.add_resource(Bookmark,  '/api/v1/bookmarks/<int:id>')
