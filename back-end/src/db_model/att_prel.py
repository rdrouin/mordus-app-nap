
from .db import db
class AttributionPreliminaire(db.Model):
    __tablename__ = "att_prel"
    id_att_prel = db.Column('id_att_prel',db.Integer , primary_key=True)
    fc_code = db.Column('fc_code',db.String(2))
    plage_horaire = db.Column('plage_horaire',db.Integer)
    id_group  = db.Column('id_group' , db.String(50))
    group_name  = db.Column('group_name' , db.String(50))
    group_type  = db.Column('group_type' , db.String(50))
    group_class  = db.Column('group_class' , db.String(50))
    capacity  = db.Column('capacity' , db.Float)
    timestamp_open = db.Column('timestamp_open' , db.DateTime)
    timestamp_close =db.Column('timestamp_close' , db.DateTime)
    plage = db.Column('plage_horaire', db.Integer)

    def __init__(self ,fc_code ,plage_horaire,value, timestamp_open,timestamp_close):
        self.fc_code=fc_code
        self.plage_horaire= plage_horaire
        self.value= value
        self.timestamp_open = timestamp_open
        self.timestamp_close= timestamp_close
