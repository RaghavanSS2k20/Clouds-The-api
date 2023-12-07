from ..dbinit import db
from .Cloud import Cloud
from .Day import Day

class User(db.Document):
    email = db.StringField( unique=True )
    displayName = db.StringField()
    clouds = db.ListField(db.ReferenceField(Cloud))
    phoneNumber = db.StringField(required=True, unique=True)
    passWord = db.StringField(required=True)
    days = db.ListField(db.ReferenceField(Day))
    
    @property
    def totalClouds(self):
        return len(self.clouds)