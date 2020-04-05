import argparse
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


def serve(port, shutdown_grace_duration):
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

    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()

    print('Listening on port {}'.format(port))

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(shutdown_grace_duration)

if __name__ == '__main__':
    logging.basicConfig()
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--port', type=int, default=None,
        help='The port to listen on.'
             'If arg is not set, will listen on the $PORT env var.'
             'If env var is empty, defaults to 8000.')
    parser.add_argument(
        '--shutdown_grace_duration', type=int, default=5,
        help='The shutdown grace duration, in seconds')

    args = parser.parse_args()

    port = args.port
    if not port:
        port = os.environ.get('PORT')
    if not port:
        port = 8000

    serve(port, args.shutdown_grace_duration)