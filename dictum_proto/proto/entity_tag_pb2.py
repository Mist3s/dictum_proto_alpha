# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/entity_tag.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dictum_proto.proto import entity_pb2 as proto_dot_entity__pb2
from dictum_proto.proto import tag_pb2 as proto_dot_tag__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16proto/entity_tag.proto\x1a\x12proto/entity.proto\x1a\x0fproto/tag.proto\"Z\n\tEntityTag\x12\x0e\n\x06tag_id\x18\x01 \x01(\x05\x12\x11\n\tentity_id\x18\x02 \x01(\x05\x12\x17\n\x06\x65ntity\x18\x03 \x01(\x0b\x32\x07.Entity\x12\x11\n\x03tag\x18\x05 \x01(\x0b\x32\x04.TagB&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.entity_tag_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _ENTITYTAG._serialized_start=63
  _ENTITYTAG._serialized_end=153
# @@protoc_insertion_point(module_scope)
