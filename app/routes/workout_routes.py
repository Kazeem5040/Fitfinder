from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required, current_user
from app.forms.workout_form import WorkoutForm
from app.models.workout import Workout
from app import db
from app.services.workout_ai_service import WorkoutAIService
import markdown

workout = Blueprint("workout", __name__)

@workout.route("/workout", methods=["GET", "POST"])
@login_required
def generate_workout():

    form = WorkoutForm()
    workout_html = None
    generated_workout = None

    if form.validate_on_submit():

        generated_workout = WorkoutAIService.generate_workout(
            energy_level=form.energy_level.data,
            body_part=form.body_part.data,
            goal=form.goal.data,
            workout_time=form.workout_time.data, gym_experience=form.gym_experience.data, 
            height=form.height.data,weight=form.weight.data, 
            fitness_level=form.fitness_level.data)
        new_workout = Workout(user_id=current_user.id, body_part=form.body_part.data, energy_level=form.energy_level.data, 
                              workout_text=generated_workout)
        db.session.add(new_workout)
        db.session.commit()
        workout_html = markdown.markdown(generated_workout)        

    return render_template("workout.html",form=form,workout=generated_workout, workout_html=workout_html)


@workout.route("/workout-history")
@login_required
def workout_history():
    workouts= Workout.query.filter_by(user_id=current_user.id).order_by(Workout.created_at.desc()).all()
    return render_template("workout_history.html", workouts=workouts)

@workout.route("/workout/<int:workout_id>")
@login_required
def view_workout(workout_id):
    workout_record = Workout.query.get_or_404(workout_id)
    workout_html = markdown.markdown(workout_record.workout_text)
    return render_template("view_workout.html", workout=workout_record, workout_html=workout_html)

@workout.route("/delete-workout/<int:workout_id>")
@login_required
def delete_workout(workout_id):
    workout_record = Workout.query.get_or_404(workout_id)
    db.session.delete(workout_record)
    db.session.commit()
    return redirect(url_for("workout.workout_history"))

