#!/usr/bin/env python3
import os
import heutagogy
import unittest
import tempfile

class HeutagogyTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, heutagogy.app.config['DATABASE'] = tempfile.mkstemp()
        heutagogy.app.config['TESTING'] = True
        self.app = heutagogy.app.test_client()
        with heutagogy.app.app_context():
            heutagogy.persistence.initialize()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(heutagogy.app.config['DATABASE'])

    def test_hello_world(self):
        res = self.app.get('/')
        assert b'Hello, world!' == res.data

if __name__ == '__main__':
    unittest.main()
