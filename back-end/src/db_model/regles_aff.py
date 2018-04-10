

from .db import db
from .regle_aff_reader import regle_aff_reader
class RegleAff(db.Model):
    __tablename__ = "regle_aff"
    drag_capacity_from = db.Column('drag_capacity_from',db.String(100) , primary_key=True)
    drag_capacity_to = db.Column('drag_capacity_to',db.String(100))
    drag_type =  db.Column('drag_type',db.String(100))
    drag_value =  db.Column('drag_value',db.Float)
    propagation =  db.Column('propagation',db.String(10))
    condition_type =  db.Column('condition_type',db.String(100))
    condition_value =  db.Column('condition_value',db.String(100))

    def __init__(self ,drag_capacity_from,drag_capacity_to,drag_type,drag_value,propagation,condition_type,condition_value):
        self.drag_capacity_from= drag_capacity_from
        self.drag_capacity_to = drag_capacity_to
        self.drag_type = drag_type
        self.drag_value = drag_value
        self.propagation = propagation
        self.condition_type=condition_type
        self.condition_value=condition_value
