from flask import render_template, redirect, url_for, jsonify, request
from app import app
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = set(["png", "jpg", "pdf", "gif"])

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods = ["GET", "POST"])
def uploadFile():
    if request.method == "POST":
        if "ourfile" not in request.files:
            return "error1"
        f = request.files["ourfile"]
        if f.filename == "":
            return redirect(url_for('home'))
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return "File uploaded"
    return redirect(url_for('home'))
