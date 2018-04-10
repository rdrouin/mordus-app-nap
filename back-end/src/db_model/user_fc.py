from .db import db

class User_Fc(db.Model):
    __tablename__ = "user_fc"
    id = db.Column('id',db.Integer , primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    fc = db.Column('fc', db.String(2),)
    user = db.relationship("User", backref=db.backref("user_fc", uselist=False))

    def __init__(self , user_id, fc):
        self.user_id = user_id
        self.fc = fc
