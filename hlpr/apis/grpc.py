import os
import time
import logging
from concurrent import futures
import grpc

from hlpr.services.stubs import task_pb2, task_pb2_grpc, user_pb2, user_pb2_grpc
from hlpr.services.servicers import (
    TaskServicer, UserServicer)

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
logging.basicConfig(level=logging.INFO)


def serve():
    """Start grpc server servicing FMS RPCs."""
    # create grpc server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    task_pb2_grpc.add_TaskServiceServicer_to_server(
        TaskServicer(), server)

    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserServicer(), server)

    # start server
    # address = '%s:%s' % (os.environ['HOST'], os.environ['PORT'])
    # logging.info('Starting grpc server at %s', address)
    # server.add_insecure_port(address)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

    # mark server as healthy
    #logging.info('grpc listening at %s', address)

    # start() does not block so sleep-loop
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()