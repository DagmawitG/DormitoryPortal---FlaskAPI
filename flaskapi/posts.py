from flask import Flask, request, session,jsonify,abort
from flaskapi.models import UserModel,Post,RequestModel,AcceptedModel
from sqlalchemy.orm import sessionmaker
from flask_login import login_required, current_user, login_user, logout_user
from flaskapi import db, api, app
from flask_restful import Api,Resource
from marshmallow import fields, Schema
from flaskapi.schema import *
import jwt
from flaskapi.auth import *

class PostAPI(Resource):
    @token_required_student
    def get(self,id=None):
        if(id):
            post = Post.query.filter_by(post_id=id).first()
            if(post):
                result = post_schema.dump(post)
                response = jsonify(result)
                response.status_code = 200
                return response
            else:
                abort(404, message = "No Posts Found with the specified ID ")
        else:
            all_posts = Post.query.all()
            if all_posts:
                result = posts_schema.dump(all_posts)
                response = jsonify(result)
                response.status_code = 200
                return response
            else:
                abort(404, message = "No Post Found!")

    @token_required_admin
    def post(self):
        
        data = request.form
        if request.is_json:
            new_post = Post(
                title = request.json['title'],
                
                content = request.json['content']
            )

        else:
            new_post = Post(
                title = data['title'],
                content = data['content'] 
            )
    
        db.session.add(new_post)
        db.session.commit()
        result =  post_schema.dump(new_post)
        response = jsonify(result)
        response.status_code = 200
        return response

    @token_required_admin
    def put(self,id):
        update_post = Post.query.filter_by(post_id=id).first()
        if update_post:
            if request.is_json:
                title = request.json['title']
                content = request.json['content']
            else:
                title = request.form['title']
                content = request.form['content']
            update_post.title = title
            update_post.content = content
            db.session.commit()

            result = post_schema.dump(update_post)
            response = jsonify(result)
            response.status_code = 201
            return response
        else:
            abort(404, message="No Post Found with the specified ID!")
    @token_required_admin
    def delete(self,id):
        post = Post.query.filter_by(post_id=id).first()
        if post:
            db.session.delete(post)
            db.session.commit()
            response = jsonify({"message":"Successfully deleted"})
            response.status_code = 202
            return response
        else:
             abort(404, message = "No Post Found with the specified ID!")


