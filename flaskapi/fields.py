from flask_restful import fields
from flaskapi.models import UserModel,Post,AcceptedModel

user_fields = {
    'id' : fields.Integer,
    'user_id' : fields.String,
    'user_name' : fields.String,
    'user_email' : fields.String,
    'user_password' : fields.String,
    'posts': fields.Nested(post_fields)
    
}


post_fields = {
    'post_id' : fields.Integer,
    'title' : fields.String,
    'date_posted' : fields.DateTime,
    'content' : fields.String,
    'user_id' : fields.Nested(user_fields)
}

request_fields = {
    "r_id" : fields.Integer,
    "requestedPerson_id" : fields.Nested(user_fields),
    "students_id" : fields.String,
    "firstname" : fields.String,
    "lastname" : fields.String,
   " gender" : fields.String,
    "email" : fields.String,
    "institution" :fields.String,
    "department" : fields.String,
    "year": fields.Integer,
    "description": fields.String,
    "state" : fields.String,
    "city": fields.String,
    "sub_city" : fields.String,
    "woreda" : fields.Integer

}
