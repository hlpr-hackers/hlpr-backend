from concurrent import futures
import time
import math
import logging

import grpc

from hlpr.services.stubs import user_pb2, user_pb2_grpc

class UserServicer(user_pb2_grpc.UserServiceServicer):
    """Provides methods that implement functionality of user server."""

    def __init__(self):
         # Create database connection
        self.connection = conn._connect()

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

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()