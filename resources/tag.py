from model import TagModel, StoreModel,ItemModel,ItemTagModel
from flask_smorest import Blueprint, abort
from schemas import tagschema,storeschema,plaintagschema,itemtagschema
from db import db
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

blp=Blueprint("tags",__name__,description="tag api")

@blp.route("/store/<int:store_id>/tags")
class taglist(MethodView):
  @blp.arguments(tagschema)
  @blp.response(201,tagschema)
  def post(self,tag_data,store_id):
    if TagModel.query.filter(TagModel.store_id==store_id, TagModel.name==tag_data["name"] ).first():
      abort(404,message="tag with same name exist")
    
    
    tag=TagModel(**tag_data,store_id=store_id)
    
    try:
      db.session.add(tag)
      db.session.commit()
    except SQLAlchemyError as e:
      abort(e)
    
    return tag
  
  @blp.response(200,tagschema(many=True))
  def get(self,store_id):
    store=StoreModel.query.get_or_404(store_id)
    
    return store.tags.all()
  
  
@blp.route("/tags/<int:id>")
class tagitems(MethodView):
  @blp.response(201,tagschema)
  def get(self,id):
    tag=TagModel.query.get_or_404(id)
    
    return tag
  
  
  @blp.response(201,description="deleted")
  def delete(self,id):
    tag=TagModel.query.get_or_404(id)
    
    if not tag.items:
      
      db.session.delete(tag)
      db.session.commit()
      return "deleted"
    return "items linked to it"      
    

@blp.route("/item/<int:item_id>/tag/<int:tag_id>")
class linkitemtotag(MethodView):
  @blp.response(200,tagschema)
  def post(self,item_id,tag_id):
    item=ItemModel.query.get_or_404(item_id)
    tag=TagModel.query.get_or_404(tag_id)
    
    item.tags.append(tag)
    
    try:
      db.session.add(item)
      db.session.commit()
    except SQLAlchemyError:
      abort(500,"error")
    
    return tag 
  
  @blp.response(200,itemtagschema)
  def delete(self,item_id,tag_id):
      item=ItemModel.query.get_or_404(item_id)
      tag=TagModel.query.get_or_404(tag_id)
      
      item.tags.remove(tag)
      
      try:
        db.session.add(item)
        db.session.commit()
      except SQLAlchemyError:
        abort("error")
      
      return tag 
    
 
  