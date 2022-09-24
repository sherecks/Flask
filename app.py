from unicodedata import name
from flask import Flask, render_template

app=Flask(__name__)


@app.route("/joao")
def hello():

    #addition
    idade1 = 21
    idade2= 19

    return render_template(
        "jinja_intro.html", name="João Pedro", idade1="21", idade2="19"
        )



@app.route("/pietra")
def pietra():

    #addition
    idade3 = 19
    idade4= 21

    return render_template(
        "jinja2_intro.html", name="Pietra Pereria Nunes", idade3="19", idade4="21"
        )