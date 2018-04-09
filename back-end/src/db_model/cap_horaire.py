from .db import db
class CapHoraire(db.Model):
    __tablename__ = "cap_horaire"
    id_cap_horaire = db.Column('id_cap_horaire',db.Integer , primary_key=True)
    cap_value = db.Column('cap_value',db.Integer)
    cap_timestamp =db.Column('cap_value',db.DateTime)
    user_id = db.Column('id_cap',db.Integer)

def __init__(self ,id ,fc):
    self.id_cap=id_cap
    self.cap_value= cap_value
    self.cap_timestamp= cap_timestamp
    self.user_id = user_id

    for line in result:
        cap_horaire = CapHoraire(line['id_cap_horaire'], line['cap_value'], line['cap_timestamp'], line['user_id'])
        db.session.add(cap_horaire)
        db.session.commit()
