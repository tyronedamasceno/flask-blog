from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return "<h1>Home page</h1>"


@app.route("/about")
def about():
    return "<h1>About page</h1>"
