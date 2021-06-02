from flask import Flask, request, session
from flaskapi.models import StudentModel,AdminModel,Post,RequestModel,AcceptedModel
from sqlalchemy.orm import sessionmaker
from flask_login import login_required, current_user, login_user, logout_user
from flaskapi import db, api, app
from flask_restful import Api,Resource

class PostAPI(Resource):
    def get(self):
        all_posts = Post.query.all()
        return posts_schema.dump(all_posts)

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
        return posts_schema.dump(new_post)
    def put(self,post_id):
        if request.is_json:
            if 'title' in request.json:
                post.title = request.json['title']
            if 'content' in request.json:
                post.content = request.json['content']
        else:
            if 'title' in request.form:
                post.title = request.form['title']
            if 'content' in request.form:
                post.content = request.form['content']
    def delete(self,post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return 'Deleted',204

