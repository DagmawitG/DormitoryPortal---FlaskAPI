from flask import Flask, request, session,abort,jsonify
from flaskapi.models import UserModel,Post,RequestModel,AcceptedModel

from sqlalchemy.orm import sessionmaker
from flask_login import login_required, current_user, login_user, logout_user
from flaskapi import db, api, app
from flask_restful import Api,Resource
from marshmallow import fields, Schema
from sqlalchemy import and_
import jwt
from flaskapi.auth import *
from flaskapi.models import AcceptedModel
from flaskapi.schema import accepted_schema

class AcceptanceAPI(Resource):
    # @token_required_admin
    def get(self,id=None):
        if(id):
            accepted = AcceptedModel.query.filter_by(a_id = id)
            if(accepted):
                result = accepted_schema.dump(accepted)
                response = jsonify(result)
                return response
            else:
                abort(404, mesage="No Accepted Students Found with the specified ID ")

        else:
            acceptants = AcceptedModel.query.all()
            if acceptants:
                result = accepted_schema.dump(acceptants)
                response = jsonify(result)
                return response
            else:
                abort(404, message="No Accepted Students Found ")

    @token_required_admin
    def post(self):
       

        
        requ = RequestModel.query.all()
        student = AcceptedModel.query.filter_by(requestedPerson_id=requ.r_id).first()
        if student:
            abort(409, message="Student has already been assigned a dormitory")
        else:
            req = RequestModel.query.filter_by(students_id=student_id).first()
            if not req:
                abort(404, message="Student not found")
              
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

            accepted = AcceptedModel(requestedPerson_id=student_id,
                                     status = True,
                                     dormitoryPlace = dormitoryPlace,
                                     blockNumber = blockNumber,
                                     dormNumber = random.randint(1,150 ))
                                     
            db.session.add(accepted)
            db.session.commit()
            


            




    # def post(self):
    #     fiveKilo = RequestModel.query.filter_by(year = 5)
    #     for row in fiveKilo:
    #         fivedata = FiveKiloModel(row)
    #         db.session.add(fivedata)
    #         db.session.commit()
    #     return fivekilos_schema.dump(fivedata)

        # maleFiveKilo = FiveKiloModel.query.filter_by(gender = 'M')
        # for row in maleFiveKilo:
        #     malefivedata = MaleFiveKiloModel(row)
        #     db.session.add(malefivedata)
        #     db.session.commit()
        # return malefiveKilos_schema_schema.dump(fivedata) 

        # femaleFiveKilo = FiveKiloModel.query.filter_by(gender = 'F')
        # for row in femaleFiveKilo:
        #     femalefivedata = FemaleFiveKiloModel(row)
        #     db.session.add(femalefivedata)
        #     db.session.commit()
        # return femalefiveKilos_schema.dump(fivedata) 

        # sixKilo = AcceptedModel.query.filter_by(and_(year != 5 , gender='M'))
        # for row in sixKilo:
        #     sixdata = SixKiloModel(row)
        #     db.session.add(sixdata)
        #     db.session.commit()
        # return sixkilos_schema.dump(sixdata)

        # fbeKilo = AcceptedModel.query.filter_by(and_(year != 5 , gender='F'))
        # for row in fbeKilo:
        #     fbedata = FBEKiloModel(row)
        #     db.session.add(fbedata)
        #     db.session.commit()
        # return fbeS_schema.dump(fbedata)







        
         
