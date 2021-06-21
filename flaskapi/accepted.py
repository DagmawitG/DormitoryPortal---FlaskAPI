from flask import Flask, request, session,abort,jsonify
from flaskapi.models import UserModel,Post,RequestModel,AcceptedModel

from sqlalchemy.orm import sessionmaker
from flask_login import login_required, current_user, login_user, logout_user
from flaskapi import db, api, app
from flask_restful import Api,Resource
from marshmallow import fields, Schema
from sqlalchemy import and_
import jwt
import random
from flaskapi.auth import *
from flaskapi.models import AcceptedModel, RequestModel
from flaskapi.schema import *

class AcceptanceAPI(Resource):
    @token_required_admin
    def get(self,id=None):
        if(id):
            accepted = AcceptedModel.query.filter_by(a_id = id)
            if(accepted):
                result = accepteds_schema.dump(accepted)
                response = jsonify(result)
                return response
            else:
                abort(404, "No Accepted Students Found with the specified ID ")

        else:
            acceptants = AcceptedModel.query.all()
            if acceptants:
                result = accepteds_schema.dump(acceptants)
                response = jsonify(result)
                return response
            else:
                abort(404, "No Accepted Students Found ")

    @token_required_admin
    def post(self, id):
        
        req = RequestModel.query.filter_by(r_id= id).first()
        if not req:
            abort(404, message="Request not found!")
        else:
            if (req.year == 5 and req.gender == "M"):
                dormitoryPlace = "5 Kilo"
                blockNumber = 1
            elif (req.year == 5 and req.gender == "F"):
                dormitoryPlace = "5 Kilo"
                blockNumber = 2
            elif (req.year != 5 and req.gender == "F"):
                dormitoryPlace = "FBE"
                blockNumber = 2
            elif (req.year != 5 and req.gender == "M"):
                dormitoryPlace = "6 Kilo"
                blockNumber = 1

            accepted = AcceptedModel(requestedPerson_id=id,
                                     status = True,
                                     dormitoryPlace = dormitoryPlace,
                                     blockNumber = blockNumber,
                                     dormNumber = random.randint(1,150 ),
                                     stud_id=req.students_id,
                                     department = req.department,
                                     year = req.year,
                                     firstname = req.firstname,
                                     lastname = req.lastname
                                     )
                                     
            db.session.add(accepted)
            db.session.commit()
            return accepted_schema.dump(accepted)
            
    @token_required_admin
    def delete(self,id):
        deleted = AcceptedModel.query.filter_by(a_id= id).first()
        if not deleted:
            abort(404, "Request not found!")
        else:
            db.session.delete(deleted)
            db.session.commit()
            response = jsonify({"message":"Successfully deleted"})
            response.status_code = 202
            return response



            




   



        
         
