from .db import db
from .vol_reader import vol_reader
import datetime

class Vol(db.Model):
    __tablename__ = "vol"
    id = db.Column('id',db.Integer , primary_key=True)
    date = db.Column('date',db.String(20))
    heure = db.Column('heure', db.Time)
    noVol = db.Column('novol' , db.String(20))
    fc= db.Column('fc' , db.String(2))
    aeronef = db.Column('aeronef',db.String(10))
    od = db.Column('od' , db.String(10))
    secteur = db.Column('secteur' , db.String(10))

    def __init__(self ,date ,heure ,noVol,fc, aeronef, od, secteur):
        self.date=date
        self.heure=heure
        self.noVol=noVol
        self.fc = fc
        self.aeronef=aeronef
        self.od=od
        self.secteur=secteur
