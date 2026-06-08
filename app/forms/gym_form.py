from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, HiddenField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Optional 

class GymSearchForm(FlaskForm):
    use_current_location = BooleanField("Use my current location", default=True)
    location = StringField("Search another city", validators=[Optional()])
    max_distance = IntegerField("Maximum Distance(Miles)", validators=[DataRequired(),NumberRange(min=1, max=50)])
    latitude = HiddenField()
    longitude = HiddenField()
    submit = SubmitField("Search Gyms")
