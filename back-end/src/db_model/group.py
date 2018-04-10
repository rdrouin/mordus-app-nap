from .db import db
from .group_reader import group_reader
class Group(db.Model):
    __tablename__ = "priority_group"
    id_group = db.Column('id_group',db.Integer , primary_key=True)
    group_name = db.Column('group_name',db.String(50))
    group_type =db.Column('group_type',db.String(50))

    def __init__(self ,group_name,group_type):
        self.group_name= group_name
        self.group_type= group_type
