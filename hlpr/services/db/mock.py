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


def create_shopper(session):
    shopper = Shopper()
    shopper.name = "granma3"
    shopper.phone_number = "870231284"
    shopper.postCode = "41720"
    shopper.joined = datetime.datetime.now()
    session.add(shopper)
    session.commit()


def create_task(session, User):
    shopper = session.query(Shopper).filter(Shopper.phone_number == "8702384").first()
    task = Task()
    task.name = "Take out garbage"
    task.status = "open"
    task.submision_timestamp = datetime.datetime.utcnow()
    task.tag = "homehelp"
    task.points = 3
    task.shopperId = shopper.id
    shopper.task = task
    session.add_all([task, shopper])
    session.commit()


if __name__ == "__main__":
    try:
        engine = create_engine("sqlite:///helpr.db", echo=True)
        conn = engine.connect()
        print(f"Connected to: {conn}")
    except Exception as e:
        print(f"connection failed {e}")
        sys.exit(1)

    time_now = datetime.datetime.utcnow()
    helpers = ["george", "leo", "carolina", "oriol", "ashwin", "vijai"]
    helper_numbers = ["3412543", "3560985", "0843567", "0892749", "1236125", "6093532"]
    helper_ratings = [5, 5, 5, 5, 5, 5]
    helper_post_codes = ["41720", "41721", "41722", "41723", "41724", "41725"]
    helper_joined = [
        time_now,
        time_now - datetime.timedelta(2),
        time_now - datetime.timedelta(3),
        time_now - datetime.timedelta(4),
        time_now - datetime.timedelta(5),
        time_now - datetime.timedelta(6),
    ]
    helpers_collection = {
        "helpers": helpers,
        "helper_numbers": helper_numbers,
        "helper_ratings": helper_ratings,
        "helper_post_codes": helper_post_codes,
        "helper_joined": helper_joined,
    }

    shoppers = ["granma", "granpa"]
    shoppers_numbers = ['0738492', '0738491']
    # shopper.phone_number = "870231284"
    # shopper.postCode = "41720"
    # shopper.joined = datetime.datetime.now()
    # session.add(shopper)

    SESSION = sessionmaker(bind=engine)
    session = SESSION()
    # create_helper(session)
    # create_shopper(session)
    # drop_all(engine)
    create_task(session, Shopper)
