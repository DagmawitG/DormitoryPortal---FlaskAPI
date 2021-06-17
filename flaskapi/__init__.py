from flask import Flask,Blueprint
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager
from flask_restful import Api,Resource
from flask_login import login_required, current_user, login_user, logout_user
from flask_marshmallow import Marshmallow
from marshmallow import fields, Schema
from flask_cors import CORS



from flask_bcrypt import Bcrypt

app = Flask(__name__)

CORS(app)



app.config['SECRET_KEY'] = "uirgjbgidojfr89tre490fguhdojvgdih2535trt"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://enwlbywxxbocyo:51943602ee8249be91f30af6a17651825d6ccbc2b6ffbccb003b4f1d1466b406@ec2-34-232-191-133.compute-1.amazonaws.com:5432/d6hc9vv24v7k03'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config["DEBUG"] = True



api = Api(app)
login = LoginManager()
login.init_app(app)
bcrypt = Bcrypt(app)
CORS(app)
db = SQLAlchemy()
db.init_app(app)
ma = Marshmallow(app)

app.app_context().push()




from flaskapi.models import *
from flaskapi import routes,posts,requests,accepted
app.register_blueprint(routes.bp)
api.add_resource(posts.PostAPI, '/posts','/posts/<int:id>')
api.add_resource(accepted.AcceptanceAPI, '/requests/<int:id>/accepted','/accepted/<int:id>','/accepted')
api.add_resource(requests.RequestAPI, '/requests','/requests/<int:id>')



