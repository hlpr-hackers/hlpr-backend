# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='task.proto',
  package='task.v1',
  syntax='proto3',
  serialized_options=None,

  serialized_pb=b'\n\ntask.proto\x12\x07task.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"9\n\rNearbyRequest\x12\x0b\n\x03lat\x18\x01 \x01(\x02\x12\x0b\n\x03lon\x18\x02 \x01(\x02\x12\x0e\n\x06radius\x18\x03 \x01(\x05\",\n\x0cNearbyResult\x12\x1c\n\x05tasks\x18\x01 \x03(\x0b\x32\r.task.v1.Task\"a\n\x11\x43reateTaskRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0b\n\x03tag\x18\x03 \x01(\t\x12\x0e\n\x06points\x18\x04 \x01(\x05\x12\x0c\n\x04UUID\x18\x05 \x01(\t\"3\n\x11\x44\x65leteTaskRequest\x12\x1e\n\x07task_id\x18\x01 \x01(\x0b\x32\r.task.v1.UUID\"S\n\x11\x41ssignTaskRequest\x12\x1e\n\x07user_id\x18\x01 \x01(\x0b\x32\r.task.v1.UUID\x12\x1e\n\x07task_id\x18\x02 \x01(\x0b\x32\r.task.v1.UUID\"S\n\x10SetStatusRequest\x12\x1e\n\x07task_id\x18\x01 \x01(\x0b\x32\r.task.v1.UUID\x12\x1f\n\x06status\x18\x02 \x01(\x0e\x32\x0f.task.v1.Status\"@\n\x0bTagsRequest\x12\x31\n\rcreated_since\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"(\n\nTagsResult\x12\x1a\n\x04tags\x18\x01 \x03(\x0b\x32\x0c.task.v1.Tag\"\"\n\x03Tag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\"\x15\n\x04UUID\x12\r\n\x05value\x18\x01 \x01(\t\"\xef\x01\n\x04Task\x12\x19\n\x02id\x18\x01 \x01(\x0b\x32\r.task.v1.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1f\n\x06status\x18\x03 \x01(\x0e\x32\x0f.task.v1.Status\x12\x35\n\x11submission_tstamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0b\n\x03tag\x18\x06 \x01(\t\x12\x0e\n\x06points\x18\x07 \x01(\x05\x12\x34\n\x10\x63ompleted_tstamp\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*5\n\x06Status\x12\x0e\n\nUNASSIGEND\x10\x00\x12\x0c\n\x08\x41SSIGNED\x10\x01\x12\r\n\tCOMPLETED\x10\x02\x32\xdf\x02\n\x0bTaskService\x12\x39\n\x06Nearby\x12\x16.task.v1.NearbyRequest\x1a\x15.task.v1.NearbyResult\"\x00\x12\x35\n\x06\x43reate\x12\x1a.task.v1.CreateTaskRequest\x1a\r.task.v1.Task\"\x00\x12\x35\n\x06\x44\x65lete\x12\x1a.task.v1.DeleteTaskRequest\x1a\r.task.v1.Task\"\x00\x12\x35\n\x06\x41ssign\x12\x1a.task.v1.AssignTaskRequest\x1a\r.task.v1.Task\"\x00\x12\x37\n\tSetStatus\x12\x19.task.v1.SetStatusRequest\x1a\r.task.v1.Task\"\x00\x12\x37\n\x08ListTags\x12\x14.task.v1.TagsRequest\x1a\x13.task.v1.TagsResult\"\x00\x62\x06proto3'

  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='task.v1.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNASSIGEND', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASSIGNED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=892,
  serialized_end=945,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
UNASSIGEND = 0
ASSIGNED = 1
COMPLETED = 2



_NEARBYREQUEST = _descriptor.Descriptor(
  name='NearbyRequest',
  full_name='task.v1.NearbyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='task.v1.NearbyRequest.lat', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='task.v1.NearbyRequest.lon', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius', full_name='task.v1.NearbyRequest.radius', index=2,
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
  serialized_start=56,
  serialized_end=113,
)


_NEARBYRESULT = _descriptor.Descriptor(
  name='NearbyResult',
  full_name='task.v1.NearbyResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='task.v1.NearbyResult.tasks', index=0,
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
  serialized_start=115,
  serialized_end=159,
)


_CREATETASKREQUEST = _descriptor.Descriptor(
  name='CreateTaskRequest',
  full_name='task.v1.CreateTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='task.v1.CreateTaskRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='task.v1.CreateTaskRequest.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='task.v1.CreateTaskRequest.tag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='points', full_name='task.v1.CreateTaskRequest.points', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='UUID', full_name='task.v1.CreateTaskRequest.UUID', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=161,
  serialized_end=258,
)


_DELETETASKREQUEST = _descriptor.Descriptor(
  name='DeleteTaskRequest',
  full_name='task.v1.DeleteTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='task.v1.DeleteTaskRequest.task_id', index=0,
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
  serialized_start=260,
  serialized_end=311,
)


_ASSIGNTASKREQUEST = _descriptor.Descriptor(
  name='AssignTaskRequest',
  full_name='task.v1.AssignTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='task.v1.AssignTaskRequest.user_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='task.v1.AssignTaskRequest.task_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=313,
  serialized_end=396,
)


_SETSTATUSREQUEST = _descriptor.Descriptor(
  name='SetStatusRequest',
  full_name='task.v1.SetStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='task.v1.SetStatusRequest.task_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='task.v1.SetStatusRequest.status', index=1,
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
  serialized_start=398,
  serialized_end=481,
)


_TAGSREQUEST = _descriptor.Descriptor(
  name='TagsRequest',
  full_name='task.v1.TagsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created_since', full_name='task.v1.TagsRequest.created_since', index=0,
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
  serialized_start=483,
  serialized_end=547,
)


_TAGSRESULT = _descriptor.Descriptor(
  name='TagsResult',
  full_name='task.v1.TagsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tags', full_name='task.v1.TagsResult.tags', index=0,
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
  serialized_start=549,
  serialized_end=589,
)


_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='task.v1.Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='task.v1.Tag.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='task.v1.Tag.count', index=1,
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
  serialized_start=591,
  serialized_end=625,
)


_UUID = _descriptor.Descriptor(
  name='UUID',
  full_name='task.v1.UUID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='task.v1.UUID.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=627,
  serialized_end=648,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='task.v1.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='task.v1.Task.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='task.v1.Task.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='task.v1.Task.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='submission_tstamp', full_name='task.v1.Task.submission_tstamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='task.v1.Task.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='task.v1.Task.tag', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='points', full_name='task.v1.Task.points', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='completed_tstamp', full_name='task.v1.Task.completed_tstamp', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=651,
  serialized_end=890,
)

_NEARBYRESULT.fields_by_name['tasks'].message_type = _TASK
_DELETETASKREQUEST.fields_by_name['task_id'].message_type = _UUID
_ASSIGNTASKREQUEST.fields_by_name['user_id'].message_type = _UUID
_ASSIGNTASKREQUEST.fields_by_name['task_id'].message_type = _UUID
_SETSTATUSREQUEST.fields_by_name['task_id'].message_type = _UUID
_SETSTATUSREQUEST.fields_by_name['status'].enum_type = _STATUS
_TAGSREQUEST.fields_by_name['created_since'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TAGSRESULT.fields_by_name['tags'].message_type = _TAG
_TASK.fields_by_name['id'].message_type = _UUID
_TASK.fields_by_name['status'].enum_type = _STATUS
_TASK.fields_by_name['submission_tstamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TASK.fields_by_name['completed_tstamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['NearbyRequest'] = _NEARBYREQUEST
DESCRIPTOR.message_types_by_name['NearbyResult'] = _NEARBYRESULT
DESCRIPTOR.message_types_by_name['CreateTaskRequest'] = _CREATETASKREQUEST
DESCRIPTOR.message_types_by_name['DeleteTaskRequest'] = _DELETETASKREQUEST
DESCRIPTOR.message_types_by_name['AssignTaskRequest'] = _ASSIGNTASKREQUEST
DESCRIPTOR.message_types_by_name['SetStatusRequest'] = _SETSTATUSREQUEST
DESCRIPTOR.message_types_by_name['TagsRequest'] = _TAGSREQUEST
DESCRIPTOR.message_types_by_name['TagsResult'] = _TAGSRESULT
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['UUID'] = _UUID
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NearbyRequest = _reflection.GeneratedProtocolMessageType('NearbyRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEARBYREQUEST,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.v1.NearbyRequest)
  })
_sym_db.RegisterMessage(NearbyRequest)

NearbyResult = _reflection.GeneratedProtocolMessageType('NearbyResult', (_message.Message,), {
  'DESCRIPTOR' : _NEARBYRESULT,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.v1.NearbyResult)
  })
_sym_db.RegisterMessage(NearbyResult)

CreateTaskRequest = _reflection.GeneratedProtocolMessageType('CreateTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETASKREQUEST,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.v1.CreateTaskRequest)
  })
_sym_db.RegisterMessage(CreateTaskRequest)

DeleteTaskRequest = _reflection.GeneratedProtocolMessageType('DeleteTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETASKREQUEST,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.v1.DeleteTaskRequest)
  })
_sym_db.RegisterMessage(DeleteTaskRequest)

AssignTaskRequest = _reflection.GeneratedProtocolMessageType('AssignTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _ASSIGNTASKREQUEST,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.v1.AssignTaskRequest)
  })
_sym_db.RegisterMessage(AssignTaskRequest)

SetStatusRequest = _reflection.GeneratedProtocolMessageType('SetStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETSTATUSREQUEST,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.v1.SetStatusRequest)
  })
_sym_db.RegisterMessage(SetStatusRequest)

TagsRequest = _reflection.GeneratedProtocolMessageType('TagsRequest', (_message.Message,), {
  'DESCRIPTOR' : _TAGSREQUEST,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.v1.TagsRequest)
  })
_sym_db.RegisterMessage(TagsRequest)

TagsResult = _reflection.GeneratedProtocolMessageType('TagsResult', (_message.Message,), {
  'DESCRIPTOR' : _TAGSRESULT,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.v1.TagsResult)
  })
_sym_db.RegisterMessage(TagsResult)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.v1.Tag)
  })
_sym_db.RegisterMessage(Tag)

UUID = _reflection.GeneratedProtocolMessageType('UUID', (_message.Message,), {
  'DESCRIPTOR' : _UUID,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.v1.UUID)
  })
_sym_db.RegisterMessage(UUID)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.v1.Task)
  })
_sym_db.RegisterMessage(Task)



_TASKSERVICE = _descriptor.ServiceDescriptor(
  name='TaskService',
  full_name='task.v1.TaskService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=948,
  serialized_end=1299,
  methods=[
  _descriptor.MethodDescriptor(
    name='Nearby',
    full_name='task.v1.TaskService.Nearby',
    index=0,
    containing_service=None,
    input_type=_NEARBYREQUEST,
    output_type=_NEARBYRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='task.v1.TaskService.Create',
    index=1,
    containing_service=None,
    input_type=_CREATETASKREQUEST,
    output_type=_TASK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='task.v1.TaskService.Delete',
    index=2,
    containing_service=None,
    input_type=_DELETETASKREQUEST,
    output_type=_TASK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Assign',
    full_name='task.v1.TaskService.Assign',
    index=3,
    containing_service=None,
    input_type=_ASSIGNTASKREQUEST,
    output_type=_TASK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetStatus',
    full_name='task.v1.TaskService.SetStatus',
    index=4,
    containing_service=None,
    input_type=_SETSTATUSREQUEST,
    output_type=_TASK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListTags',
    full_name='task.v1.TaskService.ListTags',
    index=5,
    containing_service=None,
    input_type=_TAGSREQUEST,
    output_type=_TAGSRESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TASKSERVICE)

DESCRIPTOR.services_by_name['TaskService'] = _TASKSERVICE

# @@protoc_insertion_point(module_scope)
