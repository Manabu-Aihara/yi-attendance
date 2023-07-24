from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Environment

from config import Config
# from database import init_db

app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'

jinja_env = Environment(extensions=['jinja2.ext.i18n'])
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

db = SQLAlchemy(app)
# db = db.init_app(app)
# @app.before_first_request
# def create_database():
#      db.create_all()

from src.routes import app
from src import user_models