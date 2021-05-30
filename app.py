from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from sqlalchemy import Column, String , Integer 
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
# api = Api(app)
app.config['DATABASE_URI'] = 'postgresql://enwlbywxxbocyo:51943602ee8249be91f30af6a17651825d6ccbc2b6ffbccb003b4f1d1466b406@ec2-34-232-191-133.compute-1.amazonaws.com:5432/d6hc9vv24v7k03' 
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


if __name__ == '__main__':
    app.run(debug=True)