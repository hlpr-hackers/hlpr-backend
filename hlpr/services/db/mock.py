import datetime
from sqlalchemy import create_engine
from models import Helper, Shopper, Task, Rating
from sqlalchemy.orm import sessionmaker
import sys
import random

def drop_all(eng):
    try:
        Helper.__table__.drop(eng)
        Shopper.__table__.drop(eng)
        Rating.__table__.drop(eng)
        print("Database dropped")
    except Exception as e:
        print(f"Failed to drop database {e}")


def create_helper(session, helpers):
    for name, attrib in helpers.items():
        helper = Helper()
        helper.name = name
        helper.phone_number = attrib[0]
        helper.avg_rating = attrib[1]
        helper.postCode = attrib[2]
        helper.joined = attrib[3]
        session.add(helper)
        session.commit()


def create_shopper(session, shoppers):
    for name, attrib in shoppers.items():
        shopper = Shopper()
        shopper.name = name
        shopper.phone_number = attrib[0]
        shopper.postCode = attrib[1]
        shopper.joined = attrib[2]
        session.add(shopper)
        session.commit()


def create_task(session, tasks):
    for task_name, attrib in tasks.items():
        phone_num = attrib[4]
        shopper = (
            session.query(Shopper).filter(Shopper.phone_number == phone_num).first()
        )
        task = Task()
        task.name = task_name
        task.status = attrib[0]
        task.submision_timestamp = attrib[1]
        task.tag = attrib[2]
        task.points = attrib[3]
        task.shopperId = shopper.id
        shopper.tasks.append(task)
        session.add_all([task, shopper])
        session.commit()


def assign_tasks(session, helpers):
    tasks = session.query(Task).all()
    for helper_num in helpers:
        helper = session.query(Helper).filter(Helper.phone_number == helper_num).first()
        task = random.choice(tasks)
        tasks.remove(task)
        task.helperId = helper.id
        helper.tasks.append(task)
        session.add_all([task, helper])
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
        z[0]: list(z[1:])
        for z in zip(
            helpers, helper_numbers, helper_ratings, helper_post_codes, helper_joined
        )
    }

    shoppers = ["granma", "granpa"]
    shopper_numbers = ["0738492", "0738491"]
    shooper_post_codes = ["41720", "41721"]
    shopper_joined = [
        time_now - datetime.timedelta(3),
        time_now - datetime.timedelta(6),
    ]

    shoppers_collection = {
        z[0]: list(z[1:])
        for z in zip(shoppers, shopper_numbers, shooper_post_codes, shopper_joined)
    }

    tasks = ["Take out garbage", "Walk the dog"]
    task_status = ["open", "open"]
    task_submision_timestamp = [
        time_now - datetime.timedelta(1),
        time_now - datetime.timedelta(2),
    ]
    task_tags = ["homehelp", "pethelp"]
    task_points = [4, 3]
    requested_by = shopper_numbers

    tasks_collection = {
        z[0]: list(z[1:])
        for z in zip(
            tasks, task_status, task_submision_timestamp, task_tags, task_points, requested_by
        )
    }

    SESSION = sessionmaker(bind=engine)
    session = SESSION()
    ## Drop the table. To recreate a table run `python models.py`
    # drop_all(engine)

    ## Uncomment lines below to populate database with sample data
    # create_helper(session, helpers_collection)
    # create_shopper(session, shoppers_collection)
    # create_task(session, tasks_collection)
    # helpers = random.sample(helper_numbers, 2)
    # assign_tasks(session, helpers)
