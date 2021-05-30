from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column,Integer,String



from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
# api = Api(app)
app.config['SECRET_KEY'] = "b'-\x8cPQ\xc0\x86\x92\x06\x8e\xa6\x0b?\x80\x02\xd0\x9b\x85\x91\xa8\x8aR1\xa5q'"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://enwlbywxxbocyo:51943602ee8249be91f30af6a17651825d6ccbc2b6ffbccb003b4f1d1466b406@ec2-34-232-191-133.compute-1.amazonaws.com:5432/d6hc9vv24v7k03' 
db = SQLAlchemy(app)
#DATABASE_URI = 'postgresql://enwlbywxxbocyo:51943602ee8249be91f30af6a17651825d6ccbc2b6ffbccb003b4f1d1466b406@ec2-34-232-191-133.compute-1.amazonaws.com:5432/d6hc9vv24v7k03' 
# engine = create_engine(DATABASE_URI)
# base = declarative_base
# Session = sessionmaker(bind = engine)
# session = Session()


# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/')

class StudentModel(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.String(128), primary_key=True)
    student_name = db.Column(db.String(120), nullable=False)
    student_email = db.Column(db.String(120), unique=True, nullable=False)
    student_password = db.Column(db.String(120), nullable=False)
class AdminModel(db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(128), nullable=False)
    admin_email = db.Column(db.String(128), unique=True, nullable=False)
    admin_password = db.Column(db.String(128), nullable=True)
    posts = db.relationship('Post',backref='author',lazy=True)
class Post(db.Model):
     __tablename__ = 'posts'
     post_id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(128), nullable=False)
    #  date_posted = db.Column(db.DateTime, nullable = False , default = DateTime.UtcNow())
     content = db.Column(db.Text , nullable = False)
     user_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'),nullable=False)

if __name__ == '__main__':
    app.run(debug=True)