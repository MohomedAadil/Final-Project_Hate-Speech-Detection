import unittest
#import app
import json
from Backend.FlaskRestAPI.api.flask_app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        # Clean up any test data or resources if necessary
        pass

    def test_add_post(self):
        # Simulate a POST request to add a new post
        response = self.app.post('/add_post', json={'content': 'Test post content'})
        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)
        # Check the response content for the expected message
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['message'], 'Post added successfully')


if __name__ == '__main__':
    unittest.main()
