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