from concurrent import futures
import time
import math
import logging

import grpc

from hlpr.services.stubs import task_pb2, task_pb2_grpc
from hlpr.services.db import conn, models

class TaskServicer(task_pb2_grpc.TaskServiceServicer):
    """Provides methods that implement functionality of task server."""

    def __init__(self):
         # Create database connection
        self.connection = conn._connect()

    def Create(self, request, context):
        print(request)
        return

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
