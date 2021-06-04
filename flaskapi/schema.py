from flaskapi.models import UserModel,Post,RequestModel,AcceptedModel
from flaskapi import ma
from flask_marshmallow import Marshmallow
from marshmallow import fields, Schema

class PostSchema(ma.Schema):
    class Meta:
        fields = ("post_id", "title", "content","date_posted","user_id")
        model = Post
post_schema = PostSchema()
posts_schema = PostSchema(many = True)

class RequestsSchema(ma.Schema):
    class Meta:
        fields = ("r_id","requestedPerson_id","students_id","firstname","lastname","gender","email", "institution","department","year","description","state","city","sub_city","woreda")
        model = RequestModel
request_schema = RequestsSchema()
requests_schema = RequestsSchema(many=True)

class AcceptedSchema(ma.Schema):
    class Meta:
        fields = ("a_id","requestedPerson_id","students_id","firstname","lastname","gender","email", "institution","department","year","description","state","city","sub_city","woreda")
        model = AcceptedModel
acceptant_schema = AcceptedSchema()
acceptants_schema = AcceptedSchema(many=True)


# class FiveKiloSchema(ma.Schema):
#     class Meta:
#         fields = ("fk_id","requestedPerson_id","students_id","firstname","lastname","gender","email", "institution","department","year","description","state","city","sub_city","woreda","dormitory")
#         model = FiveKiloModel
# fiveKilo_schema = FiveKiloSchema()
# fiveKilos_schema = FiveKiloSchema(many=True)


# class MaleFiveKiloSchema(ma.Schema):
#     class Meta:
#         fields = ("mf_id","requestedPerson_id","students_id","firstname","lastname","gender","email", "institution","department","year","description","state","city","sub_city","woreda","dormitory","blockNumber","dormNumber")
#         model = MaleFiveKiloModel
# malefiveKilo_schema = MaleFiveKiloSchema()
# malefiveKilos_schema = MaleFiveKiloSchema(many=True)

# class FemaleFiveKiloSchema(ma.Schema):
#     class Meta:
#         fields = ("ff_id","requestedPerson_id","students_id","firstname","lastname","gender","email", "institution","department","year","description","state","city","sub_city","woreda","dormitory","blockNumber","dormNumber")
#         model = FemaleFiveKiloModel
# femalefiveKilo_schema = FemaleFiveKiloSchema()
# femalefiveKilos_schema = FemaleFiveKiloSchema(many=True)

# class SixKiloSchema(ma.Schema):
#     class Meta:
#         fields = ("sk_id","requestedPerson_id","students_id","firstname","lastname","gender","email", "institution","department","year","description","state","city","sub_city","woreda","dormitory")
#         model = SixKiloModel
# sixKilo_schema = SixKiloSchema()
# sixKilos_schema = SixKiloSchema(many=True)

# class FBESchema(ma.Schema):
#     class Meta:
#         fields = ("fk_id","requestedPerson_id","students_id","firstname","lastname","gender","email", "institution","department","year","description","state","city","sub_city","woreda","dormitory")
#         model = FBEKiloModel
# fbe_schema = FBESchema()
# fbeS_schema = FBESchema(many=True)

