from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt




application=app = Flask(__name__)
app.config['SECRET_KEY'] = 'ad66d90a56b675248acb31307cca3cc8017fc2ac'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Admin.db"
app.config['SQLAlCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)


import routes

