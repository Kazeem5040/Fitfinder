import os

from dotenv import load_dotenv


load_dotenv()


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = (os.getenv("DATABASE_URL"))

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    OPEN_API_KEY = os.getenv("OPEN_API_KEY")