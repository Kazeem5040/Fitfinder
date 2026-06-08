from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Regexp, Length


class RegisterForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[
            DataRequired(), Length(min=8, max=20),
            Regexp(
                r"^[A-Za-z][A-Za-z0-9._]{2,24}$",
                message="Username must start with a letter and only use letters, numbers, dots, or underscores."
            )
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),  Length(min=8, max=20, message="Password must be between 8 to 20 characters!")])

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Passwords must match"
            )
        ]
    )

    submit = SubmitField("Create Account")