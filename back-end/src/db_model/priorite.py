from .db import db
from .priorite_reader import priorite_reader
class Priorite(db.Model):
    __tablename__ = "priorite"
    id = db.Column('id',db.Integer , primary_key=True)
    fc_code = db.Column('fc_code',db.String(2))
    group_id =db.Column('group_id',db.String(50))
    rank = db.Column('rank',db.Integer)

    def __init__(self ,fc_code, group_id, rank):
        self.fc_code= fc_code
        self.group_id= group_id
        self.rank = rank
