# Import the function to be tested
import pytest
import json
from FlaskRestAPI.app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_post(client):
    """Test the /add_post endpoint."""
    data = {
        'content': 'This is a test post.'
    }
    response = client.post('/add_post', json=data)
    assert response.status_code == 200
    assert 'Post added successfully' in response.get_json()['message']

def test_get_posts(client):
    """Test the /get_posts endpoint."""
    response = client.get('/get_posts')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_update_post(client):
    """Test the /update_post/<int:post_id> endpoint."""
    data = {
        'content': 'Updated post content.'
    }
    response = client.put('/update_post/1', json=data)
    assert response.status_code == 200
    assert 'Post updated successfully' in response.get_json()['message']

def test_delete_post(client):
    """Test the /delete_post/<int:post_id> endpoint."""
    response = client.delete('/delete_post/1')
    assert response.status_code == 200
    assert 'Post deleted successfully' in response.get_json()['message']

if __name__ == '__main__':
    client.main()