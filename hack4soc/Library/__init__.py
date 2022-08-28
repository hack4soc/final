from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

secret_key = os.urandom(32)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:bablu2002@localhost/library'
app.config['SECRET_KEY'] = secret_key

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from Library import routes