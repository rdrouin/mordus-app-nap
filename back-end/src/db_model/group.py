from .db import db
class Group(db.Model):
    __tablename__ = "group"
    id_group = db.Column('id_group',db.Integer , primary_key=True)
    group_name = db.Column('group_name',db.String(50))
    group_type =db.Column('group_type',db.String(50))

def __init__(self ,id ,fc):
    self.id_group=id_group
    self.group_name= group_name
    self.group_type= group_type

    for line in result:
        group = CapHoraire(line['id_group'], line['group_name'], line['group_type'])
        db.session.add(group)
        db.session.commit()
