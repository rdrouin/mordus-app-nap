from .db import db
from .cap_horaire_reader import cap_horaire_reader
class CapHoraire(db.Model):
    __tablename__ = "cap_horaire"
    id_cap_horaire = db.Column('id_cap_horaire',db.Integer , primary_key=True)
    cap_value = db.Column('cap_value',db.Integer)
    cap_timestamp =db.Column('cap_value',db.DateTime)
    user_id = db.Column('id_cap',db.Integer)

    def __init__(self ,cap_value,cap_timestamp,user_id):
        self.cap_value= cap_value
        self.cap_timestamp= cap_timestamp
        self.user_id = user_id
