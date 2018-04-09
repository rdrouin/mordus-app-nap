from .db import db
class AttributionConfirme(db.Model):
    __tablename__ = "attConf"
    id_att_prel = db.Column('id_att_prel',db.Integer , primary_key=True)
    status = db.Column('status',db.String(30))
    vol_id = db.Column('status',db.String(50))

def __init__(self ,id ,fc):
    self.id_att_prel=id_att_prel
    self.status= status
    self.vol_id= vol_id
