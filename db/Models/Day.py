from ..dbinit import db
from .Cloud import Cloud
from User import User
from .Cloud import EmotionalResult

class Day(db.Document):
    user = db.ReferenceField(User)
    clouds = db.ListField(db.ReferenceField(Cloud))
    displayCloud = db.ReferenceField(db.ReferenceField(Cloud))
    mostNoticedEmotion = db.DictField()

    