from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)

app.config['SECRET_KEY'] = "shhh_its_secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/hello')
def hello_page():
    return render_template("hello.html")

@app.route("/lucky")
def show_lucky_num():
    num = randint(1,10)
    return render_template("lucky.html", lucky_num = num)

@app.route("/form")
def show_form():
    return render_template("form.html")

COMPLIMENTS = ["cool", "clever", "rad", "a star", "stellar"]

@app.route("/greet")
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=nice_thing)

@app.route("/spell/<word>")
def spell_word(word):
    caps_word = word.upper()
    return render_template("spell_word.html", word=caps_word)

@app.route("/form-2")
def show_form_2():
    return render_template("form_2.html")

@app.route("/greet-2")
def get_greeting_2():
    username = request.args["username"]
    wants_comps = request.args.get("wants_comps")
    nice_things = sample(COMPLIMENTS, 3)
    return render_template("greet_2.html", username=username, wants_comps=wants_comps, compliments=nice_things)


