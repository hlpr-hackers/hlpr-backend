import random
import logging
import argparse

import grpc

from hlpr.services.stubs import task_pb2, task_pb2_grpc, user_pb2, user_pb2_grpc

def create_task(task_stub, task):
    feature = task_stub.Create(task_pb2.CreateTaskRequest(**task))
    print(f'{task} Created!')

def run(host, port):

    task = dict(name='task1', description='I need help' , tag='food', points=10)
    with grpc.insecure_channel(f'{host}:{port}') as channel:
        task_stub = task_pb2_grpc.TaskServiceStub(channel)
        # user_stub = user_pb2_grpc.UserServiceStub(channel)
        print('---------CREATE TASK--------------')
        create_task(task_stub, task)
   

if __name__ == '__main__':
    logging.basicConfig()
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--host', default='localhost', help='The host to connect to')
    parser.add_argument(
        '--port', type=int, default=8000, help='The port to connect to')
    parser.add_argument(
        '--timeout', type=int, default=10, help='The call timeout, in seconds')
    args = parser.parse_args()
    run(args.host, args.port)