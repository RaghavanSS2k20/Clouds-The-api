from ..dbinit import db
# from lazy
from .Day import Day
from .Cloud import Cloud
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Document):
    
    displayName = db.StringField()
    clouds = db.ListField(db.ReferenceField(Cloud))
    phoneNumber = db.StringField(required=True, unique=True)
    passWord = db.StringField(required=True)
    days = db.ListField(db.ReferenceField(Day))

    def hash_password(self):
        self.passWord = generate_password_hash(self.passWord).decode('utf8')
    def check_password(self, passWord):
        return check_password_hash(self.passWord, passWord)
    
    @property
    def totalClouds(self):
        return len(self.clouds)

   