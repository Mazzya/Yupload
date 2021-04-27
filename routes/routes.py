from flask import render_template, redirect, url_for, jsonify, request, send_from_directory
from app import app
from werkzeug.utils import secure_filename
import os
from io import open

ALLOWED_EXTENSIONS = set(["png", "jpg", "pdf", "gif", "PNG", "jpeg"])

def allowed_file(filename):
    """ Check the extension of the files to upload """
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS

@app.errorhandler(404)
def pageNotFound(error):
    return render_template("pageNotFound.html")

@app.route("/")
def home():
    return render_template("index.html", files=showFiles())

@app.route("/about")
def aboutUs():
    """ About us page """
    return render_template("about.html")
    
@app.route("/upload", methods = ["GET", "POST"])
def uploadFile():
    """ Main function for uploading files """
    if request.method == "POST":
        if "ourfile" not in request.files:
            return "error1"
        f = request.files["ourfile"]
        if f.filename == "":
            return redirect(url_for('home'))
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for('home'))
    return redirect(url_for('home'))

# Return files
@app.route("/uploads/<filename>")
def getFile(filename):
    """ Get files from directory 'content' """
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



def showFiles():
    """ This function shows the files that exist in the directory """
    path = "./content/"
    dirs = os.listdir(path)
    files = [file for file in dirs]
    return files
