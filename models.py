from datetime import datetime 
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker



class StudentModel(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(120), nullable=False)
    student_email = db.Column(db.String(120), unique=True, nullable=False)
    student_password = db.Column(db.String(120), nullable=False)
    def __init__(self, data):
        self.student_name = data.get('student_name')
        self.student_email = data.get('student_email')
        self.student_password = self.__generate_hash(data.get('student_password'))
    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self, data):
        for key, item in data.items():
            if key == 'student_password': 
                self.student_password = self.__generate_hash(value) 
            setattr(self, key, item)
    
        db.session.commit()
    def __generate_hash(self, student_password):
        return bcrypt.generate_password_hash(student_password, rounds=10).decode("utf-8")
    def check_hash(self, student_password):
        return bcrypt.check_password_hash(self.student_password, student_password)
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def get_all_users():
        return StudentModel.query.all()
    def get_one_user(id):
        return StudentModel.query.get(id)
class AdminModel(db.Model):
    __tablename__ = 'students'
    admin_id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(128), nullable=False)
    admin_email = db.Column(db.String(128), unique=True, nullable=False)
    admin_password = db.Column(db.String(128), nullable=True)
    posts = db.relationship('Post',backref='author',lazy=True)
    def __init__(self, data):
        self.admin_name = data.get('admin_name')
        self.admin_email = data.get('admin_email')
        self.admin_password = self.__generate_hash(data.get('admin_password'))
    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self, data):
        for key, item in data.items():
            if key == 'admin_password': 
                self.student_password = self.__generate_hash(value) 
            setattr(self, key, item)
    
        db.session.commit()
    def __generate_hash(self, admin_password):
        return bcrypt.generate_password_hash(admin_password, rounds=10).decode("utf-8")
    def check_hash(self, student_password):
        return bcrypt.check_password_hash(self.admin_password, admin_password)
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def get_all_users():
        return AdminModel.query.all()
    def get_one_user(id):
        return AdminModel.query.get(id)

class Post(db.Model):
     post_id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(128), nullable=False)
     date_posted = db.Column(db.DateTime, nullable = False , default = datetime.utcnow)
     content = db.Column(db.Text , nullable = False)
     user_id = db.Column(db.Integer, db.ForeignKey('user_id'),nullable=False)

