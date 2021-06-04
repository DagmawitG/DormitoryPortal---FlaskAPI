from flask import Flask, request, session,abort,jsonify
from flaskapi.models import UserModel,Post,RequestModel,AcceptedModel

from sqlalchemy.orm import sessionmaker
from flask_login import login_required, current_user, login_user, logout_user
from flaskapi import db, api, app
from flask_restful import Api,Resource
from marshmallow import fields, Schema
from sqlalchemy import and_

class AcceptanceAPI(Resource):
    def get(self):
        acceptants = AcceptModel.query.all()
        if acceptants:
            result = acceptants_schema.dump(acceptants)
            response = jsonify(result)
            return response
        else:
            abort(404,"No Accepted Students Found ")

    # def post(self,id):


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







        
         
