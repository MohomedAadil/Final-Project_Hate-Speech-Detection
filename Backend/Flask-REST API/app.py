import keras
import pickle
import pymysql
from flask import Flask

app = Flask(__name__)

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
