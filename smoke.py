from flask import Flask,request, render_template
from typing import NewType
import requests
from requests.api import post

def weightcalc(asbestos, alcohol, tobacco, UV, radon, Formaldehyde=3, Benzene=1, Arsenic=1, Diesel=1, Aflatoxins=1, radiation=1, Benzidine=1):
    asbestos = int(asbestos)
    alcohol = int(alcohol)
    tobacco = int(tobacco)
    UV = int(UV)
    radon = int(radon)
    Formaldehyde = int(Formaldehyde)
    Benzene = int(Benzene)
    Arsenic = int(Arsenic)
    Diesel = int(Diesel)
    Aflatoxins = int(Aflatoxins)
    radiation = int(radiation)
    Benzidine = int(Benzidine)

    return (5*asbestos + 3*alcohol + 5*tobacco + 4*UV + 5*radon + 3*Formaldehyde + 4*Benzene + 5*Arsenic+ 4*Diesel + 5*Aflatoxins + 4*radiation + 5*Benzidine)

#just checking name probably the user
app = Flask(__name__)

#Asbestos - 5
#Alcohol - 3
#Tobacco smoke - 5
#UV radiation - 4
#Radon - 5
#Formaldehyde - 3
#Benzene - 4
#Arsenic - 5
#Diesel engine exhaust - 4
#Aflatoxins - 5 
#Ionizing radiation - 4
#Benzidine - 5




@app.route("/")
def home():
    return render_template("home.html")
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/quiz", methods = ["POST"])
def quizsearch():
    try:
        data = request.form
        print(data["likert"],data["likert1"],data["likert2"],data["likert3"])
        data1 = (weightcalc(data["likert"],data["likert1"],data["likert2"],data["likert3"],data["likert4"],data["likert5"],data["likert6"],data["likert7"],data["likert8"],data["likert9"],data["likert10"],data["likert11"]))
    except KeyError:
        data1 = "fill in all the boxes!!"
    return render_template("quiz.html", data1 = data1)
@app.route("/slide")
def slideshow(): 
    return render_template("slideshow.html")

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80, debug=True)