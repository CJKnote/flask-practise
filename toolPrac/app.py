from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)

app.config['SECRET_KEY'] = "shhh_its_secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

MOVIES = {"Song of the Sea", "Chicken Run", "Encanto"}


@app.route('/')
def home_page():
    """shows home page"""
    return render_template('home.html')

@app.route('/old-home-page')
def redirect_to_home():
    """redirects to new home page"""
    flash("That pages has moved. This is our new page.")
    return redirect('/')

@app.route("/movies")
def show_all_movies():
    """how list of all movies in fake db"""
    return render_template("movies.html", movies=MOVIES)

# @app.route("/movies/new", methods=["POST"])
# def add_movie():
#     title = request.form['title']

#     #add to pretend DB
#     MOVIES.append(title)
#     return render_template("movies.html", movies=MOVIES)
#     #we get a confirm form resubmit this way


@app.route("/movies/new", methods=["POST"])
def add_movie():
    title = request.form['title']

    #add to pretend DB
    if title in MOVIES:
        flash('Movie already exists', "error")
    else:
        MOVIES.add(title)
        flash("created your movie!", "success")

    return redirect("/movies") #this prevents us getting the form resubmit
    #no data being sent with the request