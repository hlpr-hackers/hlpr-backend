import random
import logging

import grpc

from hlpr.services.stubs import task_pb2, task_pb2_grpc, user_pb2, user_pb2_grpc


def create_task(task_stub, task):
    feature = task_stub.Create(task_pb2.CreateTaskRequest(**task))
    print(f"{task} Created!")


def run():
    task = dict(
        name="task1", description="I need help", tag="food", points=10, UUID="0738491"
    )
    with grpc.insecure_channel("localhost:50051") as channel:
        task_stub = task_pb2_grpc.TaskServiceStub(channel)
        # user_stub = user_pb2_grpc.UserServiceStub(channel)
        print("---------CREATE TASK--------------")
        create_task(task_stub, task)


if __name__ == "__main__":
    logging.basicConfig()
    run()
