import datetime
from sqlalchemy import create_engine
import conn
from models import User, Helper, Shopper, Task, Rating
from sqlalchemy.orm import sessionmaker
import sys


def drop_all(eng):
    try:
        Helper.__table__.drop(eng)
        Shopper.__table__.drop(eng)
        Rating.__table__.drop(eng)
        print("Database dropped")
    except Exception as e:
        print(f"Failed to drop database {e}")


def create_helper(session):
    helper = Helper()
    helper.name = "george"
    helper.avg_rating = 4.7
    helper.phone_number = "12345567"
    helper.postCode = "41720"
    helper.joined = datetime.datetime.now()
    session.add(helper)
    session.commit()


if __name__ == "__main__":
    try:
        engine = create_engine("sqlite:///helpr.db", echo=True)
        conn = engine.connect()
        print(f"Connected to: {conn}")
    except Exception as e:
        print(f"connection failed {e}")
        sys.exit(1)

    SESSION = sessionmaker(bind=engine)
    session = SESSION()
    create_helper(session)
    drop_all(engine)
