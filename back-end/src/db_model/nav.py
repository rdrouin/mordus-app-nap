from .db import db

class Nav(db.Model):
    __tablename__ = "nav"
    id = db.Column('id',db.Integer , primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship("User", backref=db.backref("user_nav", uselist=False))

    def __init__(self , user_id):
        self.user_id = user_id
