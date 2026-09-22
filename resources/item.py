from flask import request
from model import ItemModel
from db import db
from flask_smorest import Blueprint, abort
from flask.views import MethodView
import uuid
from schemas import itemschema,updateitemschema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required, get_jwt


blp = Blueprint("Items", __name__, description="Operations on items")

@blp.route("/item/<int:id>")
class Item(MethodView):
    @jwt_required()
    @blp.response(200,itemschema)
    def get(self, id):
        item =ItemModel.query.get_or_404(id)
        return item
    @jwt_required()
    
    def delete(self, id):
        jwt=get_jwt()
        if not jwt.get("is_admin"):
            abort (401,message="authorized previlage required")
        item =ItemModel.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        
        return "deleted successfully"
    @jwt_required()
    @blp.arguments(updateitemschema)
    @blp.response(200,itemschema)
    def put(self,data, id):
        item =ItemModel.query.get(id)
        if item:
            item.name=data["name"]
            item.price=data["price"]
        else:
            item=ItemModel(item_id=id,**data)
        db.session.add(item)
        db.session.commit()
        return item


@blp.route("/item")
class ItemList(MethodView):
    @jwt_required()
    @blp.response(200,itemschema(many=True))
    def get(self):
        return ItemModel.query.all()
    @jwt_required()
    @blp.arguments(itemschema)
    @blp.response(200,itemschema)
    def post(self,data):   
        item=ItemModel(**data)
        
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort (500,"name must be unique")
        except SQLAlchemyError:
            abort(404,"an error happened while inserting the item")
        
        return item