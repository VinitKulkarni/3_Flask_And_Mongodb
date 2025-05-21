from flask import Flask, request, render_template
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)
db = client.test
collection = db['my-collection']

app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('name')
    password = request.form.get('password')

    # validation for empty textbox
    if not username or not password:
        return render_template('index.html', error="Both username and password are required.")

    # validation for password length
    if len(password) < 8 or len(password) > 16:
        return render_template('index.html', error="Password must be between 8 and 16 characters.")


    form_data = dict(request.form)
    collection.insert_one(form_data)
    return "Data submission successful"
    
if __name__ == "__main__":
    app.run(debug=True)
