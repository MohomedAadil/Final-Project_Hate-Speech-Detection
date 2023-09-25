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