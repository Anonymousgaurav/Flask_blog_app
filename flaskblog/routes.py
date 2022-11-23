from flask import render_template, url_for, flash, redirect

from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm

userPosts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
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
        flash(f'Account Created Successfully for {form.username.data}', 'success')
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
