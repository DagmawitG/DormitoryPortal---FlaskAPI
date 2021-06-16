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
class AcceptanceAPI(Resource):
    @token_required_admin
    def get(self,id=None):
        if(id):
            accepted = AcceptModel.query.filter_by(a_id = id)
            if(accepted):
                result = acceptant_schema.dump(accepted)
                response = jsonify(result)
                return response
            else:
                abort(404,"No Accepted Students Found with the specified ID ")

        else:
            acceptants = AcceptModel.query.all()
            if acceptants:
                result = acceptants_schema.dump(acceptants)
                response = jsonify(result)
                return response
            else:
                abort(404,"No Accepted Students Found ")
    @token_required_admin
    def post(self):
        data = request.form 
        acceptants = AcceptedModel.query.all()
        if acceptants.status == True:
            filter1 = AcceptedModel.query.filter_by(and_(year == 5 , gender='M')).all()
            if filter1:
                filter1.dormitoryPlace = "5 kilo Campus"
                filter1.blockNumber = 1
            filter2 = AcceptedModel.query.filter_by(and_(year == 5 , gender='F')).all()
            if filter2:
                filter2.dormitoryPlace = "5 kilo Campus"
                filter2.blockNumber = 2
            filter2 = AcceptedModel.query.filter_by(and_(year != 5 , gender='M')).all()  
            if filter3:
                filter3.dormitoryPlace = "6 kilo Campus"
                filter3.blockNumber = 1
            filter4 = AcceptedModel.query.filter_by(and_(year != 5 , gender='F')).all()  
            if filter4:
                filter4.dormitoryPlace = "FBE Campus"
                filter4.blockNumber = 2
            


            




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







        
         
