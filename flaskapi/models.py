from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from flaskapi import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class StudentModel(UserMixin, db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(128), nullable=False)
    student_name = db.Column(db.String(120), nullable=False)
    student_email = db.Column(db.String(120), unique=True, nullable=False)
    student_password = db.Column(db.String(120), nullable=False)
    def set_password(self, password):
        self.student_password = generate_password_hash(password)
    def check_hash(self, password):
        return check_password_hash(self.student_password,password)
def load_user(id):
    return StudentModel.query.get(int(id))
class AdminModel(UserMixin,db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(128), nullable=False)
    admin_email = db.Column(db.String(128), unique=True, nullable=False)
    admin_password = db.Column(db.String(128), nullable=True)
    posts = db.relationship('Post',backref='author',lazy=True)
    def set_password(self, password):
        self.admin_password = generate_password_hash(password)
    def check_hash(self, password):
        return check_password_hash(self.admin_password,password)
def load_user(admin_id):
    return AdminModel.query.get(int(admin_id))
class Post(db.Model):
     __tablename__ = 'posts'
     post_id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(128), nullable=False)
    #  date_posted = db.Column(db.DateTime, nullable = False , default = DateTime.UtcNow())
     content = db.Column(db.Text , nullable = False)
     user_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'),nullable=False)

