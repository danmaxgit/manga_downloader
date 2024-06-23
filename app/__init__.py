import os

from flask            import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt     import Bcrypt
from flask_login      import LoginManager

#Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object('app.config.Config')

db = SQLAlchemy(app) # flask-sqlalchemy

bcrypt = Bcrypt(app)

lm = LoginManager()
lm.init_app(app)

# Import routing, models and Start the App
from app import views, models