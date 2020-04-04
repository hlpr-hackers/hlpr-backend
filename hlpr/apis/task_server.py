from concurrent import futures
import time
import math
import logging

import grpc

import task_pb2
import task_pb2_grpc


class TaskServicer(task_pb2_grpc.TaskServiceServicer):
    """Provides methods that implement functionality of task server."""

    def __init__(self):
         # Create database connection
        self.connection = conn._connect()

    def Create(self, request, context): 
        pass

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


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    task_pb2_grpc.add_TaskServiceServicer_to_server(
        TaskServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()    