from flask import Flask,request, render_template
from typing import NewType
import requests
from requests.api import post

def weightcalc(asbestos, alcohol, tobacco, UV, radon, Formaldehyde, Meat, genes):
    return 51 + " high risk of cancer"

#just checking name probably the user
app = Flask(__name__)




@app.route("/")
def home():
    return render_template("home.html")
@app.route("/quiz", methods = ["POST"])
def quiz():

    return render_template("quiz.html")
@app.route("/slide")
def slideshow(): 
    return render_template("slideshow.html")

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80, debug=True)