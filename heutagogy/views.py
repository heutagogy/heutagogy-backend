from heutagogy import app
import heutagogy.persistence as db

from flask_jwt import jwt_required, current_identity
from flask import request
from flask_restful import Resource, Api
import datetime
import aniso8601

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
        result = db.Bookmark.query.filter_by(user=current_user_id)
        return list(map(lambda x: x.to_dict(), result))

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

            bookmarks.append(db.Bookmark(
                user=current_user_id,
                url=entity['url'],
                title=entity.get('title', None),
                timestamp=aniso8601.parse_datetime(
                    entity.get('timestamp', now)),
                read=entity.get('read', False)))

        for bookmark in bookmarks:
            db.db.session.add(bookmark)
        db.db.session.commit()

        res = list(map(lambda x: x.to_dict(), bookmarks))
        return res[0] if len(res) == 1 else res, 201


class Bookmark(Resource):
    @jwt_required()
    def get(self, id):
        current_user_id = current_identity.id
        bookmark = db.Bookmark.query \
                              .filter_by(id=id, user=current_user_id) \
                              .first()
        if bookmark is None:
            return {'error': 'Not found'}, 404
        return bookmark.to_dict()

    @jwt_required()
    def post(self, id):
        update = request.get_json()
        if 'id' in update:
            return {'error': 'Updating id is not allowed'}, 400

        current_user_id = current_identity.id
        bookmark = db.Bookmark.query \
                              .filter_by(id=id, user=current_user_id) \
                              .first()
        if bookmark is None:
            return {'error': 'Not found'}, 404

        if 'url' in update:
            bookmark.url = update['url']
        if 'title' in update:
            bookmark.title = update['title']
        if 'timestamp' in update:
            bookmark.timestamp = aniso8601.parse_datetime(update['timestamp'])
        if 'read' in update:
            bookmark.read = update['read']

        db.db.session.add(bookmark)
        db.db.session.commit()

        return bookmark.to_dict(), 200


class Users(Resource):
    def post(self):
        user = request.get_json()
        if 'username' not in user:
            return {'error': "'username' field is mandatory"}, 400
        if 'password' not in user:
            return {'error': "'password' field is mandatory"}, 400

        db.db.session.add(db.User(user['username'],
                                  user.get('email', None),
                                  user['password']))
        db.db.session.commit()

        return None, 201


api.add_resource(Bookmarks, '/api/v1/bookmarks')
api.add_resource(Bookmark,  '/api/v1/bookmarks/<int:id>')
api.add_resource(Users,     '/api/v1/users')
