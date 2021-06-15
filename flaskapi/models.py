
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker,relationship, backref
from flaskapi import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime



class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(128), nullable=False,unique=True)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    user_password = db.Column(db.String(120), nullable=False,unique=True)
   
    requests = db.relationship('RequestModel',backref='request',lazy=True)
    role = db.Column(db.String(120), nullable=False)
    def set_password(self, password):
        self.user_password = generate_password_hash(password)
    def check_hash(self, password):
        return check_password_hash(self.user_password,password)
    def __repr__(self):
        return '<User {}>'.format(self.user_name)
@login.user_loader
def load_user(id):
    return UserModel.query.get(int(id))

    
class Post(db.Model):
     __tablename__ = 'posts'
     post_id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(128), nullable=False)
     date_posted = db.Column(db.DateTime, default=datetime.utcnow())
     content = db.Column(db.Text , nullable = False)
     

class RequestModel(db.Model):
    __tablename__ = 'requests'
    r_id = db.Column(db.Integer, primary_key=True)
    requestedPerson_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    students_id = db.Column(db.String(),unique=True)
    firstname = db.Column(db.String(), nullable = False)
    lastname = db.Column(db.String(), nullable = False)
    gender = db.Column(db.String(), nullable = False)
    email = db.Column(db.String(), nullable = False,unique=True)
    institution =  db.Column(db.String(), nullable = False)
    department = db.Column(db.String(), nullable = False)
    year = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.String(), nullable = False)
    state = db.Column(db.String(), nullable = False)
    city = db.Column(db.String(), nullable = False)
    sub_city = db.Column(db.String(), nullable = False)
    woreda = db.Column(db.Integer(), nullable = False)
    accepted = db.relationship('AcceptedModel',backref='accepted',lazy=True)



class AcceptedModel(db.Model):
    __tablename__ = 'accepted'    
    a_id = db.Column(db.Integer, primary_key=True)
    requestedPerson_id = db.Column(db.Integer, db.ForeignKey('requests.r_id'),unique=True)
    status = db.Column(db.Boolean(), nullable = False)
    dormitoryPlace = db.Column(db.String, nullable = False,default="FBE")
    blockNumber = db.Column(db.Integer, nullable = False,default=0)
    dormNumber = db.Column(db.Integer, nullable = False,default=0)
    




 
