from flask import jsonify,request,session,abort,Blueprint

from flaskapi.models import UserModel,Post,RequestModel,AcceptedModel
from sqlalchemy.orm import sessionmaker
from flask_login import login_required, current_user, login_user, logout_user
from flaskapi import db, api, app 

bp = Blueprint('routes', __name__)
@bp.route('/login', methods=["POST"])
def login():
    if(current_user.is_authenticated):
        return jsonify({'message': "You've already logged in"})
    username_entered = request.form.get('username')
    password_entered = request.form.get('password')
    try:
        user = UserModel.query.filter_by(user_name=username_entered).first()
        if not user:
            return abort(404,"User not found!")    
        
    
        if (user and user.check_password(user.user_password,password_entered)):
            if (user.role == "student"):
               
                
                return jsonify({'Message': "Student Login Successful!"})
            elif (user.role == "admin"):
                
                
                return jsonify({'Message': "Admin Login Successful!"})
            session["role"] = user.role
            login_user(user)
    except Exception as e:
        return jsonify(str(e))
    
@bp.route('/logout', methods=["POST"])
def logout():
    logout_user()
    session["role"] = ''
    return jsonify({'message': "You've logged out successfully"})


 