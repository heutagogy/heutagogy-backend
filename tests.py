#!/usr/bin/env python3
import os
import heutagogy
import unittest
import tempfile
import json
import base64

class HeutagogyTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, heutagogy.app.config['DATABASE'] = tempfile.mkstemp()
        heutagogy.app.config['TESTING'] = True
        self.app = heutagogy.app.test_client()
        with heutagogy.app.app_context():
            heutagogy.persistence.initialize()

        self.authorization = 'Basic ' + base64.b64encode(b'myuser:mypassword').decode('utf-8')

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(heutagogy.app.config['DATABASE'])

    def test_hello_world(self):
        res = self.app.get('/')
        assert b'Hello, world!' == res.data

    def test_post_bookmark(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps({ 'url': 'https://github.com/' }),
            headers=[('Authorization', self.authorization)])
        result = json.loads(res.get_data().decode('utf-8'))

        self.assertEqual(201, res.status_code)
        self.assertEqual(1, result['id'])
        self.assertEqual("https://github.com/", result['url'])

    def test_post_bookmark_requires_authorization(self):
        res = self.app.post(
            '/api/v1/bookmarks',
            content_type='application/json',
            data=json.dumps({ 'url': 'https://github.com/' }))
        result = json.loads(res.get_data().decode('utf-8'))

        self.assertEqual(401, res.status_code)
        self.assertDictEqual({'message': 'Unauthorized'}, result)

    def test_get_bookmark_requires_authorization(self):
        res = self.app.get('/api/v1/bookmarks')
        self.assertEqual(401, res.status_code)

    def test_get_bookmark_returns_nothing(self):
        res = self.app.get('/api/v1/bookmarks',
                           headers=[('Authorization', self.authorization)])
        result = json.loads(res.get_data().decode('utf-8'))

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
            headers=[('Authorization', self.authorization)])
        res = self.app.get(
            '/api/v1/bookmarks',
            headers=[('Authorization', self.authorization)])
        result = json.loads(res.get_data().decode('utf-8'))

        self.assertEqual(200, res.status_code)
        self.assertEqual([dict(bookmark, id=1)], result)

if __name__ == '__main__':
    unittest.main()
