# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/article_translation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dictum_proto.proto import article_pb2 as proto_dot_article__pb2
from dictum_proto.proto import language_pb2 as proto_dot_language__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fproto/article_translation.proto\x1a\x13proto/article.proto\x1a\x14proto/language.proto\"\x8c\x01\n\x12\x41rticleTranslation\x12\x12\n\narticle_id\x18\x01 \x01(\x05\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x13\n\x0btranslation\x18\x03 \x01(\t\x12\x19\n\x07\x61rticle\x18\x04 \x01(\x0b\x32\x08.Article\x12\x1b\n\x08language\x18\x06 \x01(\x0b\x32\t.LanguageB&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.article_translation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _ARTICLETRANSLATION._serialized_start=79
  _ARTICLETRANSLATION._serialized_end=219
# @@protoc_insertion_point(module_scope)
