from flask import Flask, request, session,abort,jsonify
from flaskapi.models import UserModel,Post,RequestModel
# ,AcceptedModel,FiveKiloModel,MaleFiveKiloModel,FemaleFiveKiloModel,SixKiloModel,FBEKiloModel
from sqlalchemy.orm import sessionmaker
from flask_login import login_required, current_user, login_user, logout_user
from flaskapi import db, api, app
from flask_restful import Api,Resource
from marshmallow import fields, Schema
from flaskapi.schema import *
from flaskapi.auth import *
import jwt

class RequestAPI(Resource):
    @token_required_admin
    def get(self, id=None):
        if(id):
            requested = RequestModel.query.filter_by(r_id=id).first()
            if(requested):
                result = request_schema.dump(requested)
                response = jsonify(result)
                response.status_code = 200
                return response
            else:
                abort(404, message = "No Requests Found with the specified ID ")
        else:
            all_requests = RequestModel.query.all()
            if all_requests:
                result = requests_schema.dump(all_requests)
                response = jsonify(result)
                response.status_code = 200
                return response
            else:
                abort(404, message = "No Requests Found ")

    @token_required_student
    def post(self):
        data = request.form
        
        if request.is_json:

            new_request = RequestModel(

                students_id = request.json['id'],
                firstname =request.json['firstname'],
                lastname = request.json['lastname'],
                gender = request.json['gender'],
                email = request.json['email'],
                institution = request.json['institution'],
                department = request.json['department'],
                year = request.json['year'],
                description = request.json['description'],
                state = request.json['state'],
                city = request.json['city'],
                woreda = request.json['woreda']
            )
        else:
            new_request = RequestModel(
                students_id =data['id'],
                firstname =data['firstname'],
                lastname = data['lastname'],
                gender = data['gender'],
                email = data['email'],
                institution = data['institution'],
                department = data['department'],
                year = data['year'],
                description = data['description'],
                state = data['state'],
                city = data['city'],
                woreda = data['woreda']
            )

        
        db.session.add(new_request)
        db.session.commit()

        result = request_schema.dump(new_request)
        response = jsonify(result)
        response.status_code = 201
        return response

    @token_required_student   
    def delete(self,id):
        requested = RequestModel.query.filter_by(r_id=id).first()
        if requested:
            db.session.delete(requested)
            db.session.commit()
            response = jsonify({"message":"Successfully deleted"})
            response.status_code = 202
            return response
        else:
             abort(404, message = "No Requests Found with the specified ID!")

    



        