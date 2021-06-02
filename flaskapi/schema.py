from flaskapi.models import StudentModel,AdminModel,Post,RequestModel,AcceptedModel
from flaskapi import ma
from flask_marshmallow import Marshmallow
from marshmallow import fields, Schema

class PostSchema(ma.Schema):
    class Meta:
        fields = ("post_id", "title", "content","date_posted","user_id")
        model = Post
post_schema = PostSchema()
posts_schema = PostSchema(many = True)

class PlacementSchema(ma.Schema):
    class Meta:
        fields = ("students_id","firstname","lastname","gender","email", "institution","department","year","description","state","city","sub-city","woreda")
        model = RequestModel
placement_schema = PlacementSchema()
placements_schema = PlacementSchema(many=True)

class PlacementSchema(ma.Schema):
    class Meta:
        fields = ("students_id","firstname","lastname","gender","email", "institution","department","year","description","state","city","sub-city","woreda")
        model = RequestModel
placement_schema = PlacementSchema()
placements_schema = PlacementSchema(many=True)
