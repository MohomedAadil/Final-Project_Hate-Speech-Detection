import keras
import re
import string
import nltk
import pickle
import pymysql
from keras.preprocessing import sequence
from nltk.stem import PorterStemmer
from flask import Flask, request, jsonify

app = Flask(__name__)

# Preprocessing functions
def clean_text(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text = " ".join(text)
    #text = [stemmer.stem(word) for word in text.split(' ')]
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
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# Load the model and tokenizer
load_model = keras.models.load_model("hate&abusive_model.h5")
with open('tokenizer.pickle', 'rb') as handle:
    load_tokenizer = pickle.load(handle)

if __name__ == '__main__':
    app.run()
