
from .db import db
class AdminCsteHyst(db.Model):
    __tablename__ = "admin_constante_hyst"
    id = db.Column('id',db.Integer , primary_key=True)
    cste_name = db.Column('cste_name',db.String(100))
    cste_type = db.Column('cste_type', db.String(100))
    value = db.Column('value' , db.Float)
    timestamp= db.Column('timestamp' , db.DateTime)
    user_id = db.Column('user_id',db.Integer)

    def __init__(self ,cste_name ,cste_type ,value,timestamp,user_id):
        self.cste_name=cste_name
        self.cste_type=cste_type
        self.value=value
        self.timestamp = timestamp
        self.user_id=user_id
