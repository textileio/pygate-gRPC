# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto.ask_rpc_pb2 as ask__rpc__pb2


class RPCServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
            "/index.ask.rpc.RPCService/Get",
            request_serializer=ask__rpc__pb2.GetRequest.SerializeToString,
            response_deserializer=ask__rpc__pb2.GetResponse.FromString,
        )
        self.Query = channel.unary_unary(
            "/index.ask.rpc.RPCService/Query",
            request_serializer=ask__rpc__pb2.QueryRequest.SerializeToString,
            response_deserializer=ask__rpc__pb2.QueryResponse.FromString,
        )


class RPCServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_RPCServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Get": grpc.unary_unary_rpc_method_handler(
            servicer.Get,
            request_deserializer=ask__rpc__pb2.GetRequest.FromString,
            response_serializer=ask__rpc__pb2.GetResponse.SerializeToString,
        ),
        "Query": grpc.unary_unary_rpc_method_handler(
            servicer.Query,
            request_deserializer=ask__rpc__pb2.QueryRequest.FromString,
            response_serializer=ask__rpc__pb2.QueryResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "index.ask.rpc.RPCService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class RPCService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get(
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
            "/index.ask.rpc.RPCService/Get",
            ask__rpc__pb2.GetRequest.SerializeToString,
            ask__rpc__pb2.GetResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Query(
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
            "/index.ask.rpc.RPCService/Query",
            ask__rpc__pb2.QueryRequest.SerializeToString,
            ask__rpc__pb2.QueryResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
