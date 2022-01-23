from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = "wellwellwell"
debug = DebugToolbarExtension(app)



@app.route('/')
def madlibs_form():
    """makes a page to fill out the story prompts"""
    prompts = story.prompts
    return render_template('question_form.html', prompts=prompts)

@app.route('/story')
def make_story():
    """generates the madlibs story using entered prompts"""
    finished_story = story.generate(request.args)
    return render_template('story.html', text=finished_story)