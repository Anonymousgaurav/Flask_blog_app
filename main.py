from flask import Flask, render_template

from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '0d21cae2ddd5726f9eeb63221715fd74'

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


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)
