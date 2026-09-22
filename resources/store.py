from flask import request
from model import StoreModel
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_smorest import Blueprint, abort
from flask.views import MethodView
import uuid
from schemas import storeschema,updateitemschema

blp = Blueprint("Stores", __name__, description="Operations on stores")

@blp.route("/store/<int:id>")
class Store(MethodView):
    @blp.response(200,storeschema)
    def get(self, id):
        store =StoreModel.query.get_or_404(id)
        return store

    def delete(self, id):
        store =StoreModel.query.get_or_404(id)
        db.session.delete(store)
        db.session.commit()
        
        return "deleted successfully"

    @blp.arguments(updateitemschema)
    @blp.response(200,storeschema)
    def put(self,data, id):
        store =StoreModel.query.get_or_404(id)
        
        store.name=data["name"]
        store.location=data["location"]
       
        
        db.session.add(store)
        db.session.commit()
        
        return store

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200,storeschema(many=True))
    def get(self):
        return StoreModel.query.all()

    @blp.arguments(storeschema)
    @blp.response(200,storeschema)
    def post(self,data):

        store =StoreModel(**data)
        
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort (500,"name must be unique")
        except SQLAlchemyError:
            abort(500,"error storing data")
        
        return store