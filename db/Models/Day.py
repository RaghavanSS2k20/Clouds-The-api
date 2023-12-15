from __future__ import annotations
from ..dbinit import db
from .Cloud import Cloud
from datetime import datetime

from .Cloud import EmotionalResult

class Day(db.Document):
    
    clouds = db.ListField(db.ReferenceField(Cloud))
    displayCloud = db.ReferenceField(Cloud)
    mostNoticedEmotion = db.DictField()
    date = db.DateTimeField(default=datetime.utcnow, unique=True)

    def __init__(self, *args, **kwargs):
        super(Day, self).__init__(*args, **kwargs)
        from .User import User
        self.user = db.ReferenceField(User)



    