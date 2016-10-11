from src.ext import db
from flask_login import UserMixin


class UserModel(UserMixin, db.Model):
    __tablename__ = "rookie"
    id_ = db.column(db.Integer, primary_key=True)
    rookie_name = db.Column(db.Unicode(20))
    rookie_family = db.Column(db.Unicode(30))
    rookie_contact = db.Column(db.Unicode(30))

    @classmethod
    def set_user_model(cls, name, family, contact):
        return cls(rookie_name=name, rookie_family=family, rookie_contact=contact)

