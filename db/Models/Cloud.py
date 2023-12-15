from ..dbinit import db
# from .User import User
from datetime import datetime
from enum import Enum

from initclassifier import init_classifer
from helpers import get_dominant_emotion

distilled_classifier = init_classifer()

class IntentValue(Enum):
    GOOD = "good"
    BAD = "bad"
    NEUTRAL = "neutral"
    DRAFTS = "draft"


class StatusEnum(Enum):
    VISIBLE = "visible"
    DRAFT = "draft"

class EmotionalResult():
    def __init__(self, label, score):
        self.label = label
        self.score = score


class Cloud(db.Document):

    cloud = db.StringField(required = True)
    cloudTime = db.DateTimeField(default=datetime.utcnow)
    intent = db.EnumField(IntentValue, default=IntentValue.DRAFTS)
    emotions = db.ListField(db.DictField())

    def __init__(self,*args, **kwargs):
        super(Cloud, self).__init__(*args, **kwargs)
        from .User import User
        self.user = db.ReferenceField(User)
    def update_emotions_intent(self):
        self.emotions = distilled_classifier(self.cloud)[0]
        
    
    def save(self, *args, **kwargs):
        self.update_emotions_intent()
        super(Cloud, self).save(*args, **kwargs)


    
    

