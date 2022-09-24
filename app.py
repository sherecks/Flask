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


@app.route("/struc")
def struc():

    movies = [   
        "BATMAN - Cavaleiros das Trevas",
        "Pulp Fiction",
        "Casa do Dragão"
    ]

    return render_template("data-struc.html", movies=movies)