import keras
import re
import string
import nltk
import pickle
import pymysql
import emoji
from keras.preprocessing import sequence
from nltk.stem import PorterStemmer
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

# Preprocessing functions
def clean_text(text):
    text = str(text).lower()
    text = emoji.demojize(text)
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text = " ".join(text)
    text = " ".join(text.split())
    return text

# Initialize the Porter Stemmer
nltk.download('punkt')
stemmer = PorterStemmer()

# Define the stopword list and stemmer (you should import these)
stopword = []
stemmer = None

# MySQL Database Configuration
db_host = 'localhost'
db_user = 'root'
db_password = 'root'
db_name = 'textdb'

# Initialize the database connection
db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
cursor = db.cursor()

# Load the model and tokenizer
load_model = keras.models.load_model("hate&abusive_model.h5")
with open('tokenizer.pickle', 'rb') as handle:
    load_tokenizer = pickle.load(handle)

@app.route('/add_post', methods=['POST'])
def add_post():
    try:
        content = request.json.get('content')
        cleaned_text = clean_text(content)

        # Use a hate speech detection model
        seq = load_tokenizer.texts_to_sequences([cleaned_text])
        padded = sequence.pad_sequences(seq, maxlen=300)
        pred = load_model.predict(padded)

        if pred <= 0.5:  # You can adjust the threshold as needed
            # If it's not hate speech, add the post to the database
            sql = "INSERT INTO posts (content) VALUES (%s)"
            cursor.execute(sql, (content,))
            db.commit()
            return jsonify({'message': 'Post added successfully'}), 200
        else:
            return jsonify({'error': 'Hate speech detected'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_posts', methods=['GET'])
def get_posts():
    try:
        sql = "SELECT * FROM posts"
        cursor.execute(sql)
        posts = cursor.fetchall()
        post_list = [{'id': post[0], 'content': post[1]} for post in posts]
        return jsonify(post_list), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/update_post/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    try:
        content = request.json.get('content')
        cleaned_text = clean_text(content)

        # Use a hate speech detection model
        seq = load_tokenizer.texts_to_sequences([cleaned_text])
        padded = sequence.pad_sequences(seq, maxlen=300)
        pred = load_model.predict(padded)

        if pred <= 0.5:  # You can adjust the threshold as needed
            sql = "UPDATE posts SET content = %s WHERE id = %s"
            cursor.execute(sql, (content, post_id))
            db.commit()
            return jsonify({'message': 'Post updated successfully'}), 200
        else:
            return jsonify({'error': 'Hate speech detected'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete_post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        sql = "DELETE FROM posts WHERE id = %s"
        cursor.execute(sql, (post_id,))
        db.commit()
        return jsonify({'message': 'Post deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
