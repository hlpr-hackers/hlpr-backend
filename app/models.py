import datetime

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    joined = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    address = db.Column(db.String(256), index=True, unique=True)  # or addressmodel.address


class Helper(User):
    def __init__(self):
        super().__init__()


class Shopper(User):
    def __init__(self):
        super().__init__()


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64), index=True, unique=True)


class Rating(db.Model):
    pass
