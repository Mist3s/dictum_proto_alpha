# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dictum_proto.google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from dictum_proto.proto import attachment_pb2 as proto_dot_attachment__pb2
from dictum_proto.proto import requests_pb2 as proto_dot_requests__pb2
from dictum_proto.proto import storage_pb2 as proto_dot_storage__pb2


class StorageStub(object):
    """Репо - Attachment
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadAttachment = channel.unary_unary(
                '/Storage/UploadAttachment',
                request_serializer=proto_dot_requests__pb2.UploadAttachmentRequest.SerializeToString,
                response_deserializer=proto_dot_attachment__pb2.Attachment.FromString,
                )
        self.DeleteAttachment = channel.unary_unary(
                '/Storage/DeleteAttachment',
                request_serializer=proto_dot_requests__pb2.DeleteRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ListAttachments = channel.unary_unary(
                '/Storage/ListAttachments',
                request_serializer=proto_dot_requests__pb2.ListRequest.SerializeToString,
                response_deserializer=proto_dot_storage__pb2.ListAttachmentsResponse.FromString,
                )


class StorageServicer(object):
    """Репо - Attachment
    """

    def UploadAttachment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAttachment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAttachments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StorageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadAttachment': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadAttachment,
                    request_deserializer=proto_dot_requests__pb2.UploadAttachmentRequest.FromString,
                    response_serializer=proto_dot_attachment__pb2.Attachment.SerializeToString,
            ),
            'DeleteAttachment': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAttachment,
                    request_deserializer=proto_dot_requests__pb2.DeleteRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ListAttachments': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAttachments,
                    request_deserializer=proto_dot_requests__pb2.ListRequest.FromString,
                    response_serializer=proto_dot_storage__pb2.ListAttachmentsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Storage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Storage(object):
    """Репо - Attachment
    """

    @staticmethod
    def UploadAttachment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Storage/UploadAttachment',
            proto_dot_requests__pb2.UploadAttachmentRequest.SerializeToString,
            proto_dot_attachment__pb2.Attachment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAttachment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Storage/DeleteAttachment',
            proto_dot_requests__pb2.DeleteRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAttachments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Storage/ListAttachments',
            proto_dot_requests__pb2.ListRequest.SerializeToString,
            proto_dot_storage__pb2.ListAttachmentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
