from .db import db
import csv

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
    status = db.Column('status' , db.String(20))

    def __init__(self ,date ,heure ,noVol,fc, aeronef, od, secteur, status):
        self.date=date
        self.heure=heure
        self.noVol=noVol
        self.fc = fc
        self.aeronef=aeronef
        self.od=od
        self.secteur=secteur
        self.status=status
#import pandas
def vol_reader(file):
    table = []
    with open(file, 'r') as csvfile:
        volReader = csv.reader(csvfile, delimiter=';')
        headers = volReader.__next__()
        for row in volReader:
            obj = {}
            for i, h in enumerate(headers):
                obj[h] = row[i]
            table.append(obj)
    return table
