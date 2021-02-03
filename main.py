from flask import Flask
from config.Config import Config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt


app = Flask(__name__)
config = Config()
app.config.from_object(config)

db = SQLAlchemy(app)

from controller.UserProfile import users
app.register_blueprint(users, url_prefix="/user-profile")
