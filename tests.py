import unittest
import flask_file

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = flask_file.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        assert b'Hello World!' in rv.data

if __name__ == '__main__':
    unittest.main()