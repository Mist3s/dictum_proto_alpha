# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from dictum_proto.proto import payment_pb2 as proto_dot_payment__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in proto/payment_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class PaymentServiceStub(object):
    """Dictum Payment Service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProcessPayment = channel.unary_unary(
                '/payment.PaymentService/ProcessPayment',
                request_serializer=proto_dot_payment__pb2.ProcessPaymentRequest.SerializeToString,
                response_deserializer=proto_dot_payment__pb2.ProcessPaymentResponse.FromString,
                _registered_method=True)
        self.BatchProcessPayment = channel.unary_stream(
                '/payment.PaymentService/BatchProcessPayment',
                request_serializer=proto_dot_payment__pb2.BatchProcessPaymentRequest.SerializeToString,
                response_deserializer=proto_dot_payment__pb2.ProcessPaymentResponse.FromString,
                _registered_method=True)
        self.CheckTransactionStatus = channel.unary_unary(
                '/payment.PaymentService/CheckTransactionStatus',
                request_serializer=proto_dot_payment__pb2.CheckTransactionStatusRequest.SerializeToString,
                response_deserializer=proto_dot_payment__pb2.CheckTransactionStatusResponse.FromString,
                _registered_method=True)
        self.EstimateEnergy = channel.unary_unary(
                '/payment.PaymentService/EstimateEnergy',
                request_serializer=proto_dot_payment__pb2.EstimateEnergyRequest.SerializeToString,
                response_deserializer=proto_dot_payment__pb2.EstimateEnergyResponse.FromString,
                _registered_method=True)
        self.WaitTransactionConfirmation = channel.unary_unary(
                '/payment.PaymentService/WaitTransactionConfirmation',
                request_serializer=proto_dot_payment__pb2.WaitTransactionConfirmationRequest.SerializeToString,
                response_deserializer=proto_dot_payment__pb2.WaitTransactionConfirmationResponse.FromString,
                _registered_method=True)


class PaymentServiceServicer(object):
    """Dictum Payment Service
    """

    def ProcessPayment(self, request, context):
        """Process a single payment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchProcessPayment(self, request, context):
        """Process a batch of payments
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckTransactionStatus(self, request, context):
        """Check the status of a transaction on the Tron network
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimateEnergy(self, request, context):
        """Check the estimated energy required for a transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WaitTransactionConfirmation(self, request, context):
        """Wait for transaction confirmation
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PaymentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProcessPayment': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessPayment,
                    request_deserializer=proto_dot_payment__pb2.ProcessPaymentRequest.FromString,
                    response_serializer=proto_dot_payment__pb2.ProcessPaymentResponse.SerializeToString,
            ),
            'BatchProcessPayment': grpc.unary_stream_rpc_method_handler(
                    servicer.BatchProcessPayment,
                    request_deserializer=proto_dot_payment__pb2.BatchProcessPaymentRequest.FromString,
                    response_serializer=proto_dot_payment__pb2.ProcessPaymentResponse.SerializeToString,
            ),
            'CheckTransactionStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckTransactionStatus,
                    request_deserializer=proto_dot_payment__pb2.CheckTransactionStatusRequest.FromString,
                    response_serializer=proto_dot_payment__pb2.CheckTransactionStatusResponse.SerializeToString,
            ),
            'EstimateEnergy': grpc.unary_unary_rpc_method_handler(
                    servicer.EstimateEnergy,
                    request_deserializer=proto_dot_payment__pb2.EstimateEnergyRequest.FromString,
                    response_serializer=proto_dot_payment__pb2.EstimateEnergyResponse.SerializeToString,
            ),
            'WaitTransactionConfirmation': grpc.unary_unary_rpc_method_handler(
                    servicer.WaitTransactionConfirmation,
                    request_deserializer=proto_dot_payment__pb2.WaitTransactionConfirmationRequest.FromString,
                    response_serializer=proto_dot_payment__pb2.WaitTransactionConfirmationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'payment.PaymentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('payment.PaymentService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PaymentService(object):
    """Dictum Payment Service
    """

    @staticmethod
    def ProcessPayment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/payment.PaymentService/ProcessPayment',
            proto_dot_payment__pb2.ProcessPaymentRequest.SerializeToString,
            proto_dot_payment__pb2.ProcessPaymentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BatchProcessPayment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/payment.PaymentService/BatchProcessPayment',
            proto_dot_payment__pb2.BatchProcessPaymentRequest.SerializeToString,
            proto_dot_payment__pb2.ProcessPaymentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CheckTransactionStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/payment.PaymentService/CheckTransactionStatus',
            proto_dot_payment__pb2.CheckTransactionStatusRequest.SerializeToString,
            proto_dot_payment__pb2.CheckTransactionStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EstimateEnergy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/payment.PaymentService/EstimateEnergy',
            proto_dot_payment__pb2.EstimateEnergyRequest.SerializeToString,
            proto_dot_payment__pb2.EstimateEnergyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def WaitTransactionConfirmation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/payment.PaymentService/WaitTransactionConfirmation',
            proto_dot_payment__pb2.WaitTransactionConfirmationRequest.SerializeToString,
            proto_dot_payment__pb2.WaitTransactionConfirmationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
