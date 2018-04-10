from .db import db
from datetime import timedelta

class Contingence(db.Model):
    __tablename__ = "contingence"
    id = db.Column('id',db.Integer , primary_key=True)
    timestamp_start = db.Column('timestamp_start',db.DateTime)
    timestamp_end = db.Column('timestamp_end',db.DateTime)

    def __init__(self , timeStart):
        self.timestamp_start = timeStart
        self.timestamp_end = timeStart + timedelta(hours=4)
