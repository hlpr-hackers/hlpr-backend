# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import user_pb2 as user__pb2


class UserServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/user.v1.UserService/Create',
        request_serializer=user__pb2.CreateUserRequest.SerializeToString,
        response_deserializer=user__pb2.User.FromString,
        )
    self.Delete = channel.unary_unary(
        '/user.v1.UserService/Delete',
        request_serializer=user__pb2.DeleteUserRequest.SerializeToString,
        response_deserializer=user__pb2.User.FromString,
        )
    self.Nearby = channel.unary_unary(
        '/user.v1.UserService/Nearby',
        request_serializer=user__pb2.NearbyRequest.SerializeToString,
        response_deserializer=user__pb2.NearbyResult.FromString,
        )
    self.Reviews = channel.unary_unary(
        '/user.v1.UserService/Reviews',
        request_serializer=user__pb2.ReviewRequest.SerializeToString,
        response_deserializer=user__pb2.ReviewResponse.FromString,
        )
    self.SubmitReview = channel.unary_unary(
        '/user.v1.UserService/SubmitReview',
        request_serializer=user__pb2.SubmitReviewRequest.SerializeToString,
        response_deserializer=user__pb2.Review.FromString,
        )
    self.UpdateScore = channel.unary_unary(
        '/user.v1.UserService/UpdateScore',
        request_serializer=user__pb2.UpdateScoreRequest.SerializeToString,
        response_deserializer=user__pb2.User.FromString,
        )
    self.UserTags = channel.unary_unary(
        '/user.v1.UserService/UserTags',
        request_serializer=user__pb2.UserTagsRequest.SerializeToString,
        response_deserializer=user__pb2.TagsResult.FromString,
        )
    self.UserTasks = channel.unary_unary(
        '/user.v1.UserService/UserTasks',
        request_serializer=user__pb2.UserTaskRequest.SerializeToString,
        response_deserializer=user__pb2.TaskResult.FromString,
        )


class UserServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

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

  def Nearby(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Reviews(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubmitReview(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateScore(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UserTags(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UserTasks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=user__pb2.CreateUserRequest.FromString,
          response_serializer=user__pb2.User.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=user__pb2.DeleteUserRequest.FromString,
          response_serializer=user__pb2.User.SerializeToString,
      ),
      'Nearby': grpc.unary_unary_rpc_method_handler(
          servicer.Nearby,
          request_deserializer=user__pb2.NearbyRequest.FromString,
          response_serializer=user__pb2.NearbyResult.SerializeToString,
      ),
      'Reviews': grpc.unary_unary_rpc_method_handler(
          servicer.Reviews,
          request_deserializer=user__pb2.ReviewRequest.FromString,
          response_serializer=user__pb2.ReviewResponse.SerializeToString,
      ),
      'SubmitReview': grpc.unary_unary_rpc_method_handler(
          servicer.SubmitReview,
          request_deserializer=user__pb2.SubmitReviewRequest.FromString,
          response_serializer=user__pb2.Review.SerializeToString,
      ),
      'UpdateScore': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateScore,
          request_deserializer=user__pb2.UpdateScoreRequest.FromString,
          response_serializer=user__pb2.User.SerializeToString,
      ),
      'UserTags': grpc.unary_unary_rpc_method_handler(
          servicer.UserTags,
          request_deserializer=user__pb2.UserTagsRequest.FromString,
          response_serializer=user__pb2.TagsResult.SerializeToString,
      ),
      'UserTasks': grpc.unary_unary_rpc_method_handler(
          servicer.UserTasks,
          request_deserializer=user__pb2.UserTaskRequest.FromString,
          response_serializer=user__pb2.TaskResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'user.v1.UserService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))