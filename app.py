from flask import Flask
import os

UPLOAD_FOLDER = os.path.abspath("content/")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from routes import routes