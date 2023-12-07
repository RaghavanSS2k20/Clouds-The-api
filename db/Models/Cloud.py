from ..dbinit import db
from .User import User
from datetime import datetime
from enum import Enum

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
    user = db.ReferenceField(User)
    cloudTime = db.DateTimeField(default=datetime.utcnow)
    intent = db.EnumField(IntentValue, default=IntentValue.DRAFTS)
    emotions = db.ListField(db.DictField())
    

