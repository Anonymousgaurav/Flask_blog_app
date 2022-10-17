from flask import Flask, render_template

app = Flask(__name__)

userPosts = [
    {
        'author': 'Gaurav Kumar',
        'title': 'Nastrodamaus',
        'content': "Future predictions",
        "date_posted": "14th August"
    },
    {
        'author': 'Sourav Kumar',
        'title': 'Money Making',
        'content': "How to make money",
        "date_posted": "22th May"
    },

]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=userPosts)


@app.route("/about")
def aboutPage():
    return render_template('about.html', aboutTitle='About')
