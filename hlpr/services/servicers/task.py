from concurrent import futures
import time
import math
import logging
import sys
import grpc
from sqlalchemy.orm import sessionmaker
from hlpr.services.stubs import task_pb2, task_pb2_grpc
from hlpr.services.db.models import Citizen, Helper, Task
from hlpr.services.db import conn
from sqlalchemy import create_engine
import sqlalchemy.ext.declarative
import datetime
import uuid
from google.protobuf.timestamp_pb2 import Timestamp

class TaskServicer(task_pb2_grpc.TaskServiceServicer):
    """Provides methods that implement functionality of task server."""

    def __init__(self):
        # Create database connection

        self.engine = create_engine(
            "sqlite:///helpr.db", echo=True
        )
        SESSION = sessionmaker(bind=self.engine)
        self.session = SESSION()


    def Create(self, request, context):
        session = self.session
        citizen = session.query(Citizen).filter(
            Citizen.phone_number == request.UUID
        ).first()
        tasks = session.query(Task).all()
        task = Task()
        task.UUID = str(uuid.uuid1())
        task.name = request.name
        task.description = request.description
        task.points = request.points
        task.status = "open"
        task.submission_tstamp = datetime.datetime.utcnow()
        task.completed_tstamp = None
        task.tag = request.tag
        citizen.tasks.append(task)
        session.add_all([task, citizen])
        session.commit()
        return task_pb2.Task(
            id=task.UUID,
            name=task.name,
            status=task.status,
            description = task.description,
            tag = task.tag,
            points = task.points,
            submission_tstamp = Timestamp().GetCurrentTime(),
            completed_tstamp = Timestamp().GetCurrentTime()
        )

    def Delete(self, request, context):
        pass

    def Nearby(self, request, context):
        pass

    def Assign(self, request, context):
        pass

    def SetStatus(self, request, context):
        pass

    def ListTags(self, request, context):
        pass
