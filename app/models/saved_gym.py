from app import db
from datetime import datetime

class SavedGym(db.Model):
    __tablename__ = "saved_gyms"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    gym_name = db.Column(db.String(150), nullable=False)
    gym_address = db.Column(db.String(225), nullable=False)
    gym_distance=db.Column(db.Float, nullable=True)
    gym_rating = db.Column(db.Float, nullable=True)
