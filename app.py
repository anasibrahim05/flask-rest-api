from flask import Flask, jsonify
from flask_smorest import Api
from db import db
import model
import os
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from resources.store import blp as StoreBlueprint
from resources.item import blp as ItemBlueprint
from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint



def create_app(DB_URL=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"]=DB_URL or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    db.init_app(app)
    migrate=Migrate(app,db)
    app.config["JWT_SECRET_KEY"]="John"
    jwt=JWTManager(app)
    @jwt.invalid_token_loader
    def inavlid_token_loader(error):
        return (
        jsonify ({"description":"signature invalid","error":"in valid token"
                            
        }),401
        )

    @jwt.additional_claims_loader
    def additional_claim_loader(identity):
            if identity==1:
                    return {"is_admin":True}
            return {"is_admin":False}
    @jwt.expired_token_loader
    def expired_token_loader(jwt_header,jwt_payload):
        return (
                jsonify ({"description":"failed to autharize","error":"token expired"
                                        
                }),401
                )
        
        
    @jwt.unauthorized_loader
    def unauthorize_loader(error):
        return (
        jsonify ({"description":"can not be authorze","error":"token is missing"
                                    
        }),401
        )
   
    api = Api(app)
    with app.app_context():
            db.create_all()
    # Notice the lowercase 'b' in register_blueprint
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)

    return app