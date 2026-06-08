from flask import Blueprint, render_template, request, url_for, redirect, request
from flask_login import login_required, current_user
from app.forms.gym_form import GymSearchForm
from app.services.gym_service import GymService
from app.models.saved_gym import SavedGym
from app import db


gym = Blueprint("gym", __name__)

@gym.route("/")
def home():
    return render_template("home.html")

@gym.route("/dashboard")
@login_required 
def dashboard():
    username = current_user.username
    return render_template("user_dashboard.html", username=username)

@gym.route("/search", methods=['GET', 'POST'])
@login_required
def search():
    print("SEARCH ROUTE HIT!")
    print(request.method)
    form = GymSearchForm()
    gyms = []
    error_message= None
    if form.validate_on_submit():
        print("VALIDATION PASSED!")
        use_current_location = form.use_current_location.data
        location = form.location.data
        max_distance = form.max_distance.data
        latitude = form.latitude.data
        longitude = form.longitude.data
    
        gyms = GymService.search_gyms(use_current_location=use_current_location, location=location, max_distance=max_distance, latitude=latitude, longitude=longitude)
        if not gyms:
            error_message = "No gym found. Try a different location or increase distance!"

    elif form.is_submitted():
        print(form.errors)
      
    return render_template("search.html", form=form, gyms=gyms, error_message=error_message)

@gym.route("/save-gym", methods=["POST"])
@login_required
def save_gym():
    gym_name = request.form.get("gym_name")
    gym_address = request.form.get("gym_address")
    gym_rating = request.form.get("gym_rating")
    gym_distance = request.form.get("gym_distance")
    saved_gym = SavedGym(user_id=current_user.id, gym_name=gym_name, gym_address=gym_address, gym_rating=float(gym_rating), gym_distance=float(gym_distance))
    db.session.add(saved_gym)
    db.session.commit()
    return redirect(url_for("gym.search"))

@gym.route("/saved-gyms")
@login_required
def saved_gyms():
    gyms = SavedGym.query.filter_by(user_id=current_user.id).all()
    return render_template("saved_gyms.html", gyms=gyms)

