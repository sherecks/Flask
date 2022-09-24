from unicodedata import name
from flask import Flask, render_template

app=Flask(__name__)


@app.route("/")
def hello():
    return render_template(
        "jinja_intro.html", name="João Pedro", template_name="Jinja2"
        )



@app.route("/pietra")
def pietra():
    return render_template(
        "jinja2_intro.html", name="Pietra Pereria Nunes", template_name="Jinja2"
        )