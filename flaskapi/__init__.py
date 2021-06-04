from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager
from flask_restful import Api,Resource
from flask_login import login_required, current_user, login_user, logout_user
from flask_marshmallow import Marshmallow
from marshmallow import fields, Schema



app = Flask(__name__)





app.config['SECRET_KEY'] = "b'-\x8cPQ\xc0\x86\x92\x06\x8e\xa6\x0b?\x80\x02\xd0\x9b\x85\x91\xa8\x8aR1\xa5q'"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://enwlbywxxbocyo:51943602ee8249be91f30af6a17651825d6ccbc2b6ffbccb003b4f1d1466b406@ec2-34-232-191-133.compute-1.amazonaws.com:5432/d6hc9vv24v7k03'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config["DEBUG"] = True



api = Api(app)
login = LoginManager()
login.init_app(app)

db = SQLAlchemy()
db.init_app(app)
ma = Marshmallow(app)

app.app_context().push()


from flaskapi.models import *
from flaskapi import routes,posts,requests,accepted

api.add_resource(posts.PostAPI, '/posts','/posts/<int:post_id>')
# api.add_resource(accepted.AcceptanceAPI, '/accepted')
api.add_resource(requests.RequestAPI, '/requests')

