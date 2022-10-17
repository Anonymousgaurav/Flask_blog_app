from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Gaurav Kumar</h1>"


@app.route("/about")
def aboutPage():
    return "<h1>About Page</h1>"
