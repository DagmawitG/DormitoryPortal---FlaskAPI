# from flask import Flask
# from flask_restful import Resource, Api
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from sqlalchemy import Column,Integer,String

from flaskapi import app 

# from sqlalchemy.orm import sessionmaker

# app = Flask(__name__)

# app.config['SECRET_KEY'] = "b'-\x8cPQ\xc0\x86\x92\x06\x8e\xa6\x0b?\x80\x02\xd0\x9b\x85\x91\xa8\x8aR1\xa5q'"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://enwlbywxxbocyo:51943602ee8249be91f30af6a17651825d6ccbc2b6ffbccb003b4f1d1466b406@ec2-34-232-191-133.compute-1.amazonaws.com:5432/d6hc9vv24v7k03' 
# db = SQLAlchemy(app)

# api = Api(app)
#DATABASE_URI = 'postgresql://enwlbywxxbocyo:51943602ee8249be91f30af6a17651825d6ccbc2b6ffbccb003b4f1d1466b406@ec2-34-232-191-133.compute-1.amazonaws.com:5432/d6hc9vv24v7k03' 
# engine = create_engine(DATABASE_URI)
# base = declarative_base
# Session = sessionmaker(bind = engine)
# session = Session()


# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/')



if __name__ == '__main__':
    app.run(debug=True)