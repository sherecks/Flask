from unicodedata import name
from flask import Flask, render_template

app=Flask(__name__)


@app.route("/joao")
def hello():

    name="João Pedro"
    #adição
    idade1 = 21
    idade2= 19

    kwargs = {
        "name": name,
        "idade1": idade1,
        "idade2": idade2
    }

    return render_template(
        "jinja_intro.html", **kwargs
        )