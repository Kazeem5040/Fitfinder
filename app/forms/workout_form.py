from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class WorkoutForm(FlaskForm):

    energy_level = SelectField("Energy Level",choices=[("low", "Low"),("medium", "Medium"),("high", "High")],
        validators=[DataRequired()])

    body_part = SelectField("Body Part",choices=[("chest", "Chest"),("back", "Back"),("shoulders", "Shoulders"),("biceps", "Biceps"),
("triceps", "Triceps"),("legs", "Legs"),("core", "Core"),("full body", "Full Body")],validators=[DataRequired()])

    goal = SelectField("Workout Goal",choices=[("build muscle", "Build Muscle"),("lose weight", "Lose Weight"),
            ("strength", "Strength"),("general fitness", "General Fitness")],validators=[DataRequired()])

    workout_time = SelectField("Available Time",choices=[("20", "20 Minutes"),("25", "25 Minutes"),("30", "30 Minutes"),("45", "45 Minutes")],
        validators=[DataRequired()]
    )
    weight = IntegerField("Weight(lbs)", validators=[DataRequired()])
    height = IntegerField("Height(ft)", validators=[DataRequired()])
    fitness_level = SelectField("Fitness Level", choices=[("beginner", "Beginner"), ("intermediate", "Intermediate"), ("advanced", "Advanced")], validators=[DataRequired()])
    gym_experience = SelectField("Gym Experience", choices=[("0-6 months", "0-6 months"), ("6-12 months", "6-12 months"), ("1-3 years", "1-3 years"), ("3+ years", "3+ years")], validators=[DataRequired()])

    submit = SubmitField("Generate Workout")