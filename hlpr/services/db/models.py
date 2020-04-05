from sqlalchemy import Column, Integer, String, DateTime, Float
import datetime
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid

ENGINE = create_engine("sqlite:///helpr.db", echo=True)
BASE = declarative_base()


class User(BASE):
    __abstract__ = True
    UUID = Column(String(64), primary_key=True)
    name = Column(String(64), unique=False)
    phone_number = Column(String(24), index=True, unique=True)
    country = Column(String(64), index=True, unique=True)
    postCode = Column(Integer)
    joined = Column(DateTime, default=datetime.datetime.utcnow())
    lat = Column(Float)
    lon = Column(Float)


class Helper(User):
    __tablename__ = "helper"
    UUID = Column(String(64), primary_key=True)
    avg_rating = Column(Float)
    tasks = relationship("Task", backref="helper", lazy="select")
    reviews = relationship("Reviews", backref="helper", lazy="select")

    def __str__(self):
        return f"User {self.name} {Helper.__tablename__}, reviews {self.reviews}"


class Bounty:
    pass

class Citizen(User):
    __tablename__ = "citizen"
    UUID = Column(String(64), primary_key=True)
    tasks = relationship("Task", backref="citizen", lazy="select")
    review = relationship("Reviews", backref="citizen", lazy="select")

    def __str__(self):
        return f"User {self.name} {Citizen.__tablename__}"

    def create_task(self):
        pass


class Task(BASE):
    __tablename__ = "tasks"
    UUID = Column(String(64), primary_key=True)
    name = Column(String(256), index=True, nullable=False)
    description = Column(String(512))
    citizenId = Column(Integer, ForeignKey("citizen.UUID"), nullable=True)
    helperId = Column(Integer, ForeignKey("helper.UUID"), nullable=True)
    status = Column(String(64))
    submission_tstamp = Column(DateTime, default=datetime.datetime.utcnow())
    completed_tstamp = Column(DateTime, default=datetime.datetime.utcnow())
    tag = Column(String(64))
    points = Column(Integer, nullable=False)

    def __str__(self):
        return (
            f"Task: {self.task}, created by {self.citizen} is picked up by "
            f"{self.helper}"
        )


class Reviews(BASE):
    __tablename__ = "reviews"
    UUID = Column(String(64), primary_key=True)
    score = Column(Integer)
    review = Column(String(512))
    helperId = Column(Integer, ForeignKey("helper.UUID"), nullable=False)
    citizenId = Column(Integer, ForeignKey("citizen.UUID"), nullable=False)


BASE.metadata.create_all(ENGINE)
