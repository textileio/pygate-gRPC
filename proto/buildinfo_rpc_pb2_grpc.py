# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto.buildinfo_rpc_pb2 as buildinfo__rpc__pb2


class RPCServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BuildInfo = channel.unary_unary(
            "/buildinfo.rpc.RPCService/BuildInfo",
            request_serializer=buildinfo__rpc__pb2.BuildInfoRequest.SerializeToString,
            response_deserializer=buildinfo__rpc__pb2.BuildInfoResponse.FromString,
        )


class RPCServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BuildInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_RPCServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "BuildInfo": grpc.unary_unary_rpc_method_handler(
            servicer.BuildInfo,
            request_deserializer=buildinfo__rpc__pb2.BuildInfoRequest.FromString,
            response_serializer=buildinfo__rpc__pb2.BuildInfoResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "buildinfo.rpc.RPCService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class RPCService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BuildInfo(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/buildinfo.rpc.RPCService/BuildInfo",
            buildinfo__rpc__pb2.BuildInfoRequest.SerializeToString,
            buildinfo__rpc__pb2.BuildInfoResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
