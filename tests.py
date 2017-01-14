#!/usr/bin/env python3
import heutagogy
from heutagogy.persistence import db, User
import unittest
import json


def get_json(response):
    '''Extracts json from the response.'''
    return json.loads(response.get_data().decode())


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
        heutagogy.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        heutagogy.app.config['TESTING'] = True

        db.create_all()

        db.session.add(User('user1', 'random@gmail.com', 'password1'))
        db.session.add(User('user2', 'modnar@gmail.com', 'password2'))
        db.session.commit()

        self.app = heutagogy.app.test_client()

        self.user1 = self.authorization('user1', 'password1')
        self.user2 = self.authorization('user2', 'password2')

    def tearDown(self):
        db.drop_all()

    def test_post_bookmark(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps({'url': 'https://github.com/'}),
            headers=[self.user1])
        result = get_json(res)

        self.assertEqual(201, res.status_code)
        self.assertEqual(1, result['id'])
        self.assertEqual("https://github.com/", result['url'])

    def test_post_bookmark_requires_authorization(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps({'url': 'https://github.com/'}))
        result = get_json(res)

        self.assertEqual(401, res.status_code)
        self.assertEqual('Authorization Required', result['error'])

    def test_get_bookmark_requires_authorization(self):
        res = self.app.get('/api/v1/bookmarks')
        self.assertEqual(401, res.status_code)

    def test_get_bookmark_returns_nothing(self):
        res = self.app.get('/api/v1/bookmarks',
                           headers=[self.user1])
        result = get_json(res)

        self.assertEqual(200, res.status_code)
        self.assertEqual([], result)

    def test_post_get_bookmark(self):
        bookmark = {
            'url': 'https://github.com/',
            'title': 'GitHub front page',
            'timestamp': '2016-11-06T01:31:15',
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

        self.assertEqual(200, res.status_code)
        self.assertEqual([dict(bookmark, id=1, read=False)], result)

    def test_new_bookmark_post_is_unread(self):
        bookmark = {
            'url': 'https://github.com/',
        }
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps(bookmark),
            headers=[self.user1])
        result = get_json(res)

        self.assertEqual(201, res.status_code)
        self.assertFalse(result['read'])

    def test_new_bookmark_read_is_unread(self):
        bookmark = {
            'url': 'https://github.com/',
        }
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps(bookmark),
            headers=[self.user1])

        bookmark_id = get_json(res)['id']

        res = self.app.get(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps({'read': True}),
            headers=[self.user1])
        result = get_json(res)

        self.assertEqual(200, res.status_code)
        self.assertFalse(result['read'])

    def test_mark_as_read(self):
        bookmark = {
            'url': 'https://github.com/',
        }
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
            data=json.dumps({'read': True}),
            headers=[self.user1])

        self.assertEqual(200, res.status_code)
        result = get_json(res)
        self.assertTrue(result['read'])

    def test_mark_as_read_updates_read(self):
        bookmark = {
            'url': 'https://github.com/',
        }
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps(bookmark),
            headers=[self.user1])
        bookmark_id = get_json(res)['id']

        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps({'read': True}),
            headers=[self.user1])

        res = self.app.get(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[self.user1])

        self.assertEqual(200, res.status_code)
        result = get_json(res)
        self.assertTrue(result['read'])

    def test_wrong_pass(self):
        token = self.authorization('user1', 'wrongpass')
        self.assertIsNone(token)

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

        self.assertEqual(401, res.status_code)
        self.assertEqual('Invalid token', result['error'])

    def test_second_user_auth(self):
        res = self.app.get(
            '/api/v1/bookmarks',
            headers=[self.user2])
        self.assertEqual(200, res.status_code)

    def test_user_doesnt_see_other_bookmarks(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps({'url': 'https://github.com/'}),
            headers=[self.user1])
        self.assertEqual(201, res.status_code)

        res = self.app.get(
            '/api/v1/bookmarks',
            headers=[self.user2])
        self.assertEqual(200, res.status_code)

        self.assertEqual([], get_json(res))

    def test_user_cant_read_other_bookmarks_directly(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps({'url': 'https://github.com/'}),
            headers=[self.user1])
        self.assertEqual(201, res.status_code)
        bookmark_id = get_json(res)['id']

        res = self.app.get(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[self.user2])
        self.assertEqual(404, res.status_code)

    def test_user_change_read_status_for_other_user_bookmarks(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps({'url': 'https://github.com/'}),
            headers=[self.user1])
        self.assertEqual(201, res.status_code)
        bookmark_id = get_json(res)['id']

        res = self.app.post(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps({'read': True}),
            headers=[self.user2])
        self.assertEqual(404, res.status_code)
        self.assertEqual({'error': 'Not found'},
                         get_json(res))

        res = self.app.get(
            '/api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[self.user1])
        self.assertFalse(get_json(res)['read'])

    def test_new_bookmark_requires_url(self):
        bookmark = {
            'title': 'no url',
        }
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps(bookmark),
            headers=[self.user1])
        self.assertEqual(400, res.status_code)
        self.assertEqual({'error': 'url field is mandatory'},
                         get_json(res))

    def test_update_bookmark(self):
        res = self.app.post(
            'api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps({'url': 'https://github.com/'}),
            headers=[self.user1])
        self.assertEqual(201, res.status_code)

        bookmark_id = get_json(res)['id']

        res = self.app.post(
            'api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps({'title': 'GitHub'}),
            headers=[self.user1])
        self.assertEqual(200, res.status_code)
        bookmark = get_json(res)
        self.assertEqual('https://github.com/', bookmark['url'])
        self.assertEqual('GitHub', bookmark['title'])

        res = self.app.get(
            'api/v1/bookmarks/{}'.format(bookmark_id),
            headers=[self.user1])
        self.assertEqual(200, res.status_code)
        bookmark = get_json(res)
        self.assertEqual('https://github.com/', bookmark['url'])
        self.assertEqual('GitHub', bookmark['title'])

    def test_post_bookmarks(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps([
                {'url': 'https://github.com/'},
                {'url': 'http://example.com/'}
            ]),
            headers=[self.user1])
        result = get_json(res)

        self.assertEqual(201, res.status_code)
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

    def test_get_nonexistent_bookmark(self):
        res = self.app.get(
            'api/v1/bookmarks/1',
            headers=[self.user1])
        self.assertEqual(404, res.status_code)
        self.assertEqual({'error': 'Not found'}, get_json(res))

    def test_post_nonexistent_bookmark(self):
        res = self.app.post(
            'api/v1/bookmarks/1',
            content_type='application/json',
            data=json.dumps({'title': 'new title'}),
            headers=[self.user1])
        self.assertEqual(404, res.status_code)
        self.assertEqual({'error': 'Not found'}, get_json(res))

    def test_updating_id_is_error(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps([
                {'url': 'https://github.com/'},
            ]),
            headers=[self.user1])
        bookmark_id = get_json(res)['id']

        res = self.app.post(
            'api/v1/bookmarks/{}'.format(bookmark_id),
            content_type='application/json',
            data=json.dumps({'id': 2}),
            headers=[self.user1])
        self.assertEqual(400, res.status_code)
        self.assertEqual({'error': 'Updating id is not allowed'},
                         get_json(res))

    def test_create_user(self):
        res = self.app.post(
            '/api/v1/users',
            content_type='application/json',
            data=json.dumps({'username': 'rasen',
                             'password': 'topsecret'}))
        self.assertEqual(201, res.status_code)

        res = self.app.post(
            '/api/v1/login',
            content_type='application/json',
            data=json.dumps({
                'username': 'rasen',
                'password': 'topsecret',
            }))
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()
