from datetime import datetime

from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '0d21cae2ddd5726f9eeb63221715fd74'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(20), unique=True, nullable=False)
    userEmail = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    # magic methods
    def __repr__(self):
        return f"User('{self.userName},{self.userEmail},{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.userName},{self.date_posted}')"


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
def home():
    return render_template('home.html', posts=userPosts)


@app.route("/about")
def aboutPage():
    return render_template('about.html', aboutTitle='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # adding flash message to show the toast message
        flash(f'Account Created Succesfully for {form.username.data}', 'success')
        # return to home page after successful operation.
        return redirect(url_for("home"))
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for("home"))
        else:
            flash('Login Unsuccessful Please Check Username and Password', "danger")
    return render_template('login.html', title="Login", form=form)
