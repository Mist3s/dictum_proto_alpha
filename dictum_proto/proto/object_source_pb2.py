# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/object_source.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from dictum_proto.google.protobuf import descriptor as _descriptor
from dictum_proto.google.protobuf import descriptor_pool as _descriptor_pool
from dictum_proto.google.protobuf import symbol_database as _symbol_database
from dictum_proto.google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dictum_proto.google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from dictum_proto.proto import service_pb2 as proto_dot_service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19proto/object_source.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x13proto/service.proto\"\xaa\x01\n\x0cObjectSource\x12\x12\n\nservice_id\x18\x01 \x01(\x05\x12\x12\n\nsource_key\x18\x02 \x01(\t\x12\x13\n\x0bobject_type\x18\x03 \x01(\t\x12\x11\n\tobject_id\x18\x04 \x01(\t\x12\x19\n\x07service\x18\x06 \x01(\x0b\x32\x08.Service\x12/\n\x0b\x63reate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.object_source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _globals['_OBJECTSOURCE']._serialized_start=84
  _globals['_OBJECTSOURCE']._serialized_end=254
# @@protoc_insertion_point(module_scope)
