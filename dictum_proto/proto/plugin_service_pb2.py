# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/plugin_service.proto
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
from dictum_proto.proto import object_source_pb2 as proto_dot_object__source__pb2
from dictum_proto.proto import service_pb2 as proto_dot_service__pb2
from dictum_proto.proto import service_run_pb2 as proto_dot_service__run__pb2
from dictum_proto.proto import requests_pb2 as proto_dot_requests__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aproto/plugin_service.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x19proto/object_source.proto\x1a\x13proto/service.proto\x1a\x17proto/service_run.proto\x1a\x14proto/requests.proto\"?\n\x16GetLatestSourceRequest\x12\x12\n\nobjectType\x18\x01 \x01(\t\x12\x11\n\tserviceId\x18\x02 \x01(\x05\":\n\x18ListObjectSourcesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\"Q\n\x19ListObjectSourcesResponse\x12\x14\n\x0cresourceName\x18\x01 \x01(\t\x12\x1e\n\x07sources\x18\x02 \x03(\x0b\x32\r.ObjectSource\")\n\x11GetServiceRequest\x12\x14\n\x0cresourceName\x18\x01 \x01(\t\"%\n\x13ListServicesRequest\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\"H\n\x14ListServicesResponse\x12\x14\n\x0cresourceName\x18\x01 \x01(\t\x12\x1a\n\x08services\x18\x02 \x03(\x0b\x32\x08.Service\",\n\x14GetServiceRunRequest\x12\x14\n\x0cresourceName\x18\x01 \x01(\t\"l\n\x17ListServiceRunsResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12!\n\x0cservice_runs\x18\x02 \x03(\x0b\x32\x0b.ServiceRun\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\")\n\x11RunServiceRequest\x12\x14\n\x0cresourceName\x18\x01 \x01(\t2\x85\x0b\n\rPluginService\x12\xf5\x01\n\x11ListObjectSources\x12\x19.ListObjectSourcesRequest\x1a\x1a.ListObjectSourcesResponse\"\xa8\x01\x82\xd3\xe4\x93\x02\xa1\x01\x12(/v1/{parent=agents/*/accruals/*}/sourcesZ0\x12./v1/{parent=agents/*/counterparties/*}/sourcesZ-\x12+/v1/{parent=accounts/*/transfers/*}/sourcesZ\x14\x12\x12/v1/object-sources\x12\x39\n\x0fGetLatestSource\x12\x17.GetLatestSourceRequest\x1a\r.ObjectSource\x12\x87\x01\n\x12\x43reateObjectSource\x12\r.ObjectSource\x1a\r.ObjectSource\"S\x82\xd3\xe4\x93\x02M\"\x14/v1/accruals/sourcesZ\x1c\"\x1a/v1/counterparties/sourcesZ\x17\"\x15/v1/transfers/sources\x12y\n\x12\x44\x65leteObjectSource\x12\x0e.DeleteRequest\x1a\x16.google.protobuf.Empty\";\x82\xd3\xe4\x93\x02\x35*3/v1/{resource_name=services/*/accruals/*/sources/*}\x12P\n\rCreateService\x12\x08.Service\x1a\x08.Service\"+\x82\xd3\xe4\x93\x02%\x12#/v1/{resource_name=services/*}/runs\x12Q\n\x0cListServices\x12\x14.ListServicesRequest\x1a\x15.ListServicesResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/services\x12R\n\nGetService\x12\x12.GetServiceRequest\x1a\x08.Service\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{resource_name=services/*}\x12K\n\rUpdateService\x12\x08.Service\x1a\x08.Service\"&\x82\xd3\xe4\x93\x02 2\x1e/v1/{resource_name=services/*}\x12Y\n\x10\x43reateServiceRun\x12\x0b.ServiceRun\x1a\x0b.ServiceRun\"+\x82\xd3\xe4\x93\x02%\"#/v1/{resource_name=services/*}/runs\x12[\n\x10UpdateServiceRun\x12\x0b.ServiceRun\x1a\x0b.ServiceRun\"-\x82\xd3\xe4\x93\x02\'2%/v1/{resource_name=services/*/runs/*}\x12\x62\n\rGetServiceRun\x12\x15.GetServiceRunRequest\x1a\x0b.ServiceRun\"-\x82\xd3\xe4\x93\x02\'\x12%/v1/{resource_name=services/*/runs/*}\x12\x7f\n\x0fListServiceRuns\x12\x0c.ListRequest\x1a\x18.ListServiceRunsResponse\"D\x82\xd3\xe4\x93\x02>\x12\x1c/v1/{parent=services/*}/runsZ\x1e\x12\x1c/v1/{parent=services/-}/runs\x12Y\n\nRunService\x12\x12.RunServiceRequest\x1a\x0b.ServiceRun\"*\x82\xd3\xe4\x93\x02$\x12\"/v1/{resource_name=services/*}:runB&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.plugin_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _globals['_PLUGINSERVICE'].methods_by_name['ListObjectSources']._loaded_options = None
  _globals['_PLUGINSERVICE'].methods_by_name['ListObjectSources']._serialized_options = b'\202\323\344\223\002\241\001\022(/v1/{parent=agents/*/accruals/*}/sourcesZ0\022./v1/{parent=agents/*/counterparties/*}/sourcesZ-\022+/v1/{parent=accounts/*/transfers/*}/sourcesZ\024\022\022/v1/object-sources'
  _globals['_PLUGINSERVICE'].methods_by_name['CreateObjectSource']._loaded_options = None
  _globals['_PLUGINSERVICE'].methods_by_name['CreateObjectSource']._serialized_options = b'\202\323\344\223\002M\"\024/v1/accruals/sourcesZ\034\"\032/v1/counterparties/sourcesZ\027\"\025/v1/transfers/sources'
  _globals['_PLUGINSERVICE'].methods_by_name['DeleteObjectSource']._loaded_options = None
  _globals['_PLUGINSERVICE'].methods_by_name['DeleteObjectSource']._serialized_options = b'\202\323\344\223\0025*3/v1/{resource_name=services/*/accruals/*/sources/*}'
  _globals['_PLUGINSERVICE'].methods_by_name['CreateService']._loaded_options = None
  _globals['_PLUGINSERVICE'].methods_by_name['CreateService']._serialized_options = b'\202\323\344\223\002%\022#/v1/{resource_name=services/*}/runs'
  _globals['_PLUGINSERVICE'].methods_by_name['ListServices']._loaded_options = None
  _globals['_PLUGINSERVICE'].methods_by_name['ListServices']._serialized_options = b'\202\323\344\223\002\016\022\014/v1/services'
  _globals['_PLUGINSERVICE'].methods_by_name['GetService']._loaded_options = None
  _globals['_PLUGINSERVICE'].methods_by_name['GetService']._serialized_options = b'\202\323\344\223\002 \022\036/v1/{resource_name=services/*}'
  _globals['_PLUGINSERVICE'].methods_by_name['UpdateService']._loaded_options = None
  _globals['_PLUGINSERVICE'].methods_by_name['UpdateService']._serialized_options = b'\202\323\344\223\002 2\036/v1/{resource_name=services/*}'
  _globals['_PLUGINSERVICE'].methods_by_name['CreateServiceRun']._loaded_options = None
  _globals['_PLUGINSERVICE'].methods_by_name['CreateServiceRun']._serialized_options = b'\202\323\344\223\002%\"#/v1/{resource_name=services/*}/runs'
  _globals['_PLUGINSERVICE'].methods_by_name['UpdateServiceRun']._loaded_options = None
  _globals['_PLUGINSERVICE'].methods_by_name['UpdateServiceRun']._serialized_options = b'\202\323\344\223\002\'2%/v1/{resource_name=services/*/runs/*}'
  _globals['_PLUGINSERVICE'].methods_by_name['GetServiceRun']._loaded_options = None
  _globals['_PLUGINSERVICE'].methods_by_name['GetServiceRun']._serialized_options = b'\202\323\344\223\002\'\022%/v1/{resource_name=services/*/runs/*}'
  _globals['_PLUGINSERVICE'].methods_by_name['ListServiceRuns']._loaded_options = None
  _globals['_PLUGINSERVICE'].methods_by_name['ListServiceRuns']._serialized_options = b'\202\323\344\223\002>\022\034/v1/{parent=services/*}/runsZ\036\022\034/v1/{parent=services/-}/runs'
  _globals['_PLUGINSERVICE'].methods_by_name['RunService']._loaded_options = None
  _globals['_PLUGINSERVICE'].methods_by_name['RunService']._serialized_options = b'\202\323\344\223\002$\022\"/v1/{resource_name=services/*}:run'
  _globals['_GETLATESTSOURCEREQUEST']._serialized_start=184
  _globals['_GETLATESTSOURCEREQUEST']._serialized_end=247
  _globals['_LISTOBJECTSOURCESREQUEST']._serialized_start=249
  _globals['_LISTOBJECTSOURCESREQUEST']._serialized_end=307
  _globals['_LISTOBJECTSOURCESRESPONSE']._serialized_start=309
  _globals['_LISTOBJECTSOURCESRESPONSE']._serialized_end=390
  _globals['_GETSERVICEREQUEST']._serialized_start=392
  _globals['_GETSERVICEREQUEST']._serialized_end=433
  _globals['_LISTSERVICESREQUEST']._serialized_start=435
  _globals['_LISTSERVICESREQUEST']._serialized_end=472
  _globals['_LISTSERVICESRESPONSE']._serialized_start=474
  _globals['_LISTSERVICESRESPONSE']._serialized_end=546
  _globals['_GETSERVICERUNREQUEST']._serialized_start=548
  _globals['_GETSERVICERUNREQUEST']._serialized_end=592
  _globals['_LISTSERVICERUNSRESPONSE']._serialized_start=594
  _globals['_LISTSERVICERUNSRESPONSE']._serialized_end=702
  _globals['_RUNSERVICEREQUEST']._serialized_start=704
  _globals['_RUNSERVICEREQUEST']._serialized_end=745
  _globals['_PLUGINSERVICE']._serialized_start=748
  _globals['_PLUGINSERVICE']._serialized_end=2161
# @@protoc_insertion_point(module_scope)
