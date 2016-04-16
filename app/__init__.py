from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, static_url_path='/static')

app.secret_key = 'carloparvlove'

app.config.from_object('config')
login_manager = LoginManager()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager.init_app(app)


from app import views, models

from models import Employers

login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return models.Employers.query.filter(models.Employers.employer_id == int(user_id)).first()
