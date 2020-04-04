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




def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    route_guide_pb2_grpc.add_RouteGuideServicer_to_server(
        RouteGuideServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()    