import os

from flask            import Flask
from flask_sqlalchemy import SQLAlchemy
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object('app.config.Config')

db = SQLAlchemy  (app) # flask-sqlalchemy

with app.app_context():
    db.create_all()

# Import routing, models and Start the App
from app import views, models