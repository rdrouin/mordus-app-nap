
from .db import db

from .airport_reader import airport_reader

class Airport(db.Model):
    __tablename__ = "airport"
    city = db.Column('city',db.String(150))
    airportCode = db.Column('airportCode', db.String(10), primary_key=True)
    level = db.Column('level' , db.Integer)
    def __init__(self ,city ,airportCode , level2, level3):
        self.city = city
        self.airportCode = airportCode
        if level2=='Yes':
            self.level=2
        elif level3=='Yes':
            self.level=3
        else:
            pass
