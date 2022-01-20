from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home_page():
    html="""
    <html>
        <body>
            <h1>Home Page</h1>
            <p>Welcome to my simple app!</p>
            <a href='/hello'>Go to Hello Page</a>
        </body>
    </html>
    """
    return html

@app.route('/hello')
def say_hello():
    """Returns "hello" greeting"""
    html = "<html><body><h1>Hello</h1></body></html>"
    return html

@app.route('/goodbye')
def say_bye():
    return "GOODBYE!!!"

@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search results for: {term}</h1> <p>Sorting by: {sort}</p>"

# @app.route('/post', methods=["POST"])
# def post_demo():
#    return "You made a post request"

# @app.route('/post', methods=["GET"])
# def get_demo():
#     return "You made a get request"    

@app.route("/add-comment")
def add_comment_form():
    """Show form for adding a comment."""

    return """
    <h1>Add comment</h1>
    <form method="POST">
        <input type="text" placeholder="comment" name="comment">
        <input type="text" placeholder="username" name="username"/>
        <button>Submit</button>
    </form>
    """

@app.route("/add-comment", methods=["POST"])
def add_comment():
    """Handle adding comment."""

    comment = request.form["comment"]
    user = request.form["username"]

    # TODO: save that into a database!

    return f'<h1>Received "{comment}" from {user}.</h1>'

@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>Browsering the {subreddit} Subreddit</h1>"

POSTS = {
    1: "I like chicken tenders",
    2: "I hate mayo",
    3: "rainbows are veyr gay",
    4: "hahahhahaha",
}

@app.route('/posts/<int:id>')
def find_post(id):
    """displays the post that matches the passed in id"""
    post = POSTS.get(id, "post not found")
    return f"<p>{post}</p>"