# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/permission.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dictum_proto.proto import action_pb2 as proto_dot_action__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16proto/permission.proto\x1a\x12proto/action.proto\"s\n\nPermission\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x11\n\tentity_id\x18\x02 \x01(\x05\x12\x11\n\taction_id\x18\x03 \x01(\x05\x12\x15\n\rresource_name\x18\x04 \x01(\t\x12\x17\n\x06\x61\x63tion\x18\x05 \x01(\x0b\x32\x07.ActionB&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.permission_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _PERMISSION._serialized_start=46
  _PERMISSION._serialized_end=161
# @@protoc_insertion_point(module_scope)
