# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/account.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from dictum_proto.google.protobuf import descriptor as _descriptor
from dictum_proto.google.protobuf import descriptor_pool as _descriptor_pool
from dictum_proto.google.protobuf import symbol_database as _symbol_database
from dictum_proto.google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dictum_proto.google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from dictum_proto.proto import account_type_pb2 as proto_dot_account__type__pb2
from dictum_proto.proto import entity_pb2 as proto_dot_entity__pb2
from dictum_proto.proto import currency_pb2 as proto_dot_currency__pb2
from dictum_proto.proto import fi_pb2 as proto_dot_fi__pb2
from dictum_proto.proto import employee_pb2 as proto_dot_employee__pb2
from dictum_proto.proto import account_detail_pb2 as proto_dot_account__detail__pb2
from dictum_proto.proto import account_balance_pb2 as proto_dot_account__balance__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13proto/account.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18proto/account_type.proto\x1a\x12proto/entity.proto\x1a\x14proto/currency.proto\x1a\x0eproto/fi.proto\x1a\x14proto/employee.proto\x1a\x1aproto/account_detail.proto\x1a\x1bproto/account_balance.proto\"\xd1\x03\n\x07\x41\x63\x63ount\x12\x12\n\naccount_id\x18\x01 \x01(\x05\x12\x17\n\x0f\x63onglomerate_id\x18\x02 \x01(\x05\x12\x15\n\rcurrency_code\x18\x03 \x01(\t\x12\x11\n\tentity_id\x18\x04 \x01(\x05\x12\x0e\n\x06number\x18\x05 \x01(\t\x12\x1a\n\x04type\x18\x06 \x01(\x0e\x32\x0c.AccountType\x12\x12\n\nis_default\x18\x07 \x01(\x08\x12\x0f\n\x07\x66i_name\x18\x08 \x01(\t\x12\r\n\x05title\x18\t \x01(\t\x12\x12\n\ncashier_id\x18\x0b \x01(\x05\x12\x15\n\rresource_name\x18\r \x01(\t\x12\x17\n\x06\x65ntity\x18\x0f \x01(\x0b\x32\x07.Entity\x12\x1b\n\x08\x63urrency\x18\x11 \x01(\x0b\x32\t.Currency\x12\x0f\n\x02\x66i\x18\x13 \x01(\x0b\x32\x03.Fi\x12\x1a\n\x07\x63\x61shier\x18\x15 \x01(\x0b\x32\t.Employee\x12&\n\x0e\x61\x63\x63ount_detail\x18\x17 \x01(\x0b\x32\x0e.AccountDetail\x12/\n\x0b\x63reate_time\x18\x18 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x0f\x61\x63\x63ount_balance\x18\x19 \x01(\x0b\x32\x0f.AccountBalanceB&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.account_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _globals['_ACCOUNT']._serialized_start=220
  _globals['_ACCOUNT']._serialized_end=685
# @@protoc_insertion_point(module_scope)
