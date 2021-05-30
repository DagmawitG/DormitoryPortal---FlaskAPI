#from flask import jsonify,request

from flaskapi.models import StudentModel,AdminModel,Post
from sqlalchemy.orm import sessionmaker
from flask_login import login_required, current_user, login_user, logout_user
from flaskapi import db, api, app


@app.route('/login', methods=["POST"])
def login():
    if(current_user.is_authenticated):
        return jsonify({'message': "You've already logged in"})
    username_entered = request.form.get('username')
    password_entered = request.form.get('password')
    username_entered = username_entered.lower()
    if username_entered.startswith('atr/'):
        user = StudentModel.query.filter_by(username_entered  = student_name ).first()
    else:    
        user = StudentModel.query.filter_by(username_entered  = admin_name ).first()
   
    if user is not None and user.check_password(password_entered):
        login_user(user)
        return jsonify({'logged_in': True})
    return jsonify({'logged_in': False})
    
@app.route('/logout', methods=["POST"])
def logout():
    logout_user()
    return jsonify({'message': "You've logged out successfully"})


 