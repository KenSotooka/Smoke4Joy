from flask import Flask,request, render_template
from typing import NewType
import requests
from requests.api import post

def weightcalc(asbestos, alcohol, tobacco, UV, radon=1, Formaldehyde=1, Meat=1, genes=1):
    asbestos = int(asbestos)
    alcohol = int(alcohol)
    tobacco = int(tobacco)
    UV = int(UV)

    return (asbestos + alcohol + tobacco + UV)

#just checking name probably the user
app = Flask(__name__)




@app.route("/")
def home():
    return render_template("home.html")
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/quiz", methods = ["POST"])
def quizsearch():
    data = request.form
    print(data["likert"],data["likert1"],data["likert2"],data["likert3"])
    data1 = (weightcalc(data["likert"],data["likert1"],data["likert2"],data["likert3"]))

    return render_template("quiz.html", data1 = data1)
@app.route("/slide")
def slideshow(): 
    return render_template("slideshow.html")

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80, debug=True)