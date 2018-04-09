from .db import db
class CapPool(db.Model):
    __tablename__ = "cap_pool"
    id_cap_pool = db.Column('id_cap_pool',db.Integer , primary_key=True)
    cap_pool_name = db.Column('cap_pool_name',db.String(50))

def __init__(self ,id ,fc):
    self.id_cap_pool=id_cap_pool
    self.cap_pool_name= cap_pool_name

    for line in result:
        cap_pool = CapPool(line['id_cap_pool'], line['cap_pool_name'])
        db.session.add(cap_pool)
        db.session.commit()
