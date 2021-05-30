from flask import Flask, request, session
from flaskapi.models import StudentModel,AdminModel,Post
from sqlalchemy.orm import sessionmaker
from flask_login import login_required, current_user, login_user, logout_user
from flaskapi import db, api, app
from flask_restful import Api,Resource

class PostResource(Resource):
    def get(self):
        posts = Post.query.all()

    def post(self):
        data = request.form
        new_post = Post(
            title = data['title'],
            content = data['content']



        )
        db.session.add(new_post)
        db.session.commit()
        return "Post Created"

