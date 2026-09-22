from flask import request
from model import UserModel
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import userschema
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token

blp = Blueprint("users", __name__, description="Operations on user")

@blp.route("/register")
class registeruser(MethodView):
    @blp.arguments(userschema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(400, message="username already exists")
            
        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"])
        )
        
        try:
            db.session.add(user)
            db.session.commit()
            # Fixed typo and added 201 Created status code
            return {"message": "registered successfully"}, 201
        except SQLAlchemyError:
            # Changed 404 to 500 Internal Server Error
            abort(500, message="failed to register user")
      
      
    
  
  
@blp.route("/user/<int:id>")
class userop(MethodView):
  @blp.response(200,userschema)
  def get(self,id):
    user=UserModel.query.get_or_404(id)
    
    return user

  @blp.response(200,description="delete succesfully")
  def delete(self,id):
    user=UserModel.query.get_or_404(id)
    
    try:
      db.session.delete(user)
      db.session.commit()
      return {"message":"deleted"}
      
    except SQLAlchemyError:
      abort(message="error deleting")
    
  @blp.route("/login")
  class loginuser(MethodView):
    @blp.response(200,description="login successfull")
    @blp.arguments(userschema)
    def post(self,user_data):
      user=UserModel.query.filter(UserModel.username == user_data["username"]).first()
      if user and pbkdf2_sha256.verify( user_data["password"],user.password):
        access_token=create_access_token(identity=str(user.id))
        return {"token":access_token}
      
      abort(404,message="invalid credentials")
      
    
   