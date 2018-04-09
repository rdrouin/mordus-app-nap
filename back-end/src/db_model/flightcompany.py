

from db import db
class FlightCompany(db.Model):
    __tablename__ = "fc"
    id = db.Column('id',db.Integer , primary_key=True)
    fc = db.Column('fc',db.String(2))
