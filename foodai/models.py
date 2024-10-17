from datetime import datetime
from foodai import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(125), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    lessons = db.relationship("Lesson", backref="author", lazy=True)
    def __repr__(self):
        return f"User('{self.fname}', '{self.lname}', '{self.username}', '{self.email}', '{self.image_file}')"

