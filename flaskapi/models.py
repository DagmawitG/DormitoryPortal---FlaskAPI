
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
    user_id = db.Column(db.String(128), nullable=False)
    user_name = db.Column(db.String(120), nullable=False)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    user_password = db.Column(db.String(120), nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True)
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
     date_posted = db.Column(db.DateTime, default=datetime.now)
     content = db.Column(db.Text , nullable = False)
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class RequestModel(db.Model):
    __tablename__ = 'requests'
    r_id = db.Column(db.Integer, primary_key=True)
    requestedPerson_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    students_id = db.Column(db.String())
    firstname = db.Column(db.String(), nullable = False)
    lastname = db.Column(db.String(), nullable = False)
    gender = db.Column(db.String(), nullable = False)
    email = db.Column(db.String(), nullable = False)
    institution =  db.Column(db.String(), nullable = False)
    department = db.Column(db.String(), nullable = False)
    year = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.String(), nullable = False)
    state = db.Column(db.String(), nullable = False)
    city = db.Column(db.String(), nullable = False)
    sub_city = db.Column(db.String(), nullable = False)
    woreda = db.Column(db.Integer(), nullable = False) 


class AcceptedModel(db.Model):
    __tablename__ = 'accepted'    
    a_id = db.Column(db.Integer, primary_key=True)
    requestedPerson_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    students_id = db.Column(db.String())
    firstname = db.Column(db.String(), nullable = False)
    lastname = db.Column(db.String(), nullable = False)
    gender = db.Column(db.String(), nullable = False)
    email = db.Column(db.String(), nullable = False)
    institution =  db.Column(db.String(), nullable = False)
    department = db.Column(db.String(), nullable = False)
    year = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.String(), nullable = False)
    state = db.Column(db.String(), nullable = False)
    city = db.Column(db.String(), nullable = False)
    sub_city = db.Column(db.String(), nullable = False)
    woreda = db.Column(db.Integer(), nullable = False) 




 
# class FiveKiloModel(db.Model):
#     __tablename__ = 'fiveKilo'
#     fk_id = db.Column(db.Integer, primary_key=True)
#     requestedPerson_id = db.Column(db.Integer, db.ForeignKey('students.s_id'),nullable=False)
#     students_id = db.Column(db.String())
#     firstname = db.Column(db.String(), nullable = False)
#     lastname = db.Column(db.String(), nullable = False)
#     gender = db.Column(db.String(), nullable = False)
#     email = db.Column(db.String(), nullable = False)
#     institution =  db.Column(db.String(), nullable = False)
#     department = db.Column(db.String(), nullable = False)
#     year = db.Column(db.Integer(), nullable = False)
#     description = db.Column(db.String(), nullable = False)
#     state = db.Column(db.String(), nullable = False)
#     city = db.Column(db.String(), nullable = False)
#     sub_city = db.Column(db.String(), nullable = False)
#     woreda = db.Column(db.String(), nullable = False) 
#     dormitory = db.Column(db.String(), nullable = False,default="Five Kilo Campus") 


# countFiveKiloMale = FiveKiloModel.query.filter_by(gender = 'M').count()
# countFiveKiloFemale  = FiveKiloModel.query.filter_by(gender = 'F').count()
# studentsPerDorm = 8
# totalDorm = 80

# def male():
    
#     if(count <= totalDorm):
#         for i in range(1,countFiveKiloMale):
#             for j in range(studentsPerDorm):
#                 return i
        
#     count += 1
   
        
# def female():
   
#     if(count <= totalDorm):
#         for i in range(1,countFiveKiloFemale):
#             for j in range(studentsPerDorm):
#                 return i
        
#     count += 1
   




# class MaleFiveKiloModel(db.Model):
#     __tablename__ = 'malefiveKilo'
#     mf_id = db.Column(db.Integer, primary_key=True)
#     requestedPerson_id = db.Column(db.Integer, db.ForeignKey('students.s_id'),nullable=False)
#     students_id = db.Column(db.String())
#     firstname = db.Column(db.String(), nullable = False)
#     lastname = db.Column(db.String(), nullable = False)
#     gender = db.Column(db.String(), nullable = False)
#     email = db.Column(db.String(), nullable = False)
#     institution =  db.Column(db.String(), nullable = False)
#     department = db.Column(db.String(), nullable = False)
#     year = db.Column(db.Integer(), nullable = False)
#     description = db.Column(db.String(), nullable = False)
#     state = db.Column(db.String(), nullable = False)
#     city = db.Column(db.String(), nullable = False)
#     sub_city = db.Column(db.String(), nullable = False)
#     woreda = db.Column(db.String(), nullable = False)
#     dormitory = db.Column(db.String(),  db.ForeignKey('fiveKilo.dormitory'))
#     blockNumber = db.Column(db.Integer(), default = 1)
#     dormNumber = db.Column(db.Integer(), default = male)


# class FemaleFiveKiloModel(db.Model):
#     __tablename__ = 'femalefiveKilo'
#     ff_id = db.Column(db.Integer, primary_key=True)
#     requestedPerson_id = db.Column(db.Integer, db.ForeignKey('students.s_id'),nullable=False)
#     students_id = db.Column(db.String())
#     firstname = db.Column(db.String(), nullable = False)
#     lastname = db.Column(db.String(), nullable = False)
#     gender = db.Column(db.String(), nullable = False)
#     email = db.Column(db.String(), nullable = False)
#     institution =  db.Column(db.String(), nullable = False)
#     department = db.Column(db.String(), nullable = False)
#     year = db.Column(db.Integer(), nullable = False)
#     description = db.Column(db.String(), nullable = False)
#     state = db.Column(db.String(), nullable = False)
#     city = db.Column(db.String(), nullable = False)
#     sub_city = db.Column(db.String(), nullable = False)
#     woreda = db.Column(db.String(), nullable = False) 
#     dormitory = db.Column(db.String(), db.ForeignKey('fiveKilo.dormitory'))
#     blockNumber = db.Column(db.Integer(), default = 2)
#     dormNumber = db.Column(db.Integer(), default = female)

 
   

# class SixKiloModel(db.Model):
#     __tablename__ = 'sixKilo'
#     sk_id = db.Column(db.Integer, primary_key=True)
#     requestedPerson_id = db.Column(db.Integer, db.ForeignKey('students.s_id'),nullable=False)
#     students_id = db.Column(db.String())
#     firstname = db.Column(db.String(), nullable = False)
#     lastname = db.Column(db.String(), nullable = False)
#     gender = db.Column(db.String(), nullable = False)
#     email = db.Column(db.String(), nullable = False)
#     institution =  db.Column(db.String(), nullable = False)
#     department = db.Column(db.String(), nullable = False)
#     year = db.Column(db.Integer(), nullable = False)
#     description = db.Column(db.String(), nullable = False)
#     state = db.Column(db.String(), nullable = False)
#     city = db.Column(db.String(), nullable = False)
#     sub_city = db.Column(db.String(), nullable = False)
#     woreda = db.Column(db.String(), nullable = False) 
#     dormitory = db.Column(db.String(), nullable = False,default="Six Kilo Campus") 

# class FBEKiloModel(db.Model):

#     __tablename__ = 'fbeKilo'
#     requestedPerson_id = db.Column(db.Integer, db.ForeignKey('students.s_id'),nullable=False)
#     fbe_id = db.Column(db.Integer, primary_key=True)
#     students_id = db.Column(db.String())
#     firstname = db.Column(db.String(), nullable = False)
#     lastname = db.Column(db.String(), nullable = False)
#     gender = db.Column(db.String(), nullable = False)
#     email = db.Column(db.String(), nullable = False)
#     institution =  db.Column(db.String(), nullable = False)
#     department = db.Column(db.String(), nullable = False)
#     year = db.Column(db.Integer(), nullable = False)
#     description = db.Column(db.String(), nullable = False)
#     state = db.Column(db.String(), nullable = False)
#     city = db.Column(db.String(), nullable = False)
#     sub_city = db.Column(db.String(), nullable = False)
#     woreda = db.Column(db.String(), nullable = False)
#     dormitory = db.Column(db.String(), nullable = False,default="FBE Campus")  




