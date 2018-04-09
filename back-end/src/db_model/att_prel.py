
from .db import db
class AttributionPreliminaire(db.Model):
    __tablename__ = "attPrel"
    id_att_prel = db.Column('id_att_prel',db.Integer , primary_key=True)
    fc_code = db.Column('fc_code',db.String(2))
    plage_horaire = db.Column('fc_code',db.DateTime)
    value  = db.Column('value' , db.Float)
    timestamp_open = db.Column('timestamp_open' , db.DateTime)
    timestamp_close =db.Column('timestamp_close' , db.DateTime)

def __init__(self ,id ,fc):
    self.fc_code=fc_code
    self.plage_horaire= plage_horaire
    self.value= value
    self.timestamp_open = timestamp_open
    self.timestamp_close= timestamp_close
