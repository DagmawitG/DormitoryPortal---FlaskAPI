#from flask import jsonify,request
from flaskapi import app
from flaskapi.models import StudentModel,AdminModel,Post
from sqlalchemy.orm import sessionmaker
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()


@app.route('/login', methods=["GET","POST"])
def login():
    username_entered = request.args.get('username')
    password_entered = request.args.get('password')
    username_entered = username_entered.str.lower()
    # if username_entered.startswith('atr/'):
    #     user = session.query(StudentModel).filter(or_(StudentModel.username == username_entered, StudentModel.password == password_entered ).first()
    # else:
    #     user = session.query(AdminModel).filter(or_(AdminModel.username == username_entered, AdminModel.password == password_entered ).first()
    # if user is not None and check_password_hash(user.password, password_entered):
    #     return jsonify({'logged_in': True})
    # return jsonify({'logged_in': False})
    


