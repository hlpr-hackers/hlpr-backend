from concurrent import futures
import time
import math
import logging

import grpc

from hlpr.services.stubs import user_pb2, user_pb2_grpc
from hlpr.services.db import conn, models

class UserServicer(user_pb2_grpc.UserServiceServicer):
    """Provides methods that implement functionality of user server."""

    def __init__(self):
         # Create database connection
        pass

    def Create(self, request, context):
        pass

    def Delete(self, request, context):
        pass

    def Nearby(self, request, context):
        pass

    def Reviews(self, request, context):
        pass

    def SubmitReview(self, request, context):
        pass

    def UpdateScore(self, request, context):
        pass

    def UserTags(self, request, context):
        pass

    def UserTasks(self, request, context):
        pass
