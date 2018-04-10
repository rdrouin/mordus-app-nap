from .db import db
from .fc_reader import fc_reader
class FlightCompany(db.Model):
    __tablename__ = "fc"
    id = db.Column('id',db.Integer , primary_key=True)
    fc = db.Column('fc',db.String(2))

    def __init__(self ,fc):
        self.fc=fc
