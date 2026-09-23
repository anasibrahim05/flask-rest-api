from marshmallow import Schema , fields
class plainitemschema(Schema):
  item_id=fields.Str(dump_only=True)
  name=fields.Str(required=True)
  price=fields.Int(required=True)


class plainstoreschema(Schema):
  id=fields.Int(dump_only=True)
  name=fields.Str(required=True)
  location=fields.Str(required=True)

class plaintagschema(Schema):
  id=fields.Str(dump_only=True)
  name=fields.Str(required=True)
  

class updatestorescehma(Schema):

  name=fields.Str()
  location=fields.Str()



class updateitemschema(Schema):
  store_id=fields.Int()
  name=fields.Str()
  price=fields.Int()

class itemschema(plainitemschema):
  store_id=fields.Int(required=True, load_only=True)
  stores=fields.Nested(plainstoreschema,dump_only=True)
  tags=fields.List(fields.Nested(plaintagschema),dump_only=True)
  
class storeschema(plainstoreschema):
  items=fields.List(fields.Nested(plainitemschema),dump_only=True)
  tags=fields.Nested(plaintagschema,dump_only=True)

class tagschema(plaintagschema):
  store_id=fields.Int(load_only=True)
  stores=fields.Nested(plainstoreschema,dump_only=True)
  items=fields.List(fields.Nested(plainitemschema),dump_only=True)
  
class itemtagschema(Schema):
  message=fields.Str()
  items=fields.Nested(itemschema)
  tags=fields.Nested(tagschema)
  
class userschema(Schema):
  id=fields.Int(dump_only=True)
  username=fields.Str(required=True)
  password=fields.Str(required=True,load_only=True)
  
class registerschema(userschema):
  email=fields.Str(required=True)