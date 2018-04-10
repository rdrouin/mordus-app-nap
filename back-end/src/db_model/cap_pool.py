from .db import db
from .cap_pool_reader import cap_pool_reader
class CapPool(db.Model):
    __tablename__ = "cap_pool"
    id_cap_pool = db.Column('id_cap_pool',db.Integer , primary_key=True)
    cap_pool_name = db.Column('cap_pool_name',db.String(50))

    def __init__(self ,cap_pool_name):
        self.cap_pool_name= cap_pool_name
