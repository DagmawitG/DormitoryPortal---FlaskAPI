from flask import Flask, request, session
from flaskapi.models import StudentModel,AdminModel,Post,RequestModel,AcceptedModel
from sqlalchemy.orm import sessionmaker
from flask_login import login_required, current_user, login_user, logout_user
from flaskapi import db, api, app
from flask_restful import Api,Resource
from marshmallow import fields, Schema

class AcceptanceAPI(Resource):
    def post(self):
        result = 

        
        if 
