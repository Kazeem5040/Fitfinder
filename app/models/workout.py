from app import db
from datetime import datetime
from sqlalchemy import DateTime

class Workout(db.Model):
    __tablename__ = "workouts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    body_part = db.Column(db.String(50), nullable=False)
    energy_level = db.Column(db.String(50), nullable=False)
    workout_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(DateTime, default=datetime.utcnow)