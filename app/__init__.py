from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = "you will never guess"
app.config.from_object(Config)

#initialisation of flask sqlalchemy and flask migrate module

db = SQLAlchemy(app)
migrate = Migrate(app,db)
login = LoginManager(app)
login.login_view='login'


from app import  routes , models
