from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid # for public id
from  werkzeug.security import generate_password_hash, check_password_hash
# imports for PyJWT authentication,app
from flaskapi import db, login,app
from flaskapi.models import UserModel,Post,RequestModel,AcceptedModel
import jwt
from datetime import datetime, timedelta
from functools import wraps

def token_required_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'X-Access-Token' in request.headers:
            token = request.headers['X-Access-Token']
        # return 401 if token is not passed
        if not token:
            return {'message' : 'Token is missing !!'}, 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = UserModel.query.filter_by(user_id = data['user_id']).first()
            print(current_user)
        except:
            return {'message' : 'Token is invalid !!'}, 401
        if current_user.role != 'Admin':
            return {'message' : 'Not Authorized'},401
        # returns the current logged in users contex to the routes
        return f(*args, **kwargs)
  
    return decorated

def token_required_student(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'X-Access-Token' in request.headers:
            token = request.headers['X-Access-Token']
        # return 401 if token is not passed
        if not token:
            return {'message' : 'Token is missing !!'}, 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = UserModel.query.filter_by(user_id = data['user_id']).first()
        except:
            return {'message' : 'Token is invalid !!'}, 401
        if current_user.role != 'student':
            return {'message':'Not Authorized'},401
        # returns the current logged in users contex to the routes
        return f(*args, **kwargs)
  
    return decorated


