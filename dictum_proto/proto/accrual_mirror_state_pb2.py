# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/accrual_mirror_state.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from dictum_proto.google.protobuf import descriptor as _descriptor
from dictum_proto.google.protobuf import descriptor_pool as _descriptor_pool
from dictum_proto.google.protobuf import symbol_database as _symbol_database
from dictum_proto.google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dictum_proto.proto import payment_type_pb2 as proto_dot_payment__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n proto/accrual_mirror_state.proto\x1a\x18proto/payment_type.proto\"\xc4\x01\n\x12\x41\x63\x63rualMirrorState\x12\x1f\n\x17\x61\x63\x63rual_mirror_state_id\x18\x01 \x01(\x05\x12\"\n\x0cpayment_type\x18\x02 \x01(\x0e\x32\x0c.PaymentType\x12\x14\n\x0c\x62uyer_status\x18\x03 \x01(\t\x12\x15\n\rseller_status\x18\x04 \x01(\t\x12\x0f\n\x07is_sync\x18\x05 \x01(\x08\x12\x14\n\x0c\x62uyer_action\x18\x06 \x01(\t\x12\x15\n\rseller_action\x18\x08 \x01(\tB&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.accrual_mirror_state_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _globals['_ACCRUALMIRRORSTATE']._serialized_start=63
  _globals['_ACCRUALMIRRORSTATE']._serialized_end=259
# @@protoc_insertion_point(module_scope)
