from flask import Blueprint, flash, render_template, redirect, url_for, request
from app.forms.register_form import RegisterForm
from app.forms.login_form import LoginForm
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app import db

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == "POST":
        print(form.validate_on_submit())
        print(form.errors)
    if form.validate_on_submit():
        existing_username = User.query.filter_by(username=form.username.data).first()
        if existing_username:
            flash("Username already exists. Please log in!")
            return render_template("register.html", form=form)
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Email already exists. Please log in!")
            return render_template("register.html", form=form)
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully!")
        login_user(new_user)
        return redirect(url_for("gym.dashboard"))

    return render_template("register.html", form=form)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.errors)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for("gym.dashboard"))
        else:
            flash("Invalid email or password. Please retry!")
    return render_template("login.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out!")
    return redirect(url_for("auth.login"))

