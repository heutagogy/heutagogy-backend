from heutagogy import app
import heutagogy.persistence

from flask import request
from flask_restful import Resource, Api, abort
import flask_login
import datetime

api = Api(app)


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
        bookmark['title'] = r.get('title', bookmark['url'])

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
        update = request.get_json()
        if 'id' in update:
            return {'error': 'Updating id is not allowed'}

        user_id = flask_login.current_user.id
        bookmark = heutagogy.persistence.get_bookmark(user_id, id)
        if bookmark is None:
            return {'error': 'Not found'}, 404

        updated = dict(bookmark, **update)

        result = heutagogy.persistence.set_bookmark(updated)
        return result, 200


api.add_resource(Bookmarks, '/api/v1/bookmarks')
api.add_resource(Bookmark,  '/api/v1/bookmarks/<int:id>')
