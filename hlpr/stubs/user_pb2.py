# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import task_pb2 as task__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='user.proto',
  package='user.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nuser.proto\x12\x07user.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\ntask.proto\"T\n\x11\x43reateUserRequest\x12\x1b\n\x04role\x18\x01 \x01(\x0e\x32\r.user.v1.Role\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cphone_number\x18\x03 \x01(\x05\"3\n\x11\x44\x65leteUserRequest\x12\x1e\n\x07user_id\x18\x01 \x01(\x0b\x32\r.user.v1.UUID\"V\n\rNearbyRequest\x12\x0b\n\x03lat\x18\x01 \x01(\x02\x12\x0b\n\x03lon\x18\x02 \x01(\x02\x12\x0e\n\x06radius\x18\x03 \x01(\x05\x12\x1b\n\x04role\x18\x04 \x01(\x0e\x32\r.user.v1.Role\",\n\x0cNearbyResult\x12\x1c\n\x05users\x18\x01 \x03(\x0b\x32\r.user.v1.User\"/\n\rReviewRequest\x12\x1e\n\x07user_id\x18\x01 \x01(\x0b\x32\r.user.v1.UUID\"2\n\x0eReviewResponse\x12 \n\x07reviews\x18\x01 \x03(\x0b\x32\x0f.user.v1.Review\"U\n\x13SubmitReviewRequest\x12\x1e\n\x07user_id\x18\x01 \x01(\x0b\x32\r.user.v1.UUID\x12\x0e\n\x06review\x18\x02 \x01(\t\x12\x0e\n\x06rating\x18\x03 \x01(\x05\"C\n\x12UpdateScoreRequest\x12\x1e\n\x07user_id\x18\x01 \x01(\x0b\x32\r.user.v1.UUID\x12\r\n\x05value\x18\x02 \x01(\x05\"1\n\x0fUserTagsRequest\x12\x1e\n\x07user_id\x18\x01 \x01(\x0b\x32\r.user.v1.UUID\"\x1a\n\nTagsResult\x12\x0c\n\x04tags\x18\x01 \x03(\t\"R\n\x0fUserTaskRequest\x12\x1e\n\x07user_id\x18\x01 \x01(\x0b\x32\r.user.v1.UUID\x12\x1f\n\x06status\x18\x02 \x01(\x0e\x32\x0f.task.v1.Status\"*\n\nTaskResult\x12\x1c\n\x05tasks\x18\x01 \x03(\x0b\x32\r.task.v1.Task\"\x15\n\x04UUID\x12\r\n\x05value\x18\x01 \x01(\t\"\xc5\x02\n\x04User\x12\x19\n\x02id\x18\x01 \x01(\x0b\x32\r.user.v1.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cphone_number\x18\x03 \x01(\x05\x12\x31\n\rjoined_tstamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x04role\x18\x05 \x01(\x0e\x32\r.user.v1.Role\x12\x12\n\navg_rating\x18\x06 \x01(\x02\x12\r\n\x05score\x18\x07 \x01(\x05\x12\x0c\n\x04\x63ity\x18\x08 \x01(\t\x12\x0f\n\x07\x63ountry\x18\t \x01(\t\x12\x12\n\npostalCode\x18\n \x01(\t\x12\x0b\n\x03lat\x18\x0b \x01(\x02\x12\x0b\n\x03lon\x18\x0c \x01(\x02\x12 \n\x07reviews\x18\r \x01(\x0b\x32\x0f.user.v1.Review\x12\x1c\n\x05tasks\x18\x0e \x01(\x0b\x32\r.task.v1.Task\"w\n\x06Review\x12\x19\n\x02id\x18\x01 \x01(\x0b\x32\r.user.v1.UUID\x12\x0e\n\x06review\x18\x02 \x01(\t\x12\x0e\n\x06rating\x18\x03 \x01(\x05\x12\x32\n\x0e\x63reated_tstamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*\x1b\n\x04Role\x12\x08\n\x04HLPR\x10\x00\x12\t\n\x05NEEDR\x10\x01\x32\xed\x03\n\x0bUserService\x12\x35\n\x06\x43reate\x12\x1a.user.v1.CreateUserRequest\x1a\r.user.v1.User\"\x00\x12\x35\n\x06\x44\x65lete\x12\x1a.user.v1.DeleteUserRequest\x1a\r.user.v1.User\"\x00\x12\x39\n\x06Nearby\x12\x16.user.v1.NearbyRequest\x1a\x15.user.v1.NearbyResult\"\x00\x12<\n\x07Reviews\x12\x16.user.v1.ReviewRequest\x1a\x17.user.v1.ReviewResponse\"\x00\x12?\n\x0cSubmitReview\x12\x1c.user.v1.SubmitReviewRequest\x1a\x0f.user.v1.Review\"\x00\x12;\n\x0bUpdateScore\x12\x1b.user.v1.UpdateScoreRequest\x1a\r.user.v1.User\"\x00\x12;\n\x08UserTags\x12\x18.user.v1.UserTagsRequest\x1a\x13.user.v1.TagsResult\"\x00\x12<\n\tUserTasks\x12\x18.user.v1.UserTaskRequest\x1a\x13.user.v1.TaskResult\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,task__pb2.DESCRIPTOR,])

_ROLE = _descriptor.EnumDescriptor(
  name='Role',
  full_name='user.v1.Role',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HLPR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEEDR', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1277,
  serialized_end=1304,
)
_sym_db.RegisterEnumDescriptor(_ROLE)

Role = enum_type_wrapper.EnumTypeWrapper(_ROLE)
HLPR = 0
NEEDR = 1



_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='user.v1.CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='user.v1.CreateUserRequest.role', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='user.v1.CreateUserRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='user.v1.CreateUserRequest.phone_number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=152,
)


_DELETEUSERREQUEST = _descriptor.Descriptor(
  name='DeleteUserRequest',
  full_name='user.v1.DeleteUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='user.v1.DeleteUserRequest.user_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=205,
)


_NEARBYREQUEST = _descriptor.Descriptor(
  name='NearbyRequest',
  full_name='user.v1.NearbyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='user.v1.NearbyRequest.lat', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='user.v1.NearbyRequest.lon', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius', full_name='user.v1.NearbyRequest.radius', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='user.v1.NearbyRequest.role', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=293,
)


_NEARBYRESULT = _descriptor.Descriptor(
  name='NearbyResult',
  full_name='user.v1.NearbyResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='user.v1.NearbyResult.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=339,
)


_REVIEWREQUEST = _descriptor.Descriptor(
  name='ReviewRequest',
  full_name='user.v1.ReviewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='user.v1.ReviewRequest.user_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=341,
  serialized_end=388,
)


_REVIEWRESPONSE = _descriptor.Descriptor(
  name='ReviewResponse',
  full_name='user.v1.ReviewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reviews', full_name='user.v1.ReviewResponse.reviews', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=440,
)


_SUBMITREVIEWREQUEST = _descriptor.Descriptor(
  name='SubmitReviewRequest',
  full_name='user.v1.SubmitReviewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='user.v1.SubmitReviewRequest.user_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='review', full_name='user.v1.SubmitReviewRequest.review', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rating', full_name='user.v1.SubmitReviewRequest.rating', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=442,
  serialized_end=527,
)


_UPDATESCOREREQUEST = _descriptor.Descriptor(
  name='UpdateScoreRequest',
  full_name='user.v1.UpdateScoreRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='user.v1.UpdateScoreRequest.user_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='user.v1.UpdateScoreRequest.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=596,
)


_USERTAGSREQUEST = _descriptor.Descriptor(
  name='UserTagsRequest',
  full_name='user.v1.UserTagsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='user.v1.UserTagsRequest.user_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=598,
  serialized_end=647,
)


_TAGSRESULT = _descriptor.Descriptor(
  name='TagsResult',
  full_name='user.v1.TagsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tags', full_name='user.v1.TagsResult.tags', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=649,
  serialized_end=675,
)


_USERTASKREQUEST = _descriptor.Descriptor(
  name='UserTaskRequest',
  full_name='user.v1.UserTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='user.v1.UserTaskRequest.user_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='user.v1.UserTaskRequest.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=677,
  serialized_end=759,
)


_TASKRESULT = _descriptor.Descriptor(
  name='TaskResult',
  full_name='user.v1.TaskResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='user.v1.TaskResult.tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=761,
  serialized_end=803,
)


_UUID = _descriptor.Descriptor(
  name='UUID',
  full_name='user.v1.UUID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='user.v1.UUID.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=805,
  serialized_end=826,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='user.v1.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.v1.User.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='user.v1.User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='user.v1.User.phone_number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='joined_tstamp', full_name='user.v1.User.joined_tstamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='user.v1.User.role', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avg_rating', full_name='user.v1.User.avg_rating', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='user.v1.User.score', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='city', full_name='user.v1.User.city', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country', full_name='user.v1.User.country', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postalCode', full_name='user.v1.User.postalCode', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lat', full_name='user.v1.User.lat', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='user.v1.User.lon', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reviews', full_name='user.v1.User.reviews', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='user.v1.User.tasks', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=829,
  serialized_end=1154,
)


_REVIEW = _descriptor.Descriptor(
  name='Review',
  full_name='user.v1.Review',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.v1.Review.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='review', full_name='user.v1.Review.review', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rating', full_name='user.v1.Review.rating', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_tstamp', full_name='user.v1.Review.created_tstamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1156,
  serialized_end=1275,
)

_CREATEUSERREQUEST.fields_by_name['role'].enum_type = _ROLE
_DELETEUSERREQUEST.fields_by_name['user_id'].message_type = _UUID
_NEARBYREQUEST.fields_by_name['role'].enum_type = _ROLE
_NEARBYRESULT.fields_by_name['users'].message_type = _USER
_REVIEWREQUEST.fields_by_name['user_id'].message_type = _UUID
_REVIEWRESPONSE.fields_by_name['reviews'].message_type = _REVIEW
_SUBMITREVIEWREQUEST.fields_by_name['user_id'].message_type = _UUID
_UPDATESCOREREQUEST.fields_by_name['user_id'].message_type = _UUID
_USERTAGSREQUEST.fields_by_name['user_id'].message_type = _UUID
_USERTASKREQUEST.fields_by_name['user_id'].message_type = _UUID
_USERTASKREQUEST.fields_by_name['status'].enum_type = task__pb2._STATUS
_TASKRESULT.fields_by_name['tasks'].message_type = task__pb2._TASK
_USER.fields_by_name['id'].message_type = _UUID
_USER.fields_by_name['joined_tstamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_USER.fields_by_name['role'].enum_type = _ROLE
_USER.fields_by_name['reviews'].message_type = _REVIEW
_USER.fields_by_name['tasks'].message_type = task__pb2._TASK
_REVIEW.fields_by_name['id'].message_type = _UUID
_REVIEW.fields_by_name['created_tstamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name['DeleteUserRequest'] = _DELETEUSERREQUEST
DESCRIPTOR.message_types_by_name['NearbyRequest'] = _NEARBYREQUEST
DESCRIPTOR.message_types_by_name['NearbyResult'] = _NEARBYRESULT
DESCRIPTOR.message_types_by_name['ReviewRequest'] = _REVIEWREQUEST
DESCRIPTOR.message_types_by_name['ReviewResponse'] = _REVIEWRESPONSE
DESCRIPTOR.message_types_by_name['SubmitReviewRequest'] = _SUBMITREVIEWREQUEST
DESCRIPTOR.message_types_by_name['UpdateScoreRequest'] = _UPDATESCOREREQUEST
DESCRIPTOR.message_types_by_name['UserTagsRequest'] = _USERTAGSREQUEST
DESCRIPTOR.message_types_by_name['TagsResult'] = _TAGSRESULT
DESCRIPTOR.message_types_by_name['UserTaskRequest'] = _USERTASKREQUEST
DESCRIPTOR.message_types_by_name['TaskResult'] = _TASKRESULT
DESCRIPTOR.message_types_by_name['UUID'] = _UUID
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Review'] = _REVIEW
DESCRIPTOR.enum_types_by_name['Role'] = _ROLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

DeleteUserRequest = _reflection.GeneratedProtocolMessageType('DeleteUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.DeleteUserRequest)
  })
_sym_db.RegisterMessage(DeleteUserRequest)

NearbyRequest = _reflection.GeneratedProtocolMessageType('NearbyRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEARBYREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.NearbyRequest)
  })
_sym_db.RegisterMessage(NearbyRequest)

NearbyResult = _reflection.GeneratedProtocolMessageType('NearbyResult', (_message.Message,), {
  'DESCRIPTOR' : _NEARBYRESULT,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.NearbyResult)
  })
_sym_db.RegisterMessage(NearbyResult)

ReviewRequest = _reflection.GeneratedProtocolMessageType('ReviewRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.ReviewRequest)
  })
_sym_db.RegisterMessage(ReviewRequest)

ReviewResponse = _reflection.GeneratedProtocolMessageType('ReviewResponse', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWRESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.ReviewResponse)
  })
_sym_db.RegisterMessage(ReviewResponse)

SubmitReviewRequest = _reflection.GeneratedProtocolMessageType('SubmitReviewRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITREVIEWREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.SubmitReviewRequest)
  })
_sym_db.RegisterMessage(SubmitReviewRequest)

UpdateScoreRequest = _reflection.GeneratedProtocolMessageType('UpdateScoreRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESCOREREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.UpdateScoreRequest)
  })
_sym_db.RegisterMessage(UpdateScoreRequest)

UserTagsRequest = _reflection.GeneratedProtocolMessageType('UserTagsRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERTAGSREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.UserTagsRequest)
  })
_sym_db.RegisterMessage(UserTagsRequest)

TagsResult = _reflection.GeneratedProtocolMessageType('TagsResult', (_message.Message,), {
  'DESCRIPTOR' : _TAGSRESULT,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.TagsResult)
  })
_sym_db.RegisterMessage(TagsResult)

UserTaskRequest = _reflection.GeneratedProtocolMessageType('UserTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERTASKREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.UserTaskRequest)
  })
_sym_db.RegisterMessage(UserTaskRequest)

TaskResult = _reflection.GeneratedProtocolMessageType('TaskResult', (_message.Message,), {
  'DESCRIPTOR' : _TASKRESULT,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.TaskResult)
  })
_sym_db.RegisterMessage(TaskResult)

UUID = _reflection.GeneratedProtocolMessageType('UUID', (_message.Message,), {
  'DESCRIPTOR' : _UUID,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.UUID)
  })
_sym_db.RegisterMessage(UUID)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.User)
  })
_sym_db.RegisterMessage(User)

Review = _reflection.GeneratedProtocolMessageType('Review', (_message.Message,), {
  'DESCRIPTOR' : _REVIEW,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.v1.Review)
  })
_sym_db.RegisterMessage(Review)



_USERSERVICE = _descriptor.ServiceDescriptor(
  name='UserService',
  full_name='user.v1.UserService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1307,
  serialized_end=1800,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='user.v1.UserService.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEUSERREQUEST,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='user.v1.UserService.Delete',
    index=1,
    containing_service=None,
    input_type=_DELETEUSERREQUEST,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Nearby',
    full_name='user.v1.UserService.Nearby',
    index=2,
    containing_service=None,
    input_type=_NEARBYREQUEST,
    output_type=_NEARBYRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Reviews',
    full_name='user.v1.UserService.Reviews',
    index=3,
    containing_service=None,
    input_type=_REVIEWREQUEST,
    output_type=_REVIEWRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SubmitReview',
    full_name='user.v1.UserService.SubmitReview',
    index=4,
    containing_service=None,
    input_type=_SUBMITREVIEWREQUEST,
    output_type=_REVIEW,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateScore',
    full_name='user.v1.UserService.UpdateScore',
    index=5,
    containing_service=None,
    input_type=_UPDATESCOREREQUEST,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UserTags',
    full_name='user.v1.UserService.UserTags',
    index=6,
    containing_service=None,
    input_type=_USERTAGSREQUEST,
    output_type=_TAGSRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UserTasks',
    full_name='user.v1.UserService.UserTasks',
    index=7,
    containing_service=None,
    input_type=_USERTASKREQUEST,
    output_type=_TASKRESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERSERVICE)

DESCRIPTOR.services_by_name['UserService'] = _USERSERVICE

# @@protoc_insertion_point(module_scope)