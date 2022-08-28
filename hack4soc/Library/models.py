from random import randint
from sqlalchemy import null
from Library import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from Library import login_manager
from wtforms.validators import ValidationError

from sqlalchemy import Column, Integer, String, ForeignKey, Date

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    

    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(length = 30), nullable = False, unique = True)
    password_hash = db.Column(db.String(length = 300), nullable = False)    
    recent = db.Column(db.Integer(), nullable=False)
    
    

    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)    

    def __repr__(self):
        return "A user with username : %s" % (self.username)


class book_table(db.Model, UserMixin):    

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(length=100), nullable=False)
    genre = db.Column(db.String(length=50), nullable=False)
    level = db.Column(db.String(length=50), nullable=False)    
    link = db.Column(db.String(length=1000), nullable=False)
    description=db.Column(db.String(length=1500), nullable=False)
    image=db.Column(db.String(length=150), nullable=False)
    author=db.Column(db.String(length=30), nullable=False)
        

    def __repr__(self):
        return "the table containing books"
