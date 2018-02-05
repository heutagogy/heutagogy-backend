from heutagogy import app
from heutagogy.heutagogy import q
import heutagogy.persistence as db
from heutagogy.auth import token_required
import heutagogy.article as article

from flask_user import current_user
from flask import request, send_from_directory
from flask_restful import Resource, Api
import sqlalchemy.orm

from http import HTTPStatus
import datetime
import aniso8601
import urllib.parse as urlparse
import link_header as lh

api = Api(app)


@app.route('/')
def root():
    return send_from_directory('public', 'index.html')


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers['Access-Control-Expose-Headers'] = 'Link'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = \
            'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response


def update_query(url, params):
    """Update query parameters in the url with params"""
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlparse.urlencode(query)
    return urlparse.urlunparse(url_parts)


def filter_url(url):
    u = urlparse.urlsplit(url)

    query = sorted([
        (k, v)
        for k, v in urlparse.parse_qsl(u.query)
        if not k.startswith('utm_')])

    u = u._replace(fragment='', query=urlparse.urlencode(query))

    return u.geturl()


def is_child(parent, potential_child):
    if parent.id == potential_child.id:
        return True

    for child in parent.children:
        if is_child(child, potential_child):
            return True

    return False


class Bookmarks(Resource):
    @token_required
    def get(self):
        url = request.args.get('url')
        tags = request.args.getlist('tag')

        filters = [db.Bookmark.user == current_user.id]
        if url is not None:
            filters.append(db.Bookmark.url == filter_url(url))

        # If Bookmark.tags is null, filtering will yield no results
        if tags:
            filters.append(db.Bookmark.tags.contains(tags))

        result = db.Bookmark.query.filter(*filters) \
                                  .order_by(
                                      db.Bookmark.read.desc().nullsfirst(),
                                      db.Bookmark.timestamp.desc()) \
                                  .paginate()
        headers = {}
        links = []
        if result.has_next:
            last_url = update_query(request.url, {'page': result.pages})
            links.append(lh.Link(last_url, rel='last'))

        if links:
            headers['Link'] = lh.format_links(links)
        return list(map(lambda x: x.to_dict(), result.items)), 200, headers

    @token_required
    def post(self):
        r = request.get_json()

        if not r:
            return {'error': 'payload is mandatory'}, HTTPStatus.BAD_REQUEST

        if isinstance(r, dict):
            r = [r]

        bookmarks = []
        now = datetime.datetime.utcnow().isoformat()

        for entity in r:
            if 'url' not in entity:
                return {'error': 'url field is mandatory'}, \
                    HTTPStatus.BAD_REQUEST

            url = filter_url(entity['url'])

            if entity.get('read'):
                read = aniso8601.parse_datetime(entity.get('read'))
            else:
                read = None

            meta = entity.get('meta')

            if entity.get('title'):
                title = entity.get('title')
            else:
                title = url

            tags = entity.get('tags')

            parent_id = entity.get('parent')
            if parent_id is not None:
                parent = db.Bookmark.query \
                                  .filter_by(id=parent_id,
                                             user=current_user.id) \
                                  .first()

                if parent is None:
                    return {'error': 'parent does not exist'}, \
                        HTTPStatus.BAD_REQUEST

            bookmark = db.Bookmark(
                user=current_user.id,
                url=url,
                title=title,
                timestamp=aniso8601.parse_datetime(
                    entity.get('timestamp', now)),
                read=read,
                meta=meta,
                tags=tags,
                parent_id=parent_id)

            db.db.session.add(bookmark)
            db.db.session.commit()

            bookmarks.append(bookmark)

            q.enqueue(article.fetch_article, bookmark.id, url)

        res = list(map(lambda x: x.to_dict(), bookmarks))
        return res[0] if len(res) == 1 else res, HTTPStatus.CREATED


class Bookmark(Resource):
    @token_required
    def get(self, id):
        bookmark = db.Bookmark.query \
                              .filter_by(id=id, user=current_user.id) \
                              .first()
        if bookmark is None:
            return {'error': 'Not found'}, HTTPStatus.NOT_FOUND
        return bookmark.to_dict()

    @token_required
    def post(self, id):
        update = request.get_json()
        if 'id' in update:
            return {'error': 'Updating id is not allowed'}, \
                HTTPStatus.BAD_REQUEST

        bookmark = db.Bookmark.query \
                              .filter_by(id=id, user=current_user.id) \
                              .first()
        if bookmark is None:
            return {'error': 'Not found'}, HTTPStatus.NOT_FOUND

        if 'url' in update:
            bookmark.url = filter_url(update['url'])
        if 'title' in update:
            bookmark.title = update['title']
        if 'timestamp' in update:
            bookmark.timestamp = aniso8601.parse_datetime(update['timestamp'])
        if 'read' in update:
            if update['read']:
                bookmark.read = aniso8601.parse_datetime(update['read'])
            else:
                bookmark.read = None

        if 'meta' in update:
            bookmark.meta = update['meta'] if update['meta'] else None

        if 'tags' in update:
            bookmark.tags = update['tags']
        if 'parent' in update:
            parent_id = update['parent']
            if parent_id is not None:
                parent = db.Bookmark.query \
                                    .filter_by(id=parent_id,
                                               user=current_user.id) \
                                    .first()

                if parent is None:
                    return {'error': 'parent does not exist'}, \
                        HTTPStatus.BAD_REQUEST

                if is_child(bookmark, parent):
                    return {'error': 'bookmark loops are not allowed'}, \
                        HTTPStatus.BAD_REQUEST
            bookmark.parent_id = parent_id

        db.db.session.add(bookmark)
        db.db.session.commit()

        return bookmark.to_dict(), HTTPStatus.OK

    @token_required
    def delete(self, id):
        bookmark = db.Bookmark.query \
                              .filter_by(id=id, user=current_user.id) \
                              .first()
        if bookmark is None:
            return {'error': 'Not found'}, HTTPStatus.NOT_FOUND

        db.db.session.delete(bookmark)
        db.db.session.commit()

        return (), HTTPStatus.NO_CONTENT


class BookmarkContent(Resource):
    @token_required
    def get(self, id):
        bookmark = db.Bookmark.query \
                              .options(sqlalchemy.orm.load_only(
                                  'content_text', 'content_html')) \
                              .filter_by(id=id, user=current_user.id) \
                              .first_or_404()

        return {'html': bookmark.content_html, 'text': bookmark.content_text}


class BookmarkNotes(Resource):
    @token_required
    def post(self, id):
        bookmark = db.Bookmark.query \
                              .filter_by(id=id, user=current_user.id) \
                              .first_or_404()

        r = request.get_json()
        if not r:
            return {'error': 'payload is mandatory'}, HTTPStatus.BAD_REQUEST
        if 'text' not in r:
            return {'error': 'text field is mandatory'}, HTTPStatus.BAD_REQUEST

        note = db.Note(bookmark, r['text'])

        db.db.session.add(note)
        db.db.session.commit()

        return note.to_dict(), HTTPStatus.CREATED


class Tags(Resource):
    @token_required
    def get(self):
        bookmarks = db.Bookmark.query \
                    .filter(db.Bookmark.user == current_user.id,
                            db.Bookmark.tags != None).all() # noqa
        return list(set().union(*map(lambda x: x.tags, bookmarks)))


class Notes(Resource):
    @token_required
    def get(self, id):
        note = db.Note.query \
                      .filter_by(id=id) \
                      .first_or_404()
        if note.bookmark.user != current_user.id:
            return {'error': 'Note does not exist'}, HTTPStatus.NOT_FOUND

        return note.to_dict()

    @token_required
    def post(self, id):
        note = db.Note.query \
                      .filter_by(id=id) \
                      .first()
        if note is None or note.bookmark.user != current_user.id:
            return {'error': 'Not found'}, HTTPStatus.NOT_FOUND

        r = request.get_json()
        if 'text' in r:
            note.text = r['text']

        db.db.session.add(note)
        db.db.session.commit()

        return note.to_dict(), HTTPStatus.OK

    @token_required
    def delete(self, id):
        note = db.Note.query \
                      .filter_by(id=id) \
                      .first()
        if note is None or note.bookmark.user != current_user.id:
            return {'error': 'Not found'}, HTTPStatus.NOT_FOUND

        db.db.session.delete(note)
        db.db.session.commit()

        return (), HTTPStatus.NO_CONTENT


class Stats(Resource):
    def get(self):
        total_read = db.Bookmark.query \
                                .filter(db.Bookmark.read != None) \
                                .count() # noqa

        week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
        read_in_7days = db.Bookmark.query \
                                   .filter(db.Bookmark.read > week_ago) \
                                   .count()

        return {
            'total_read': total_read,
            'total_read_7days': read_in_7days,
        }


api.add_resource(Bookmarks,       '/api/v1/bookmarks')
api.add_resource(Bookmark,        '/api/v1/bookmarks/<int:id>')
api.add_resource(BookmarkContent, '/api/v1/bookmarks/<int:id>/content')
api.add_resource(BookmarkNotes,   '/api/v1/bookmarks/<int:id>/notes')
api.add_resource(Tags,            '/api/v1/tags')
api.add_resource(Notes,           '/api/v1/notes/<int:id>')
api.add_resource(Stats,           '/api/v1/stats')
