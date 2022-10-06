from unicodedata import name
from flask import Flask, render_template

app=Flask(__name__)



class Galileanmoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


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


    car = {
        "marca": "Volkswagen",
        "modelo": "Fusca",
        "ano": "1979",
    }

    moons = Galileanmoons("Io", "Europa", "Ganymede", "Calisto")

    kwargs = {
        "movies": movies,
        "car": car,
        "moons": moons
    }


    return render_template("data-struc.html", **kwargs)


@app.route("/home")
def todo():

    
    todos = [
        ("Pegar comida", False),
        ("Aprender a programar", True)
    ]

    return render_template("home.html",  todos=todos)