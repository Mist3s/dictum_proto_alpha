# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/fin_event.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from dictum_proto.google.protobuf import descriptor as _descriptor
from dictum_proto.google.protobuf import descriptor_pool as _descriptor_pool
from dictum_proto.google.protobuf import symbol_database as _symbol_database
from dictum_proto.google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dictum_proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from dictum_proto.google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from dictum_proto.proto import accrual_pb2 as proto_dot_accrual__pb2
from dictum_proto.proto import accruals_aggregate_pb2 as proto_dot_accruals__aggregate__pb2
from dictum_proto.proto import action_pb2 as proto_dot_action__pb2
from dictum_proto.proto import allocation_pb2 as proto_dot_allocation__pb2
from dictum_proto.proto import article_pb2 as proto_dot_article__pb2
from dictum_proto.proto import comment_pb2 as proto_dot_comment__pb2
from dictum_proto.proto import event_aggregate_pb2 as proto_dot_event__aggregate__pb2
from dictum_proto.proto import permission_pb2 as proto_dot_permission__pb2
from dictum_proto.proto import position_pb2 as proto_dot_position__pb2
from dictum_proto.proto import product_pb2 as proto_dot_product__pb2
from dictum_proto.proto import requests_pb2 as proto_dot_requests__pb2
from dictum_proto.proto import signature_pb2 as proto_dot_signature__pb2
from dictum_proto.proto import transfer_pb2 as proto_dot_transfer__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15proto/fin_event.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x13proto/accrual.proto\x1a\x1eproto/accruals_aggregate.proto\x1a\x12proto/action.proto\x1a\x16proto/allocation.proto\x1a\x13proto/article.proto\x1a\x13proto/comment.proto\x1a\x1bproto/event_aggregate.proto\x1a\x16proto/permission.proto\x1a\x14proto/position.proto\x1a\x13proto/product.proto\x1a\x14proto/requests.proto\x1a\x15proto/signature.proto\x1a\x14proto/transfer.proto\"k\n\x17ListPermissionsResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12 \n\x0bpermissions\x18\x02 \x03(\x0b\x32\x0b.Permission\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\"h\n\x16ListSignaturesResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x1e\n\nsignatures\x18\x02 \x03(\x0b\x32\n.Signature\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\"b\n\x14ListCommentsResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x1a\n\x08\x63omments\x18\x02 \x03(\x0b\x32\x08.Comment\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\"F\n\x13ListActionsResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x18\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32\x07.Action\"%\n\x13ListArticlesRequest\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\"e\n\x15ListTransfersResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x1c\n\ttransfers\x18\x02 \x03(\x0b\x32\t.Transfer\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\"O\n\x1b\x42\x61tchInsertTransfersRequest\x12\x1c\n\ttransfers\x18\x01 \x03(\x0b\x32\t.Transfer\x12\x12\n\nservice_id\x18\x02 \x01(\x05\"b\n\x14ListAccrualsResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x1a\n\x08\x61\x63\x63ruals\x18\x02 \x03(\x0b\x32\x08.Accrual\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\"L\n\x1a\x42\x61tchInsertAccrualsRequest\x12\x1a\n\x08\x61\x63\x63ruals\x18\x01 \x03(\x0b\x32\x08.Accrual\x12\x12\n\nservice_id\x18\x02 \x01(\x05\"R\n\x1b\x42\x61tchInsertPositionsRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x1c\n\tpositions\x18\x02 \x03(\x0b\x32\t.Position\"0\n\x17\x41llocateTransferRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"b\n\x14ListProductsResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x1a\n\x08products\x18\x02 \x03(\x0b\x32\x08.Product\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\"e\n\x15ListPositionsResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x1c\n\tpositions\x18\x02 \x03(\x0b\x32\t.Position\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\"I\n\x14ListArticlesResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x1a\n\x08\x61rticles\x18\x02 \x03(\x0b\x32\x08.Article\"k\n\x17ListAllocationsResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12 \n\x0b\x61llocations\x18\x02 \x03(\x0b\x32\x0b.Allocation\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\"\x1c\n\x0c\x46ileResponse\x12\x0c\n\x04\x66ile\x18\x01 \x01(\x0c\x32\xf5\x1b\n\x08\x46inEvent\x12\x63\n\x0eListSignatures\x12\x0c.ListRequest\x1a\x17.ListSignaturesResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/v1/{parent=accruals/*}/signatures\x12]\n\x0cListComments\x12\x0c.ListRequest\x1a\x15.ListCommentsResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /v1/{parent=accruals/*}/comments\x12\x65\n\rCreateComment\x12\x08.Comment\x1a\x08.Comment\"@\x82\xd3\xe4\x93\x02:\"//v1/{comment.resource_name=accruals/*}/comments:\x07\x63omment\x12\\\n\rUpdateComment\x12\x08.Comment\x1a\x08.Comment\"7\x82\xd3\xe4\x93\x02\x31\x32&/v1/{comment.resource_name=comments/*}:\x07\x63omment\x12_\n\rDeleteComment\x12\x0e.DeleteRequest\x1a\x16.google.protobuf.Empty\"&\x82\xd3\xe4\x93\x02 *\x1e/v1/{resource_name=comments/*}\x12\x8d\x01\n\x10\x43reatePermission\x12\x0b.Permission\x1a\x0b.Permission\"_\x82\xd3\xe4\x93\x02Y\"K/v1/{permission.resource_name=entities/*/employees/*/actions/*}/permissions:\npermission\x12\x65\n\x0fListPermissions\x12\x0c.ListRequest\x1a\x18.ListPermissionsResponse\"*\x82\xd3\xe4\x93\x02$\x12\x0f/v1/permissionsZ\x11\x12\x0f/v1/permissions\x12x\n\x10\x44\x65letePermission\x12\x0e.DeleteRequest\x1a\x16.google.protobuf.Empty\"<\x82\xd3\xe4\x93\x02\x36*4/v1/{resource_name=entities/*/employees/*/actions/*}\x12_\n\x0bListActions\x12\x16.google.protobuf.Empty\x1a\x14.ListActionsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x0b/v1/actionsZ\r\x12\x0b/v1/actions\x12q\n\rListTransfers\x12\x0c.ListRequest\x1a\x16.ListTransfersResponse\":\x82\xd3\xe4\x93\x02\x34\x12\r/v1/transfersZ#\x12!/v1/{parent=accounts/*}/transfers\x12N\n\x0bGetTransfer\x12\x0b.GetRequest\x1a\t.Transfer\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{resource_name=transfers/*}\x12G\n\x0e\x43reateTransfer\x12\t.Transfer\x1a\t.Transfer\"\x1f\x82\xd3\xe4\x93\x02\x19\"\r/v1/transfers:\x08transfer\x12u\n\x10\x41llocateTransfer\x12\x18.AllocateTransferRequest\x1a\x0b.Allocation\":\x82\xd3\xe4\x93\x02\x34\"(/v1/{resource_name=transfers/*}/allocate:\x08transfer\x12z\n\x14\x42\x61tchInsertTransfers\x12\x1c.BatchInsertTransfersRequest\x1a\x16.google.protobuf.Empty\",\x82\xd3\xe4\x93\x02&\"\x13/v1/batch-transfers:\x0f\x62\x61tch_transfers\x12\x62\n\x0eUpdateTransfer\x12\t.Transfer\x1a\t.Transfer\":\x82\xd3\xe4\x93\x02\x34\x32(/v1/{transfer.resource_name=transfers/*}:\x08transfer\x12[\n\x12\x41ggregateTransfers\x12\x11.AggregateRequest\x1a\x0f.EventAggregate\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/transfers/-/aggregate\x12o\n\x0cListAccruals\x12\x0c.ListRequest\x1a\x15.ListAccrualsResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x0c/v1/accrualsZ$\x12\"/v1/{parent=operations/*}/accruals\x12K\n\nGetAccrual\x12\x0b.GetRequest\x1a\x08.Accrual\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{resource_name=accruals/*}\x12\x42\n\rCreateAccrual\x12\x08.Accrual\x1a\x08.Accrual\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x0c/v1/accruals:\x07\x61\x63\x63rual\x12\\\n\rUpdateAccrual\x12\x08.Accrual\x1a\x08.Accrual\"7\x82\xd3\xe4\x93\x02\x31\x32&/v1/{accrual.resource_name=accruals/*}:\x07\x61\x63\x63rual\x12\x8e\x01\n\x11\x41ggregateAccruals\x12\x11.AggregateRequest\x1a\x12.AccrualsAggregate\"R\x82\xd3\xe4\x93\x02L\x12\x18/v1/accruals/-/aggregateZ0\x12./v1/{parent=operations/*}/accruals/-/aggregate\x12u\n\x13\x42\x61tchInsertAccruals\x12\x1b.BatchInsertAccrualsRequest\x1a\x16.google.protobuf.Empty\")\x82\xd3\xe4\x93\x02#\"\x12/v1/batch-accruals:\rbatch_accrual\x12m\n\x12GenerateAccrualPDF\x12\x0b.GetRequest\x1a\r.FileResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/v1/{accrual.resource_name=accruals/*}/generate-pdf\x12m\n\x0cListProducts\x12\x0c.ListRequest\x1a\x15.ListProductsResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x0c/v1/productsZ\"\x12 /v1/{parent=entities/*}/products\x12o\n\rListPositions\x12\x0c.ListRequest\x1a\x16.ListPositionsResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\r/v1/positionsZ!\x12\x1f/v1/{parent=events/*}/positions\x12\x62\n\x0eUpdatePosition\x12\t.Position\x1a\t.Position\":\x82\xd3\xe4\x93\x02\x34\x32(/v1/{position.resource_name=positions/*}:\x08position\x12\xae\x01\n\x13\x42\x61tchInsertPostions\x12\x1c.BatchInsertPositionsRequest\x1a\x16.google.protobuf.Empty\"a\x82\xd3\xe4\x93\x02[\"\r/v1/positions:\x0f\x62\x61tch_positionsZ9\"&/v1/{resource_name=events/*}/positions:\x0f\x62\x61tch_positions\x12Q\n\x0cListArticles\x12\x14.ListArticlesRequest\x1a\x15.ListArticlesResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/articles\x12K\n\nGetArticle\x12\x0b.GetRequest\x1a\x08.Article\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{resource_name=articles/*}\x12\x42\n\rCreateArticle\x12\x08.Article\x1a\x08.Article\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x0c/v1/articles:\x07\x61rticle\x12\\\n\rUpdateArticle\x12\x08.Article\x1a\x08.Article\"7\x82\xd3\xe4\x93\x02\x31\x32&/v1/{article.resource_name=articles/*}:\x07\x61rticle\x12h\n\rDeleteArticle\x12\x0e.DeleteRequest\x1a\x16.google.protobuf.Empty\"/\x82\xd3\xe4\x93\x02)*\x1e/v1/{resource_name=articles/*}:\x07\x61rticle\x12\xa1\x01\n\x0fListAllocations\x12\x0c.ListRequest\x1a\x18.ListAllocationsResponse\"f\x82\xd3\xe4\x93\x02`\x12\x0f/v1/allocationsZ&\x12$/v1/{parent=transfers/*}/allocationsZ%\x12#/v1/{parent=accruals/*}/allocations\x12Q\n\x10\x43reateAllocation\x12\x0b.Allocation\x1a\x0b.Allocation\"#\x82\xd3\xe4\x93\x02\x1d\"\x0f/v1/allocations:\nallocationB&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.fin_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _globals['_FINEVENT'].methods_by_name['ListSignatures']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['ListSignatures']._serialized_options = b'\202\323\344\223\002$\022\"/v1/{parent=accruals/*}/signatures'
  _globals['_FINEVENT'].methods_by_name['ListComments']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['ListComments']._serialized_options = b'\202\323\344\223\002\"\022 /v1/{parent=accruals/*}/comments'
  _globals['_FINEVENT'].methods_by_name['CreateComment']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['CreateComment']._serialized_options = b'\202\323\344\223\002:\"//v1/{comment.resource_name=accruals/*}/comments:\007comment'
  _globals['_FINEVENT'].methods_by_name['UpdateComment']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['UpdateComment']._serialized_options = b'\202\323\344\223\00212&/v1/{comment.resource_name=comments/*}:\007comment'
  _globals['_FINEVENT'].methods_by_name['DeleteComment']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['DeleteComment']._serialized_options = b'\202\323\344\223\002 *\036/v1/{resource_name=comments/*}'
  _globals['_FINEVENT'].methods_by_name['CreatePermission']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['CreatePermission']._serialized_options = b'\202\323\344\223\002Y\"K/v1/{permission.resource_name=entities/*/employees/*/actions/*}/permissions:\npermission'
  _globals['_FINEVENT'].methods_by_name['ListPermissions']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['ListPermissions']._serialized_options = b'\202\323\344\223\002$\022\017/v1/permissionsZ\021\022\017/v1/permissions'
  _globals['_FINEVENT'].methods_by_name['DeletePermission']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['DeletePermission']._serialized_options = b'\202\323\344\223\0026*4/v1/{resource_name=entities/*/employees/*/actions/*}'
  _globals['_FINEVENT'].methods_by_name['ListActions']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['ListActions']._serialized_options = b'\202\323\344\223\002\034\022\013/v1/actionsZ\r\022\013/v1/actions'
  _globals['_FINEVENT'].methods_by_name['ListTransfers']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['ListTransfers']._serialized_options = b'\202\323\344\223\0024\022\r/v1/transfersZ#\022!/v1/{parent=accounts/*}/transfers'
  _globals['_FINEVENT'].methods_by_name['GetTransfer']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['GetTransfer']._serialized_options = b'\202\323\344\223\002!\022\037/v1/{resource_name=transfers/*}'
  _globals['_FINEVENT'].methods_by_name['CreateTransfer']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['CreateTransfer']._serialized_options = b'\202\323\344\223\002\031\"\r/v1/transfers:\010transfer'
  _globals['_FINEVENT'].methods_by_name['AllocateTransfer']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['AllocateTransfer']._serialized_options = b'\202\323\344\223\0024\"(/v1/{resource_name=transfers/*}/allocate:\010transfer'
  _globals['_FINEVENT'].methods_by_name['BatchInsertTransfers']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['BatchInsertTransfers']._serialized_options = b'\202\323\344\223\002&\"\023/v1/batch-transfers:\017batch_transfers'
  _globals['_FINEVENT'].methods_by_name['UpdateTransfer']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['UpdateTransfer']._serialized_options = b'\202\323\344\223\00242(/v1/{transfer.resource_name=transfers/*}:\010transfer'
  _globals['_FINEVENT'].methods_by_name['AggregateTransfers']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['AggregateTransfers']._serialized_options = b'\202\323\344\223\002\033\022\031/v1/transfers/-/aggregate'
  _globals['_FINEVENT'].methods_by_name['ListAccruals']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['ListAccruals']._serialized_options = b'\202\323\344\223\0024\022\014/v1/accrualsZ$\022\"/v1/{parent=operations/*}/accruals'
  _globals['_FINEVENT'].methods_by_name['GetAccrual']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['GetAccrual']._serialized_options = b'\202\323\344\223\002 \022\036/v1/{resource_name=accruals/*}'
  _globals['_FINEVENT'].methods_by_name['CreateAccrual']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['CreateAccrual']._serialized_options = b'\202\323\344\223\002\027\"\014/v1/accruals:\007accrual'
  _globals['_FINEVENT'].methods_by_name['UpdateAccrual']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['UpdateAccrual']._serialized_options = b'\202\323\344\223\00212&/v1/{accrual.resource_name=accruals/*}:\007accrual'
  _globals['_FINEVENT'].methods_by_name['AggregateAccruals']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['AggregateAccruals']._serialized_options = b'\202\323\344\223\002L\022\030/v1/accruals/-/aggregateZ0\022./v1/{parent=operations/*}/accruals/-/aggregate'
  _globals['_FINEVENT'].methods_by_name['BatchInsertAccruals']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['BatchInsertAccruals']._serialized_options = b'\202\323\344\223\002#\"\022/v1/batch-accruals:\rbatch_accrual'
  _globals['_FINEVENT'].methods_by_name['GenerateAccrualPDF']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['GenerateAccrualPDF']._serialized_options = b'\202\323\344\223\0025\0223/v1/{accrual.resource_name=accruals/*}/generate-pdf'
  _globals['_FINEVENT'].methods_by_name['ListProducts']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['ListProducts']._serialized_options = b'\202\323\344\223\0022\022\014/v1/productsZ\"\022 /v1/{parent=entities/*}/products'
  _globals['_FINEVENT'].methods_by_name['ListPositions']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['ListPositions']._serialized_options = b'\202\323\344\223\0022\022\r/v1/positionsZ!\022\037/v1/{parent=events/*}/positions'
  _globals['_FINEVENT'].methods_by_name['UpdatePosition']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['UpdatePosition']._serialized_options = b'\202\323\344\223\00242(/v1/{position.resource_name=positions/*}:\010position'
  _globals['_FINEVENT'].methods_by_name['BatchInsertPostions']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['BatchInsertPostions']._serialized_options = b'\202\323\344\223\002[\"\r/v1/positions:\017batch_positionsZ9\"&/v1/{resource_name=events/*}/positions:\017batch_positions'
  _globals['_FINEVENT'].methods_by_name['ListArticles']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['ListArticles']._serialized_options = b'\202\323\344\223\002\016\022\014/v1/articles'
  _globals['_FINEVENT'].methods_by_name['GetArticle']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['GetArticle']._serialized_options = b'\202\323\344\223\002 \022\036/v1/{resource_name=articles/*}'
  _globals['_FINEVENT'].methods_by_name['CreateArticle']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['CreateArticle']._serialized_options = b'\202\323\344\223\002\027\"\014/v1/articles:\007article'
  _globals['_FINEVENT'].methods_by_name['UpdateArticle']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['UpdateArticle']._serialized_options = b'\202\323\344\223\00212&/v1/{article.resource_name=articles/*}:\007article'
  _globals['_FINEVENT'].methods_by_name['DeleteArticle']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['DeleteArticle']._serialized_options = b'\202\323\344\223\002)*\036/v1/{resource_name=articles/*}:\007article'
  _globals['_FINEVENT'].methods_by_name['ListAllocations']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['ListAllocations']._serialized_options = b'\202\323\344\223\002`\022\017/v1/allocationsZ&\022$/v1/{parent=transfers/*}/allocationsZ%\022#/v1/{parent=accruals/*}/allocations'
  _globals['_FINEVENT'].methods_by_name['CreateAllocation']._loaded_options = None
  _globals['_FINEVENT'].methods_by_name['CreateAllocation']._serialized_options = b'\202\323\344\223\002\035\"\017/v1/allocations:\nallocation'
  _globals['_LISTPERMISSIONSRESPONSE']._serialized_start=386
  _globals['_LISTPERMISSIONSRESPONSE']._serialized_end=493
  _globals['_LISTSIGNATURESRESPONSE']._serialized_start=495
  _globals['_LISTSIGNATURESRESPONSE']._serialized_end=599
  _globals['_LISTCOMMENTSRESPONSE']._serialized_start=601
  _globals['_LISTCOMMENTSRESPONSE']._serialized_end=699
  _globals['_LISTACTIONSRESPONSE']._serialized_start=701
  _globals['_LISTACTIONSRESPONSE']._serialized_end=771
  _globals['_LISTARTICLESREQUEST']._serialized_start=773
  _globals['_LISTARTICLESREQUEST']._serialized_end=810
  _globals['_LISTTRANSFERSRESPONSE']._serialized_start=812
  _globals['_LISTTRANSFERSRESPONSE']._serialized_end=913
  _globals['_BATCHINSERTTRANSFERSREQUEST']._serialized_start=915
  _globals['_BATCHINSERTTRANSFERSREQUEST']._serialized_end=994
  _globals['_LISTACCRUALSRESPONSE']._serialized_start=996
  _globals['_LISTACCRUALSRESPONSE']._serialized_end=1094
  _globals['_BATCHINSERTACCRUALSREQUEST']._serialized_start=1096
  _globals['_BATCHINSERTACCRUALSREQUEST']._serialized_end=1172
  _globals['_BATCHINSERTPOSITIONSREQUEST']._serialized_start=1174
  _globals['_BATCHINSERTPOSITIONSREQUEST']._serialized_end=1256
  _globals['_ALLOCATETRANSFERREQUEST']._serialized_start=1258
  _globals['_ALLOCATETRANSFERREQUEST']._serialized_end=1306
  _globals['_LISTPRODUCTSRESPONSE']._serialized_start=1308
  _globals['_LISTPRODUCTSRESPONSE']._serialized_end=1406
  _globals['_LISTPOSITIONSRESPONSE']._serialized_start=1408
  _globals['_LISTPOSITIONSRESPONSE']._serialized_end=1509
  _globals['_LISTARTICLESRESPONSE']._serialized_start=1511
  _globals['_LISTARTICLESRESPONSE']._serialized_end=1584
  _globals['_LISTALLOCATIONSRESPONSE']._serialized_start=1586
  _globals['_LISTALLOCATIONSRESPONSE']._serialized_end=1693
  _globals['_FILERESPONSE']._serialized_start=1695
  _globals['_FILERESPONSE']._serialized_end=1723
  _globals['_FINEVENT']._serialized_start=1726
  _globals['_FINEVENT']._serialized_end=5299
# @@protoc_insertion_point(module_scope)
