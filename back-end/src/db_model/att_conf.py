from .db import db
class AttributionConfirme(db.Model):
    __tablename__ = "att_conf"
    id_att_conf = db.Column('id_att_conf',db.Integer , primary_key=True)
    vol_id = db.Column('vol_id',db.String(50))
    fc_name = db.Column('fc_name',db.String(50))

    def __init__(self ,vol ,fc):
        self.vol_id= vol
        self.fc_name= fc
