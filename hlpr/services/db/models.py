from sqlalchemy import Column, Integer, String, DateTime, Float
import datetime
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

ENGINE = create_engine("sqlite:///my.db", echo=True)
BASE = declarative_base()


class User(BASE):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True, unique=True)
    country = Column(String(64), index=True, unique=True)
    postCode = Column(Integer)
    registered = Column(DateTime, default=datetime.datetime.utcnow)
    lat = Column(Float)
    lon = Column(Float)


class Helper(User):
    __tablename__ = "helper"
    id = Column(Integer, primary_key=True)
    tasks = relationship("Service", backref="helper", lazy="select")
    rating = relationship("Rating", backref="helper", lazy="select")

    def __str__(self):
        return f"User {self.name} {Helper.__tablename__}, rating {self.rating}"


class Shopper(User):
    __tablename__ = "shopper"
    id = Column(Integer, primary_key=True)
    tasks = relationship("Service", backref="shopper", lazy="select")

    def __str__(self):
        return f"User {self.name} {Shopper.__tablename__}"


class Service(BASE):
    __tablename__ = "service"
    id = Column(Integer, primary_key=True)
    task = Column(String(256), index=True)
    shopperId = Column(Integer, ForeignKey("shopper.id"), nullable=True)
    helperId = Column(Integer, ForeignKey("helper.id"), nullable=True)

    def __str__(self):
        return (
            f"Task: {self.task}, created by {self.shopper} is picked up by "
            f"{self.helper}"
        )


class Rating(BASE):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String(512))
    helperId = Column(Integer, ForeignKey("helper.id"), nullable=False)


BASE.metadata.create_all(ENGINE)
