from flask import jsonify,request,session,abort,Blueprint,make_response

from flaskapi.models import UserModel,Post,RequestModel,AcceptedModel
from sqlalchemy.orm import sessionmaker
from flaskapi.auth import *
from flask_login import login_required, current_user, login_user, logout_user
from flaskapi import db, api, app 
import uuid # for public id
from  werkzeug.security import generate_password_hash, check_password_hash
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta
from functools import wraps

bp = Blueprint('routes', __name__)



@bp.route('/users', methods=["GET"])
@token_required_admin
def get_all_users(current_user):
    # querying the database
    # for all the entries in it
    users = UserModel.query.all()
    # converting the query objects
    # to list of jsons
    output = []
    for user in users:
        # appending the user data json
        # to the response list
        output.append({
            'user_id': user.user_id,
            'user_name' : user.user_name,
            'user_email' : user.user_email
        })
  
    return jsonify({'users': output})
@bp.route('/login', methods=["POST"])

def login():
    # creates dictionary of form data
    auth = request.form
  
    if not auth or not auth.get('user_id') or not auth.get('user_password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
  
    user = UserModel.query\
        .filter_by(user_id = auth.get('user_id'))\
        .first()
  
    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify,user',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
    
    
    
    if check_password_hash(user.hashed_password,auth.get('user_password')):
        # generates the JWT Token
        if user.role=="Admin":
            token = jwt.encode({
                'user_id': user.user_id,
                'exp' : datetime.utcnow() + timedelta(minutes = 30)
            }, app.config['SECRET_KEY']) 
            session["role"] = user.role
            return make_response(jsonify({'token' : token}, {'role' : user.role}), 201)
        elif user.role=="student":
            token = jwt.encode({
                'user_id': user.user_id,
                'exp' : datetime.utcnow() + timedelta(minutes = 30)
            }, app.config['SECRET_KEY'])
            session["role"] = user.role
            return make_response(jsonify({'token' : token}, {'role' : user.role}), 201)
        
    # returns 403 if password is wrong
    return make_response(
        'Could not verify,pwd',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    ) 


# @bp.route('/signup', methods =['POST'])
# def signup():
#     # creates a dictionary of the form data
#     data = request.form
  
#     # gets name, email and password
#     user_id = data.get('user_id')
#     user_name, user_email = data.get('user_name'), data.get('user_email')
#     user_password = data.get('user_password')
  
#     # checking for existing user
#     user = User.query\
#         .filter_by(user_id = user_id)\
#         .first()
#     if not user:
#         # database ORM object
#         user = User(
#             user_id = user_id,
#             user_name = user_name,
#             user_email = user_email,
#             user_password = generate_password_hash(user_password)
#         )
#         # insert user
#         db.session.add(user)
#         db.session.commit()
  
#         return make_response('Successfully registered.', 201)
#     else:
#         # returns 202 if user already exists
#         return make_response('User already exists. Please Log in.', 202)
     


# def login():
#     if(current_user.is_authenticated):
#         return jsonify({'message': "You've already logged in"})
#     username_entered = request.json['username']
#     password_entered = request.json['password']
#     try:
#         user = UserModel.query.filter_by(user_name=username_entered).first()
#         if not user:
#             return abort(404,"User not found!")    
        
    
#         if (user and user.check_password(user.user_password,password_entered)):
#             if (user.role == "student"):
               
                
#                 return jsonify({'Message': "Student Login Successful!"})
#             elif (user.role == "admin"):
                
                
#                 return jsonify({'Message': "Admin Login Successful!"})
#             session["role"] = user.role
#             login_user(user)
#     except Exception as e:
#         return jsonify(str(e))
    
@bp.route('/logout', methods=["POST"])
def logout():
    
    session["role"] = ''
    return jsonify({'message': "You've logged out successfully"})


 