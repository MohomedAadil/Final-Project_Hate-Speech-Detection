import unittest
import app
import json
#from Backend.api.flask_app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


if __name__ == '__main__':
    unittest.main()
