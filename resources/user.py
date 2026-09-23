from flask import request
from model import UserModel
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import userschema, registerschema
from passlib.hash import pbkdf2_sha256
from sqlalchemy import or_
from flask_jwt_extended import create_access_token
import os
import requests
import jinja2

blp = Blueprint("users", __name__, description="Operations on user")
template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)

def render_html(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)

def send_simple_message(to, subject, body, html):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxdee396c516ce4bf6ae94f1514fade86d.mailgun.org/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={
            "from": "Anas Ibrahim <postmaster@sandboxdee396c516ce4bf6ae94f1514fade86d.mailgun.org>",
            "to": [to],
            "subject": subject,
            "text": body,
            "html": html
        })
      
@blp.route("/register")
class registeruser(MethodView):
    @blp.arguments(registerschema)
    def post(self, user_data):
        if UserModel.query.filter(
          or_(
            UserModel.email == user_data["email"],
            UserModel.username == user_data["username"])).first():
              
            abort(400, message="username or email already exists")
            
        user = UserModel(
            username=user_data["username"],
            email=user_data["email"],
            password=pbkdf2_sha256.hash(user_data["password"])
        )
        
        try:
            db.session.add(user)
            db.session.commit()
            send_simple_message(user.email,
                                "register successfull",
                                f"hi {user.username}, you are register successfully",
                                render_html("email/action.html", username=user.username))
            
            # FIXED: Removed the 'user' object from the return tuple
            return {"message": "registered successfully"}, 201
            
        except SQLAlchemyError:
            abort(500, message="failed to register user")
      
@blp.route("/user/<int:id>")
class userop(MethodView):
    @blp.response(200, userschema)
    def get(self, id):
        user = UserModel.query.get_or_404(id)
        return user

    def delete(self, id):
        user = UserModel.query.get_or_404(id)
        try:
            db.session.delete(user)
            db.session.commit()
            return {"message": "deleted"}
        except SQLAlchemyError:
            # FIXED: Added the 500 status code
            abort(500, message="error deleting")
    
# FIXED: Unindented the login class so it registers correctly
@blp.route("/login")
class loginuser(MethodView):
    @blp.arguments(userschema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username == user_data["username"]).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=str(user.id))
            return {"token": access_token}
      
        abort(401, message="invalid credentials") # Note: 401 is better for login failures