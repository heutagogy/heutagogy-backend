#!/usr/bin/env python3
import heutagogy
from heutagogy.persistence import db
from heutagogy.auth import User
from http import HTTPStatus
import unittest
import json
import urllib.parse
from urllib.parse import urlencode
import link_header as lh
from datetime import datetime, timedelta


def get_json(response):
    '''Extracts json from the response.'''
    return json.loads(response.get_data().decode())


def single_user(f):
    def wrapper(*args):
        user1 = User(username='user1', email='random@gmail.com')
        user1.set_password('password1')
        db.session.add(user1)
        db.session.commit()
        return f(*args)
    return wrapper


def multiple_users(f):
    def wrapper(*args):
        user1 = User(username='user1', email='random@gmail.com')
        user1.set_password('password1')
        user2 = User(username='user2', email='modnar@gmail.com')
        user2.set_password('password2')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        return f(*args)
    return wrapper


def parse_url(url):
    res = list(urllib.parse.urlparse(url))
    res[4] = urllib.parse.parse_qs(res[4])
    return res


def parse_link_in_header(link_header):
    """Parses all links in the link_header.to_py() result. This helps
making test results deterministic."""
    def parse_header_link(x):
        res = list(x)
        res[0] = parse_url(res[0])
        return res
    return list(map(parse_header_link, link_header))


class HeutagogyTestCase(unittest.TestCase):

    def authorization(self, username, password):
        '''
        Creates an Authorization header for the given username and
        password.
        '''
        res = self.app.post(
            '/api/v1/login',
            content_type='application/json',
            data=json.dumps({
                'username': username,
                'password': password
            }))
        result = get_json(res)
        token = result.get('access_token', None)
        return ('Authorization', 'JWT ' + token) if token else None

    def setUp(self):
        heutagogy.app.config['TESTING'] = True

        db.create_all()

        self.app = heutagogy.app.test_client()

    @property
    def user1(self):
        if not hasattr(self, '_user1'):
            self._user1 = self.authorization('user1', 'password1')
        return self._user1

    @property
    def user2(self):
        if not hasattr(self, '_user2'):
            self._user2 = self.authorization('user2', 'password2')
        return self._user2

    def tearDown(self):
        db.drop_all()

    def add_bookmark(self,
                     bookmark={'url': 'http://github.com',
                               'title': 'test title'},
                     user=None):
        user = user or self.user1
        return self.app.post(
            'api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps(bookmark),
            headers=[user])

    def get_bookmark(self, bookmark_id, user=None):
        user = user or self.user1
        return self.app.get(
            'api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[user])

    def delete_bookmark(self, bookmark_id, user=None):
        user = user or self.user1
        return self.app.delete(
            'api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[user])


class ApiTestCase(HeutagogyTestCase):
    @single_user
    def test_post_bookmark(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps({'url': 'https://github.com/',
                             'title': 'Sample title'}),
            headers=[self.user1])
        result = get_json(res)

        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        self.assertEqual(1, result['id'])
        self.assertEqual("https://github.com/", result['url'])

    def test_post_bookmark_requires_authorization(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps({'url': 'https://github.com/',
                             'title': 'sample title'}))

        self.assertEqual(401, res.status_code)
        self.assertEqual('Authorization Required', get_json(res)['error'])

    def test_get_bookmark_requires_authorization(self):
        res = self.app.get('/api/v1/bookmarks')
        self.assertEqual(401, res.status_code)

    @single_user
    def test_get_bookmark_returns_nothing(self):
        res = self.app.get('/api/v1/bookmarks',
                           headers=[self.user1])
        result = get_json(res)

        self.assertEqual(200, res.status_code)
        self.assertEqual([], result)

    @single_user
    def test_post_get_bookmark(self):
        bookmark = {
            'url': 'https://github.com/',
            'title': 'GitHub front page',
            'timestamp': '2016-11-06T01:31:15',
            'notes': [],
        }
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps(bookmark),
            headers=[self.user1])
        res = self.app.get(
            '/api/v1/bookmarks',
            headers=[self.user1])
        result = get_json(res)

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual([dict(
            bookmark, id=1, read=None, meta=None, tags=[]
        )], result)

    @single_user
    def test_new_bookmark_post_is_unread(self):
        bookmark = {
            'url': 'https://github.com/',
            'title': 'Sample title',
        }
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps(bookmark),
            headers=[self.user1])
        result = get_json(res)

        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        self.assertIsNone(result['read'])

    @single_user
    def test_new_bookmark_read_is_unread(self):
        bookmark = {
            'url': 'https://github.com/',
            'title': 'Sample title',
        }
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps(bookmark),
            headers=[self.user1])

        bookmark_id = get_json(res)['id']

        res = self.app.get(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[self.user1])
        result = get_json(res)

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertIsNone(result['read'])

    @single_user
    def test_new_bookmark_no_meta(self):
        bookmark = {
            'url': 'https://github.com/',
            'title': 'Sample title',
        }
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps(bookmark),
            headers=[self.user1])

        bookmark_id = get_json(res)['id']

        res = self.app.get(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[self.user1])
        result = get_json(res)

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertIsNone(result['meta'])

    @single_user
    def test_mark_as_read(self):
        bookmark = {
            'url': 'https://github.com/',
            'title': 'Sample title',
        }
        read = '2016-11-06T01:31:15'
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps(bookmark),
            headers=[self.user1])
        result = get_json(res)

        bookmark_id = result['id']

        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps({'read': read}),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        result = get_json(res)
        self.assertEqual(read, result['read'])

    @single_user
    def test_mark_as_read_updates_read(self):
        bookmark = {
            'url': 'https://github.com/',
        }
        read = '2016-11-06T01:31:15'
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps(bookmark),
            headers=[self.user1])
        bookmark_id = get_json(res)['id']

        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps({'read': read}),
            headers=[self.user1])

        res = self.app.get(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        result = get_json(res)
        self.assertEqual(read, result['read'])

    @single_user
    def test_update_meta(self):
        bookmark = {
            'url': 'https://github.com/',
        }
        meta = {"blah": True}

        # create bookmark
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps(bookmark),
            headers=[self.user1])
        bookmark_id = get_json(res)['id']

        # update meta
        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps({'meta': meta}),
            headers=[self.user1])

        # check result
        res = self.app.get(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        result = get_json(res)
        self.assertEqual(meta, result['meta'])

    @single_user
    def test_wrong_pass(self):
        token = self.authorization('user1', 'wrongpass')
        self.assertIsNone(token)

    @single_user
    def test_invalid_token(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            headers=[('Authorization', 'JWT '
                      + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
                      + 'eyJuYmYiOjE0ODI0MjE2NzUsImlhdCI6MTQ4M'
                      + 'jQyMTY3NSwiZXhwIjoxNDg1MDEzNjc1LCJpZG'
                      + 'VudGl0eSI6InVzZXIzIn0.ZumbtlrLZAW0R60'
                      + 'kiJKASGU29AoAUVMMLmwLqvuWzz8')],
            data=json.dumps({'url': 'https://github.com/'}))
        result = get_json(res)

        self.assertEqual(HTTPStatus.UNAUTHORIZED, res.status_code)
        self.assertEqual('Invalid token', result['error'])

    @multiple_users
    def test_second_user_auth(self):
        res = self.app.get(
            '/api/v1/bookmarks',
            headers=[self.user2])
        self.assertEqual(HTTPStatus.OK, res.status_code)

    @multiple_users
    def test_user_doesnt_see_other_bookmarks(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps({'url': 'https://github.com/',
                             'title': 'Sample title'}),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get(
            '/api/v1/bookmarks',
            headers=[self.user2])
        self.assertEqual(HTTPStatus.OK, res.status_code)

        self.assertEqual([], get_json(res))

    @multiple_users
    def test_user_cant_read_other_bookmarks_directly(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps({'url': 'https://github.com/',
                             'title': 'Sample title'}),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        bookmark_id = get_json(res)['id']

        res = self.app.get(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[self.user2])
        self.assertEqual(HTTPStatus.NOT_FOUND, res.status_code)

    @multiple_users
    def test_user_cant_change_read_status_for_other_user_bookmarks(self):
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        bookmark_id = get_json(res)['id']

        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps({'read': '2016-11-06T01:31:15'}),
            headers=[self.user2])
        self.assertEqual(HTTPStatus.NOT_FOUND, res.status_code)
        self.assertEqual({'error': 'Not found'},
                         get_json(res))

        res = self.app.get(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[self.user1])
        self.assertIsNone(get_json(res)['read'])

    @single_user
    def test_new_bookmark_requires_url(self):
        bookmark = {
            'title': 'no url',
        }
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps(bookmark),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.BAD_REQUEST, res.status_code)
        self.assertEqual({'error': 'url field is mandatory'},
                         get_json(res))

    @single_user
    def test_update_bookmark(self):
        res = self.add_bookmark({
            'url': 'https://github.com/',
            'title': 'some title',
        })
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        bookmark_id = get_json(res)['id']

        res = self.app.post(
            'api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps({'title': 'GitHub'}),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.OK, res.status_code)
        bookmark = get_json(res)
        self.assertEqual('https://github.com/', bookmark['url'])
        self.assertEqual('GitHub', bookmark['title'])

        res = self.app.get(
            'api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.OK, res.status_code)
        bookmark = get_json(res)
        self.assertEqual('https://github.com/', bookmark['url'])
        self.assertEqual('GitHub', bookmark['title'])

    @single_user
    def test_post_bookmarks(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps([
                {'url': 'https://github.com/',
                 'title': 'GitHub'},
                {'url': 'http://example.com/',
                 'title': 'Example'},
            ]),
            headers=[self.user1])
        result = get_json(res)

        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        self.assertEqual(1, result[0]['id'])
        self.assertEqual("https://github.com/", result[0]['url'])
        self.assertEqual(2, result[1]['id'])
        self.assertEqual("http://example.com/", result[1]['url'])

    def test_cors_headers(self):
        res = self.app.options(
            '/api/v1/bookmarks',
            headers=[('Access-Control-Request-Headers',
                      'authorization, content-type'),
                     ('Access-Control-Request-Method', 'GET')])

        self.assertEqual(res.headers['Access-Control-Allow-Origin'],
                         '*')
        self.assertEqual(res.headers['Access-Control-Allow-Methods'],
                         'DELETE, GET, POST, PUT')
        self.assertEqual(res.headers['Access-Control-Allow-Headers'],
                         'authorization, content-type')

    @single_user
    def test_get_nonexistent_bookmark(self):
        res = self.app.get(
            'api/v1/bookmarks/1',
            headers=[self.user1])
        self.assertEqual(HTTPStatus.NOT_FOUND, res.status_code)
        self.assertEqual({'error': 'Not found'}, get_json(res))

    @single_user
    def test_post_nonexistent_bookmark(self):
        res = self.app.post(
            'api/v1/bookmarks/1',
            content_type='application/json',
            data=json.dumps({'title': 'new title'}),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.NOT_FOUND, res.status_code)
        self.assertEqual({'error': 'Not found'}, get_json(res))

    @single_user
    def test_updating_id_is_error(self):
        res = self.add_bookmark()
        bookmark_id = get_json(res)['id']

        res = self.app.post(
            'api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps({'id': 2}),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.BAD_REQUEST, res.status_code)
        self.assertEqual({'error': 'Updating id is not allowed'},
                         get_json(res))

    @single_user
    def test_handle_timezone(self):
        res = self.app.post(
            'api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps({'url': 'https://github.com/',
                             'title': 'Sample title',
                             'timestamp': '2017-01-01T01:20:13+0200'}),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        self.assertEqual('2016-12-31T23:20:13', get_json(res)['timestamp'])

    @single_user
    def test_paginate(self):
        for _ in range(30):
            res = self.add_bookmark()
            self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get(
            'api/v1/bookmarks',
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual(20, len(get_json(res)))

    @single_user
    def test_paginate_next_page(self):
        for _ in range(30):
            res = self.add_bookmark()
            self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get(
            'api/v1/bookmarks?page=2',
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual(10, len(get_json(res)))

    @single_user
    def test_paginate_404_on_unknown_page(self):
        res = self.app.get('api/v1/bookmarks?page=2', headers=[self.user1])

        self.assertEqual(HTTPStatus.NOT_FOUND, res.status_code)

    @single_user
    def test_paginate_num_per_page(self):
        for _ in range(30):
            res = self.add_bookmark()
            self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get(
            'api/v1/bookmarks?per_page=15',
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual(15, len(get_json(res)))

    @single_user
    def test_delete_does_delete(self):
        res = self.add_bookmark()
        bookmark_id = get_json(res)['id']

        res = self.delete_bookmark(bookmark_id)
        res = self.get_bookmark(bookmark_id)

        self.assertEqual(HTTPStatus.NOT_FOUND, res.status_code)

    @single_user
    def test_delete_return_204_no_content(self):
        res = self.add_bookmark()
        bookmark_id = get_json(res)['id']
        res = self.delete_bookmark(bookmark_id)

        self.assertEqual(HTTPStatus.NO_CONTENT, res.status_code)
        self.assertEqual(b'', res.get_data())

    @single_user
    def test_delete_does_not_reuse_ids(self):
        res = self.add_bookmark()
        bookmark_id = get_json(res)['id']

        res = self.delete_bookmark(bookmark_id)

        res = self.add_bookmark()

        self.assertNotEqual(bookmark_id, get_json(res)['id'])

    @single_user
    def test_filter_by_url(self):
        self.add_bookmark({'url': 'https://heutagogy-frontend.herokuapp.com',
                           'title': 'Heutagogy frontend'})
        self.add_bookmark({'url': 'https://github.com',
                           'title': 'GitHub'})
        self.add_bookmark({'url': 'https://www.wikipedia.org',
                           'title': 'Wikipedia'})
        self.add_bookmark(
            {'url': 'https://github.com/flask-restful/flask-restful',
             'title': 'Flask-RESTful'})

        res = self.app.get(
            'api/v1/bookmarks?{}'.format(
                urlencode({'url': 'https://github.com'})),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)

        r = get_json(res)
        self.assertEqual(1, len(r))
        self.assertEqual('https://github.com', r[0]['url'])

    @single_user
    def test_strip_fragment_on_save(self):
        res = self.add_bookmark(
            {'url': 'https://medium.com/some-article#.vlqdq2s5j',
             'title': 'Some article'})

        self.assertEqual('https://medium.com/some-article',
                         get_json(res)['url'])

    @single_user
    def test_strip_fragment_on_search(self):
        self.add_bookmark(
            {'url': 'https://medium.com/some-article#.vlqdq2s5j',
             'title': 'Some article'})

        res = self.app.get(
            'api/v1/bookmarks?{}'.format(urlencode(
                {'url': 'https://medium.com/some-article#.yfsxelyhh'})),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)

        r = get_json(res)
        self.assertEqual(1, len(r))
        self.assertEqual('https://medium.com/some-article', r[0]['url'])

    @single_user
    def test_strip_fragment_on_update(self):
        res = self.add_bookmark({'url': 'https://medium.com/some-article',
                                 'title': 'Some article'})
        bookmark_id = get_json(res)['id']

        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps(
                {'url': 'https://medium.com/some-article#.vlqdq2s5j'}),
            headers=[self.user1])

        self.assertEqual('https://medium.com/some-article',
                         get_json(res)['url'])

    @single_user
    def test_bookmarks_order(self):
        id1 = get_json(self.add_bookmark({
            'url': 'http://example3.com',
            'title': 'Sample title',
            'timestamp': '2017-02-01T11:12:12Z',
        }))['id']
        id2 = get_json(self.add_bookmark({
            'url': 'http://example2.com',
            'title': 'Sample title',
            'timestamp': '2017-02-01T12:30:05Z',
            'read': '2017-02-01T13:20:01Z',
        }))['id']
        id3 = get_json(self.add_bookmark({
            'url': 'http://example1.com',
            'title': 'Sample title',
            'timestamp': '2017-02-01T12:30:05Z',
        }))['id']
        id4 = get_json(self.add_bookmark({
            'url': 'http://example4.com',
            'title': 'Sample title',
            'timestamp': '2017-01-01T12:11:13Z',
            'read': '2017-02-01T13:20:02Z',
        }))['id']

        # should be [3, 1, 4, 2]
        b = get_json(self.app.get('/api/v1/bookmarks',
                                  headers=[self.user1]))

        self.assertEqual(id3, b[0]['id'])
        self.assertEqual(id1, b[1]['id'])
        self.assertEqual(id4, b[2]['id'])
        self.assertEqual(id2, b[3]['id'])

    @single_user
    def test_bookmarks_return_link_last(self):
        for _ in range(25):
            self.add_bookmark()

        res = self.app.get('/api/v1/bookmarks',
                           headers=[self.user1])

        self.assertTrue('Link' in res.headers)
        links = lh.parse(res.headers['Link']).to_py()
        self.assertIn([parse_url('http://localhost/api/v1/bookmarks?page=2'),
                       [['rel', 'last']]], parse_link_in_header(links))

    @single_user
    def test_bookmark_return_link_last_with_per_page(self):
        for _ in range(8):
            self.add_bookmark()

        res = self.app.get('/api/v1/bookmarks?per_page=3',
                           headers=[self.user1])

        self.assertTrue('Link' in res.headers)
        links = lh.parse(res.headers['Link']).to_py()
        self.assertIn([
            parse_url('http://localhost/api/v1/bookmarks?page=3&per_page=3'),
            [['rel', 'last']]
        ], parse_link_in_header(links))

    @single_user
    def test_bookmarks_dont_return_link_last_when_on_last(self):
        for _ in range(25):
            self.add_bookmark()

        res = self.app.get('/api/v1/bookmarks?page=2',
                           headers=[self.user1])

        self.assertTrue('Link' not in res.headers)

    @single_user
    def test_add_bookmark_with_tags(self):
        bookmark = {
            'url': 'http://github.com',
            'title': 'test title',
            'tags': ['github', 'test'],
        }

        res = self.add_bookmark(bookmark)

        self.assertEqual(HTTPStatus.CREATED, res.status_code)

    @single_user
    def test_get_bookmark_with_tag(self):
        bookmark = {
            'url': 'http://github.com',
            'title': 'test title',
            'timestamp': '2016-11-06T01:31:15',
            'tags': ['github', 'test'],
            'notes': [],
        }
        res = self.add_bookmark(bookmark)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get(
            '/api/v1/bookmarks',
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual([dict(
            bookmark, id=1, read=None, meta=None
        )], get_json(res))

    @single_user
    def test_filter_by_tag(self):
        bookmark = {
            'url': 'http://github.com',
            'title': 'test title',
            'timestamp': '2016-11-06T01:31:15',
            'tags': ['github', 'test'],
            'notes': [],
        }
        res = self.add_bookmark(bookmark)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get(
            '/api/v1/bookmarks?tag=github',
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual([dict(
            bookmark, id=1, read=None, meta=None
        )], get_json(res))

    @single_user
    def test_filter_by_tag_full_match(self):
        bookmark = {
            'url': 'http://github.com',
            'title': 'correct article',
            'timestamp': '2016-11-06T01:31:15',
            'tags': ['github', 'test'],
            'notes': [],
        }
        res = self.add_bookmark(bookmark)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark({
            'url': 'http://github.com/rasendubi',
            'title': 'wrong article',
            'tags': ['github'],
        })
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get(
            '/api/v1/bookmarks?tag=github&tag=test',
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual([dict(
            bookmark, id=1, read=None, meta=None
        )], get_json(res))

    @single_user
    def test_update_bookmark_tags(self):
        bookmark = {
            'url': 'http://github.com',
            'title': 'test title',
            'tags': ['github', 'test'],
        }
        res = self.add_bookmark(bookmark)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        result = get_json(res)
        bookmark_id = result['id']

        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps({'tags': ['test']}),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        result = get_json(res)
        self.assertEqual(['test'], result['tags'])

    @single_user
    def test_get_tags(self):
        res = self.add_bookmark({
            'url': 'http://github.com',
            'title': 'test title',
            'tags': ['github', 'test'],
        })
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark({
            'url': 'http://github.com',
            'title': 'test title',
            'tags': ['blah', 'test'],
        })
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark({
            'url': 'http://github.com',
            'title': 'test title',
            'tags': ['hello', 'world'],
        })
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get(
            '/api/v1/tags',
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual(sorted(['github', 'test', 'blah', 'hello', 'world']),
                         sorted(get_json(res)))

    @single_user
    def test_get_tags_empty(self):
        res = self.app.get(
            '/api/v1/tags',
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual(sorted([]),
                         sorted(get_json(res)))

    @single_user
    def test_add_note(self):
        bookmark = {
            'url': 'http://github.com',
            'title': 'test title',
        }
        note = {
            'text': 'test note',
        }
        res = self.add_bookmark(bookmark)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        result = get_json(res)
        bookmark_id = result['id']

        res = self.app.post(
            '/api/v1/bookmarks/{}/notes'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps(note),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        result = get_json(res)
        self.assertEqual('test note', result['text'])
        self.assertIn('id', result)

    @single_user
    def test_get_added_note(self):
        bookmark = {
            'url': 'http://github.com',
            'title': 'test title',
        }
        note = {
            'text': 'test note',
        }
        res = self.add_bookmark(bookmark)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        result = get_json(res)
        bookmark_id = result['id']
        res = self.app.post(
            '/api/v1/bookmarks/{}/notes'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps(note),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        result = get_json(res)['notes'][0]
        self.assertEqual('test note', result['text'])
        self.assertIn('id', result)

    @single_user
    def test_get_note_by_id(self):
        bookmark = {
            'url': 'http://github.com',
            'title': 'test title',
        }
        note = {
            'text': 'test note',
        }
        res = self.add_bookmark(bookmark)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        result = get_json(res)
        bookmark_id = result['id']
        res = self.app.post(
            '/api/v1/bookmarks/{}/notes'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps(note),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        note_id = get_json(res)['id']
        res = self.app.get(
            '/api/v1/notes/{}'.format(note_id),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        result = get_json(res)
        self.assertEqual('test note', result['text'])
        self.assertEqual(note_id, result['id'])

    @single_user
    def test_update_note_by_id(self):
        bookmark = {
            'url': 'http://github.com',
            'title': 'test title',
        }
        note = {
            'text': 'test note',
        }
        res = self.add_bookmark(bookmark)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        result = get_json(res)
        bookmark_id = result['id']
        res = self.app.post(
            '/api/v1/bookmarks/{}/notes'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps(note),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        note_id = get_json(res)['id']
        res = self.app.post(
            '/api/v1/notes/{}'.format(note_id),
            content_type='application/json',
            data=json.dumps({'text': 'new text'}),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        result = get_json(res)
        self.assertEqual('new text', result['text'])
        self.assertEqual(note_id, result['id'])

    @single_user
    def test_delete_note_by_id(self):
        bookmark = {
            'url': 'http://github.com',
            'title': 'test title',
        }
        note = {
            'text': 'test note',
        }
        res = self.add_bookmark(bookmark)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        result = get_json(res)
        bookmark_id = result['id']
        res = self.app.post(
            '/api/v1/bookmarks/{}/notes'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps(note),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        note_id = get_json(res)['id']
        res = self.app.delete(
            '/api/v1/notes/{}'.format(note_id),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.NO_CONTENT, res.status_code)
        res = self.app.get(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.OK, res.status_code)
        result = get_json(res)
        self.assertEqual([], result['notes'])

    @single_user
    def test_add_with_parent(self):
        res = self.add_bookmark()
        parent_id = get_json(res)['id']
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.add_bookmark({
            'title': 'GitHub',
            'url': 'https://github.com',
            'parent': parent_id,
        })

        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        self.assertIn('parent', get_json(res))
        self.assertEqual(parent_id, get_json(res)['parent'])

    @single_user
    def test_wrong_parent(self):
        parent_id = 15

        res = self.add_bookmark({
            'title': 'GitHub',
            'url': 'https://github.com',
            'parent': parent_id,
        })

        self.assertEqual(HTTPStatus.BAD_REQUEST, res.status_code)
        self.assertEqual({'error': 'parent does not exist'},
                         get_json(res))

    @single_user
    def test_get_children(self):
        res = self.add_bookmark()
        parent_id = get_json(res)['id']
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark({
            'title': 'GitHub',
            'url': 'https://github.com',
            'parent': parent_id,
        })
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        child_id = get_json(res)['id']

        res = self.get_bookmark(parent_id)

        self.assertEqual(HTTPStatus.OK, res.status_code)
        r = get_json(res)
        self.assertIn('children', r)
        self.assertEqual(1, len(r['children']))
        self.assertEqual(child_id, r['children'][0]['id'])

    @single_user
    def test_drop_utm_params(self):
        bookmark = {
            'title': 'blah',
            'url': 'https://github.com?other=1&utm_blah=ignore',
        }

        res = self.add_bookmark(bookmark)

        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        self.assertEqual('https://github.com?other=1', get_json(res)['url'])

    @single_user
    def test_drop_utm_params_on_search(self):
        bookmark = {
            'title': 'blah',
            'url': 'https://github.com?other=1&utm_blah=ignore',
        }
        res = self.add_bookmark(bookmark)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get(
            'api/v1/bookmarks?{}'.format(urlencode(
                {'url': 'https://github.com?other=1'})),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual(1, len(get_json(res)))
        self.assertEqual('https://github.com?other=1', get_json(res)[0]['url'])

    @single_user
    def test_dont_allow_self_loop(self):
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        bookmark_id = get_json(res)['id']

        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps({'parent': bookmark_id}),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.BAD_REQUEST, res.status_code)

    @single_user
    def test_dont_allow_loops(self):
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        bookmark_id1 = get_json(res)['id']
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        bookmark_id2 = get_json(res)['id']

        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id1),
            content_type='application/json',
            data=json.dumps({'parent': bookmark_id2}),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.OK, res.status_code)
        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id2),
            content_type='application/json',
            data=json.dumps({'parent': bookmark_id1}),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.BAD_REQUEST, res.status_code)

    @single_user
    def test_dont_allow_loops3(self):
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        bookmark_id1 = get_json(res)['id']
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        bookmark_id2 = get_json(res)['id']
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        bookmark_id3 = get_json(res)['id']

        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id1),
            content_type='application/json',
            data=json.dumps({'parent': bookmark_id2}),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.OK, res.status_code)
        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id2),
            content_type='application/json',
            data=json.dumps({'parent': bookmark_id3}),
            headers=[self.user1])
        self.assertEqual(HTTPStatus.OK, res.status_code)
        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id3),
            content_type='application/json',
            data=json.dumps({'parent': bookmark_id1}),
            headers=[self.user1])

        self.assertEqual(HTTPStatus.BAD_REQUEST, res.status_code)


class StatsTestCase(HeutagogyTestCase):
    @single_user
    def test_response_is_ok(self):
        res = self.app.get('/api/v1/stats')

        self.assertEqual(HTTPStatus.OK, res.status_code)

    @single_user
    def test_initial_stats_is_zero(self):
        res = self.app.get('/api/v1/stats')

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual(0, get_json(res)['total_read'])
        self.assertEqual(0, get_json(res)['total_read_7days'])

    @single_user
    def test_unread_bookmarks(self):
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get('/api/v1/stats')

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual(0, get_json(res)['total_read'])

    @single_user
    def test_read_bookmarks(self):
        res = self.add_bookmark({
            'url': 'https://github.com',
            'read': datetime.now().isoformat(),
        })
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get('/api/v1/stats')

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual(1, get_json(res)['total_read'])

    @multiple_users
    def test_multiuser(self):
        res = self.add_bookmark({
            'url': 'https://github.com',
            'read': datetime.now().isoformat(),
        }, user=self.user1)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark({
            'url': 'https://github.com',
            'read': datetime.now().isoformat(),
        }, user=self.user2)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get('/api/v1/stats')

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual(2, get_json(res)['total_read'])

    @single_user
    def test_read_in_7days(self):
        res = self.add_bookmark({
            'url': 'https://github.com',
            'read': datetime.now().isoformat(),
        })
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark({
            'url': 'https://github.com',
            'read': (datetime.now() - timedelta(days=3)).isoformat(),
        })
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark({
            'url': 'https://github.com',
            'read': (datetime.now() - timedelta(days=7)).isoformat(),
        })
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark()
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res = self.app.get('/api/v1/stats')

        self.assertEqual(HTTPStatus.OK, res.status_code)
        self.assertEqual(2, get_json(res)['total_read_7days'])

    @multiple_users
    def test_personal_stats(self):
        res = self.add_bookmark({
            'url': 'https://github.com',
            'read': datetime.now().isoformat(),
        }, user=self.user1)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark({
            'url': 'https://github.com',
            'read': (datetime.now() - timedelta(days=7)).isoformat(),
        }, user=self.user1)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark({
            'url': 'https://github.com',
            'read': (datetime.now() - timedelta(days=3)).isoformat(),
        }, user=self.user2)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        res = self.add_bookmark({
            'url': 'https://github.com',
            'read': (datetime.now() - timedelta(days=700)).isoformat(),
        }, user=self.user1)
        self.assertEqual(HTTPStatus.CREATED, res.status_code)

        res1 = self.app.get('/api/v1/stats', headers=[self.user1])
        res2 = self.app.get('/api/v1/stats', headers=[self.user2])

        self.assertEqual(HTTPStatus.OK, res1.status_code)
        self.assertEqual(HTTPStatus.OK, res2.status_code)

        self.assertEqual(3, get_json(res1)['user_read'])
        self.assertEqual(1, get_json(res2)['user_read'])

        self.assertEqual(1, get_json(res1)['user_read_today'])
        self.assertEqual(0, get_json(res2)['user_read_today'])

        self.assertEqual(2, get_json(res1)['user_read_year'])
        self.assertEqual(1, get_json(res2)['user_read_year'])


if __name__ == '__main__':
    unittest.main()
