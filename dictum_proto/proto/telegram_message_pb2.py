# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/telegram_message.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from dictum_proto.google.protobuf import descriptor as _descriptor
from dictum_proto.google.protobuf import descriptor_pool as _descriptor_pool
from dictum_proto.google.protobuf import symbol_database as _symbol_database
from dictum_proto.google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dictum_proto.proto import accrual_pb2 as proto_dot_accrual__pb2
from dictum_proto.proto import transfer_pb2 as proto_dot_transfer__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cproto/telegram_message.proto\x1a\x13proto/accrual.proto\x1a\x14proto/transfer.proto\"\xa8\x01\n\x0fTelegramMessage\x12\x1b\n\x13telegram_message_id\x18\x01 \x01(\x05\x12\x17\n\x0f\x63hat_source_key\x18\x02 \x01(\x05\x12\x13\n\x0btransfer_id\x18\x05 \x01(\x05\x12\x12\n\naccrual_id\x18\x06 \x01(\x05\x12\x1b\n\x08transfer\x18\x07 \x01(\x0b\x32\t.Transfer\x12\x19\n\x07\x61\x63\x63rual\x18\x08 \x01(\x0b\x32\x08.AccrualB&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.telegram_message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _globals['_TELEGRAMMESSAGE']._serialized_start=76
  _globals['_TELEGRAMMESSAGE']._serialized_end=244
# @@protoc_insertion_point(module_scope)
