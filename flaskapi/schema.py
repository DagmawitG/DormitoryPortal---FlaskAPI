from flaskapi.models import UserModel,Post,RequestModel,AcceptedModel
from flaskapi import ma
from flask_marshmallow import Marshmallow
from marshmallow import fields, Schema

class PostSchema(ma.Schema):
    class Meta:
        fields = ("post_id", "title", "content","date_posted")
        model = Post
post_schema = PostSchema()
posts_schema = PostSchema(many = True)

class RequestsSchema(ma.Schema):
    class Meta:
        fields = ("r_id","students_id","firstname","lastname","gender","email", "institution","department","year","description","state","city","sub_city","woreda")
        model = RequestModel
request_schema = RequestsSchema()
requests_schema = RequestsSchema(many=True)

class AcceptedSchema(ma.Schema):
    class Meta:
        fields = ("a_id", "requestedPerson_id","firstname" ,
    "lastname","stud_id","year","department", "status", "dormitoryPlace", "blockNumber", "dormNumber")
        model = AcceptedModel
accepted_schema = AcceptedSchema()
accepteds_schema = AcceptedSchema(many=True)




