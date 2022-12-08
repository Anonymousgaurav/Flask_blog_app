from datetime import datetime

from flask_login import UserMixin

from flaskblog import db, login_manager


# this is used to grab the user id if the data is stored in the cache / session
# You will need to provide a user_loader callback. This callback is used to reload the user object from the user ID
# stored in the session. It should take the str ID of a user, and return the corresponding user object.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
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
