from .db import db

class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column('id',db.Integer , primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship("User", backref=db.backref("user", uselist=False))

    def __init__(self , user_id):
        self.user_id = user_id
