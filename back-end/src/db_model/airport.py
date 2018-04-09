
from .db import db

from airportsreader import csvreader

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
            print("probleme")



if __name__ == '__main__':
    result = csvreader("airports.csv")
    for line in result:
        airport = Airport(line['city'] , line['airportCode'],line['level2'],line['level3'])
        db.session.add(airport)
        db.session.commit()
    print('airport successfully registered')
