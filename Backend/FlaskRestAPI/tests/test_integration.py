import unittest
import json
from FlaskRestAPI.app import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_integration(self):
        # Test the entire integration flow:
        # 1. Add a post
        response = self.app.post('/add_post', json={'content': 'Test post content'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        post_id = data['post_id']

        # 2. Get the posts
        response = self.app.get('/get_posts')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertTrue(isinstance(data, list))
        self.assertTrue(any(post['id'] == post_id for post in data))

        # 3. Update the post
        updated_content = 'Updated test post content'
        response = self.app.put(f'/update_post/{post_id}', json={'content': updated_content})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['message'], 'Post updated successfully')

        # 4. Delete the post
        response = self.app.delete(f'/delete_post/{post_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['message'], 'Post deleted successfully')

if __name__ == '__main__':
    unittest.main()
