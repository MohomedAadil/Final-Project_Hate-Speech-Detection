// JavaScript code to interact with the Flask API
const postForm = document.getElementById('postForm');
const contentInput = document.getElementById('content');
const errorContainer = document.getElementById('errorContainer');
const postList = document.getElementById('postList');
const viewAllPostsButton = document.getElementById('viewAllPosts');

// Function to display error messages
function showError(message) {
    errorContainer.textContent = message;
}

// Function to fetch and display posts
async function fetchPosts() {
    try {
        const response = await fetch('http://localhost:5000/get_posts');
        const posts = await response.json();

        postList.innerHTML = '';

        posts.forEach(post => {
            const li = document.createElement('li');
            li.className = 'post-item';
            li.textContent = post.content;

            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Delete';
            deleteButton.addEventListener('click', () => deletePost(post.id));

            const updateButton = document.createElement('button');
            updateButton.textContent = 'Update';
            updateButton.addEventListener('click', () => updatePost(post.id, post.content));

            li.appendChild(deleteButton);
            li.appendChild(updateButton);
            postList.appendChild(li);
        });
    } catch (error) {
        console.error('Error fetching posts:', error);
    }
}

// Function to add a new post
async function addPost(content) {
    try {
        const response = await fetch('http://localhost:5000/add_post', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ content })
        });

        if (response.ok) {
            contentInput.value = '';
            errorContainer.textContent = '';
            fetchPosts();
        } else {
            // Check if the response contains JSON data
            const contentType = response.headers.get('content-type');
            if (contentType && contentType.includes('application/json')) {
                const errorData = await response.json();
                showError(errorData.error);
            } else {
                // Handle the case where the response is not in JSON format
                showError('An error occurred while adding the post.');
            }
        }
    } catch (error) {
        console.error('Error adding post:', error);
    }
}