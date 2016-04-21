from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_url_path='/static')
bcrypt = Bcrypt(app)

app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view =  "signin"

@login_manager.user_loader
def load_user(userid):
    return models.Employers.query.filter(models.Employers.employer_id==userid).first()

