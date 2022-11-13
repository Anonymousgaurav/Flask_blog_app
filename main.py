from flask import Flask, render_template, flash, redirect, url_for

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


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)
