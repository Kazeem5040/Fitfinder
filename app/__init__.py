from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "myflippinghappyfitfinder"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fitfinder.db"

    db.init_app(app)
    login_manager.init_app(app)

    from app.routes.gym_routes import gym
    from app.routes.auth_routes import auth
    from app.routes.workout_routes import workout

    from app.models.user import User

    app.register_blueprint(gym)
    app.register_blueprint(auth)
    app.register_blueprint(workout)

    with app.app_context():
        db.create_all()
    return app
