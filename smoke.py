from flask import Flask,request, render_template
from typing import NewType
import requests
from requests.api import post

#just checking name probably the user
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/slide")
def slideshow():
    return render_template("slideshow.html")

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80, debug=True)