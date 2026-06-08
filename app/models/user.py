from app import db
from flask_login import UserMixin
from app import login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(300), nullable = False)
    password_hash = db.Column(db.String(255), nullable=False)
    saved_gym = db.relationship("SavedGym", backref="user", lazy=True)

@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))

