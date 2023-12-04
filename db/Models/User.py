from ..dbinit import db
class User(db.Document):
    email = db.StringField(required = True, unique=True )
    displayName = db.StringField()
    clouds = db.ListField(db.StringField())