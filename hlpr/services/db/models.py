from sqlalchemy import Column, Integer, String, DateTime, Float
import datetime
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

ENGINE = create_engine("sqlite:///helpr.db", echo=True)
BASE = declarative_base()


class User(BASE):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    phone_number = Column(String(24), index=True, unique=True)
    country = Column(String(64), index=True, unique=True)
    postCode = Column(Integer)
    joined = Column(DateTime, default=datetime.datetime.utcnow())
    lat = Column(Float)
    lon = Column(Float)


class Helper(User):
    __tablename__ = "helper"
    id = Column(Integer, primary_key=True)
    avg_rating = Column(Float)
    tasks = relationship("Task", backref="helper", lazy="select")
    rating = relationship("Rating", backref="helper", lazy="select")
    reviews = Column(String(512))

    def __str__(self):
        return f"User {self.name} {Helper.__tablename__}, rating {self.rating}"


class Shopper(User):
    __tablename__ = "shopper"
    id = Column(Integer, primary_key=True)
    tasks = relationship("Task", backref="shopper", lazy="select")
    review = relationship("Rating", backref="shopper", lazy="select")

    def __str__(self):
        return f"User {self.name} {Shopper.__tablename__}"

    def create_task(self):
        pass


class Task(BASE):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), index=True, nullable=False)
    description = Column(String(512))
    shopperId = Column(Integer, ForeignKey("shopper.id"), nullable=True)
    helperId = Column(Integer, ForeignKey("helper.id"), nullable=True)
    status = Column(String(64))
    submission_tstamp = Column(DateTime, default=datetime.datetime.utcnow())
    completed_tstamp = Column(DateTime, default=datetime.datetime.utcnow())
    tag = Column(String(64))
    points = Column(Integer, nullable=False)

    def __str__(self):
        return (
            f"Task: {self.task}, created by {self.shopper} is picked up by "
            f"{self.helper}"
        )


class Rating(BASE):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    review = Column(String(512))
    helperId = Column(Integer, ForeignKey("helper.id"), nullable=False)
    shopperId = Column(Integer, ForeignKey("shopper.id"), nullable=False)


BASE.metadata.create_all(ENGINE)
