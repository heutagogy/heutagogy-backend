from heutagogy import app
import heutagogy.persistence

from flask_jwt import jwt_required, current_identity
from flask import request
from flask_restful import Resource, Api
import datetime

api = Api(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = \
            'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response


class Bookmarks(Resource):
    @jwt_required()
    def get(self):
        current_user_id = current_identity.id
        result = heutagogy.persistence.get_bookmarks(current_user_id)
        return result

    @jwt_required()
    def post(self):
        r = request.get_json()

        if not r:
            return {'error': 'payload is mandatory'}, 400

        if isinstance(r, dict):
            r = [r]

        bookmarks = []
        current_user_id = current_identity.id
        now = datetime.datetime.utcnow().isoformat()

        for entity in r:
            if 'url' not in entity:
                return {'error': 'url field is mandatory'}, 400

            bookmarks.append({
                'read': entity.get('read', False),
                'timestamp': entity.get('timestamp', now),
                'title': entity.get('title', entity['url']),
                'url': entity['url'],
            })

        res = heutagogy.persistence.save_bookmarks(current_user_id, bookmarks)
        return res[0] if len(res) == 1 else res, 201


class Bookmark(Resource):
    @jwt_required()
    def get(self, id):
        current_user_id = current_identity.id
        bookmark = heutagogy.persistence.get_bookmark(current_user_id, id)
        if bookmark is None:
            return {'error': 'Not found'}, 404
        return bookmark

    @jwt_required()
    def post(self, id):
        update = request.get_json()
        if 'id' in update:
            return {'error': 'Updating id is not allowed'}, 400

        current_user_id = current_identity.id
        bookmark = heutagogy.persistence.get_bookmark(current_user_id, id)
        if bookmark is None:
            return {'error': 'Not found'}, 404

        updated = dict(bookmark, **update)

        result = heutagogy.persistence.set_bookmark(updated)
        return result, 200


api.add_resource(Bookmarks, '/api/v1/bookmarks')
api.add_resource(Bookmark,  '/api/v1/bookmarks/<int:id>')
