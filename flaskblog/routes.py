from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, current_user, login_required

from flaskblog import bcrypt, db, app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(userName=form.username.data, userEmail=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        # adding flash message to show the toast message
        flash(f'Account Created Successfully', 'success')
        # return to home page after successful operation.
        return redirect(url_for("login"))
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(userEmail=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Login Successful', "success")
            print(next_page)
            return redirect(next_page) if next_page else redirect(url_for('home'))
        flash('Login Unsuccessful Please Check Username and Password', "danger")
    return render_template('login.html', title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/account")
@login_required
def account():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    print(image_file)
    return render_template('account.html', title="Account", image_file=image_file)
