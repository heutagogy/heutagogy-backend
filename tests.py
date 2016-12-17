#!/usr/bin/env python3
import os
import heutagogy
import unittest
import tempfile
import json
import base64


def get_json(response):
    '''Extracts json from the response.'''
    return json.loads(response.get_data().decode())


def authorization(username, password):
    '''
    Creates an Authorization header for the given username and
    password.
    '''
    token = (username + ':' + password).encode()
    return ('Authorization', 'Basic ' + base64.b64encode(token).decode())


class HeutagogyTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, heutagogy.app.config['DATABASE'] = tempfile.mkstemp()
        heutagogy.app.config['TESTING'] = True
        heutagogy.app.config['USERS'] = {
            'user1': {'password': 'password1'},
            'user2': {'password': 'password2'},
        }

        self.app = heutagogy.app.test_client()

        with heutagogy.app.app_context():
            heutagogy.persistence.initialize()

        self.user1 = authorization('user1', 'password1')
        self.user2 = authorization('user2', 'password2')

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(heutagogy.app.config['DATABASE'])

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
        self.assertDictEqual({'error': 'Unauthorized'}, result)

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
            'timestamp': '2016-11-06 01:31:15',
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
        self.assertEqual(False, result['read'])

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
        self.assertEqual(False, result['read'])

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
        self.assertEqual(True, result['read'])

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
        self.assertEqual(True, result['read'])

    def test_wrong_pass(self):
        res = self.app.get(
            '/api/v1/bookmarks',
            headers=[authorization('user1', 'wrongpass')])
        self.assertEqual(401, res.status_code)
        self.assertEqual({'error': 'Unauthorized'},
                         get_json(res))

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
        self.assertEqual(False, get_json(res)['read'])

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


if __name__ == '__main__':
    unittest.main()
