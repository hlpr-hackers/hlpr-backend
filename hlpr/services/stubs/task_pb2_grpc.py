# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import task_pb2 as task__pb2


class TaskServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Nearby = channel.unary_unary(
        '/task.v1.TaskService/Nearby',
        request_serializer=task__pb2.NearbyRequest.SerializeToString,
        response_deserializer=task__pb2.NearbyResult.FromString,
        )
    self.Create = channel.unary_unary(
        '/task.v1.TaskService/Create',
        request_serializer=task__pb2.CreateTaskRequest.SerializeToString,
        response_deserializer=task__pb2.Task.FromString,
        )
    self.Delete = channel.unary_unary(
        '/task.v1.TaskService/Delete',
        request_serializer=task__pb2.DeleteTaskRequest.SerializeToString,
        response_deserializer=task__pb2.Task.FromString,
        )
    self.Assign = channel.unary_unary(
        '/task.v1.TaskService/Assign',
        request_serializer=task__pb2.AssignTaskRequest.SerializeToString,
        response_deserializer=task__pb2.Task.FromString,
        )
    self.SetStatus = channel.unary_unary(
        '/task.v1.TaskService/SetStatus',
        request_serializer=task__pb2.SetStatusRequest.SerializeToString,
        response_deserializer=task__pb2.Task.FromString,
        )
    self.ListTags = channel.unary_unary(
        '/task.v1.TaskService/ListTags',
        request_serializer=task__pb2.TagsRequest.SerializeToString,
        response_deserializer=task__pb2.TagsResult.FromString,
        )


class TaskServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Nearby(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Assign(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTags(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TaskServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Nearby': grpc.unary_unary_rpc_method_handler(
          servicer.Nearby,
          request_deserializer=task__pb2.NearbyRequest.FromString,
          response_serializer=task__pb2.NearbyResult.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=task__pb2.CreateTaskRequest.FromString,
          response_serializer=task__pb2.Task.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=task__pb2.DeleteTaskRequest.FromString,
          response_serializer=task__pb2.Task.SerializeToString,
      ),
      'Assign': grpc.unary_unary_rpc_method_handler(
          servicer.Assign,
          request_deserializer=task__pb2.AssignTaskRequest.FromString,
          response_serializer=task__pb2.Task.SerializeToString,
      ),
      'SetStatus': grpc.unary_unary_rpc_method_handler(
          servicer.SetStatus,
          request_deserializer=task__pb2.SetStatusRequest.FromString,
          response_serializer=task__pb2.Task.SerializeToString,
      ),
      'ListTags': grpc.unary_unary_rpc_method_handler(
          servicer.ListTags,
          request_deserializer=task__pb2.TagsRequest.FromString,
          response_serializer=task__pb2.TagsResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'task.v1.TaskService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))