# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dictum_proto.google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from dictum_proto.proto import plugin_owner_type_pb2 as proto_dot_plugin__owner__type__pb2
from dictum_proto.proto import plugin_pb2 as proto_dot_plugin__pb2
from dictum_proto.proto import entity_pb2 as proto_dot_entity__pb2
from dictum_proto.proto import account_pb2 as proto_dot_account__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13proto/service.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dproto/plugin_owner_type.proto\x1a\x12proto/plugin.proto\x1a\x12proto/entity.proto\x1a\x13proto/account.proto\"\xbb\x02\n\x07Service\x12\x12\n\nservice_id\x18\x01 \x01(\x05\x12\x11\n\tplugin_id\x18\x02 \x01(\x05\x12\x11\n\tclient_id\x18\x03 \x01(\t\x12$\n\nowner_type\x18\x04 \x01(\x0e\x32\x10.PluginOwnerType\x12\x11\n\tentity_id\x18\x06 \x01(\x05\x12\x12\n\naccount_id\x18\x08 \x01(\x05\x12\x1f\n\x17\x63redentials_storage_key\x18\n \x01(\t\x12\x0c\n\x04\x63ron\x18\x0c \x01(\t\x12\x17\n\x06plugin\x18\x0e \x01(\x0b\x32\x07.Plugin\x12\x17\n\x06\x65ntity\x18\x10 \x01(\x0b\x32\x07.Entity\x12\x19\n\x07\x61\x63\x63ount\x18\x12 \x01(\x0b\x32\x08.Account\x12-\n\tsync_time\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.TimestampB&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _SERVICE._serialized_start=149
  _SERVICE._serialized_end=464
# @@protoc_insertion_point(module_scope)
