import unittest
#import app
import json
from FlaskRestAPI.app import app

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

    def test_get_posts(self):
            # Simulate a GET request to retrieve posts
            response = self.app.get('/get_posts')
            # Check if the response status code is 200 (success)
            self.assertEqual(response.status_code, 200)
            # Check the response content for the expected data structure
            data = json.loads(response.data.decode('utf-8'))
            self.assertTrue(isinstance(data, list))
            # Add further checks to ensure the response contains the expected posts

    def test_update_post(self):
            # Simulate a POST request to add a new post
            response = self.app.post('/add_post', json={'content': 'Test post content'})
            # Check if the response status code is 200 (success)
            self.assertEqual(response.status_code, 200)
            # Retrieve the ID of the newly added post from the response data
            data = json.loads(response.data.decode('utf-8'))
            post_id = data['post_id']
            # Simulate a PUT request to update the post
            updated_content = 'Updated test post content'
            response = self.app.put(f'/update_post/{post_id}', json={'content': updated_content})
            # Check if the response status code is 200 (success)
            self.assertEqual(response.status_code, 200)
            # Check the response content for the expected message
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(data['message'], 'Post updated successfully')
            # Optionally, retrieve the updated post and check its content in the database

    def test_delete_post(self):
            # Simulate a POST request to add a new post
            response = self.app.post('/add_post', json={'content': 'Test post content'})
            # Check if the response status code is 200 (success)
            self.assertEqual(response.status_code, 200)
            # Retrieve the ID of the newly added post from the response data
            data = json.loads(response.data.decode('utf-8'))
            post_id = data['post_id']
            # Simulate a DELETE request to delete the post
            response = self.app.delete(f'/delete_post/{post_id}')
            # Check if the response status code is 200 (success)
            self.assertEqual(response.status_code, 200)
            # Check the response content for the expected message
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(data['message'], 'Post deleted successfully')

if __name__ == '__main__':
    unittest.main()
