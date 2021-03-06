# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: net_rpc.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="net_rpc.proto",
    package="net.rpc",
    syntax="proto3",
    serialized_options=b"Z&github.com/textileio/powergate/net/rpc",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\rnet_rpc.proto\x12\x07net.rpc")\n\x0cPeerAddrInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x61\x64\x64rs\x18\x02 \x03(\t"@\n\x08Location\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\t\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01"Y\n\x08PeerInfo\x12(\n\taddr_info\x18\x01 \x01(\x0b\x32\x15.net.rpc.PeerAddrInfo\x12#\n\x08location\x18\x02 \x01(\x0b\x32\x11.net.rpc.Location"\x13\n\x11ListenAddrRequest">\n\x12ListenAddrResponse\x12(\n\taddr_info\x18\x01 \x01(\x0b\x32\x15.net.rpc.PeerAddrInfo"\x0e\n\x0cPeersRequest"1\n\rPeersResponse\x12 \n\x05peers\x18\x01 \x03(\x0b\x32\x11.net.rpc.PeerInfo""\n\x0f\x46indPeerRequest\x12\x0f\n\x07peer_id\x18\x01 \x01(\t"8\n\x10\x46indPeerResponse\x12$\n\tpeer_info\x18\x01 \x01(\x0b\x32\x11.net.rpc.PeerInfo">\n\x12\x43onnectPeerRequest\x12(\n\tpeer_info\x18\x01 \x01(\x0b\x32\x15.net.rpc.PeerAddrInfo"\x15\n\x13\x43onnectPeerResponse"(\n\x15\x44isconnectPeerRequest\x12\x0f\n\x07peer_id\x18\x01 \x01(\t"\x18\n\x16\x44isconnectPeerResponse"\'\n\x14\x43onnectednessRequest\x12\x0f\n\x07peer_id\x18\x01 \x01(\t"F\n\x15\x43onnectednessResponse\x12-\n\rconnectedness\x18\x01 \x01(\x0e\x32\x16.net.rpc.Connectedness*\xc6\x01\n\rConnectedness\x12\x1d\n\x19\x43ONNECTEDNESS_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x43ONNECTEDNESS_NOT_CONNECTED\x10\x01\x12\x1b\n\x17\x43ONNECTEDNESS_CONNECTED\x10\x02\x12\x1d\n\x19\x43ONNECTEDNESS_CAN_CONNECT\x10\x03\x12 \n\x1c\x43ONNECTEDNESS_CANNOT_CONNECT\x10\x04\x12\x17\n\x13\x43ONNECTEDNESS_ERROR\x10\x05\x32\xc5\x03\n\nRPCService\x12G\n\nListenAddr\x12\x1a.net.rpc.ListenAddrRequest\x1a\x1b.net.rpc.ListenAddrResponse"\x00\x12\x38\n\x05Peers\x12\x15.net.rpc.PeersRequest\x1a\x16.net.rpc.PeersResponse"\x00\x12\x41\n\x08\x46indPeer\x12\x18.net.rpc.FindPeerRequest\x1a\x19.net.rpc.FindPeerResponse"\x00\x12J\n\x0b\x43onnectPeer\x12\x1b.net.rpc.ConnectPeerRequest\x1a\x1c.net.rpc.ConnectPeerResponse"\x00\x12S\n\x0e\x44isconnectPeer\x12\x1e.net.rpc.DisconnectPeerRequest\x1a\x1f.net.rpc.DisconnectPeerResponse"\x00\x12P\n\rConnectedness\x12\x1d.net.rpc.ConnectednessRequest\x1a\x1e.net.rpc.ConnectednessResponse"\x00\x42(Z&github.com/textileio/powergate/net/rpcb\x06proto3',
)

_CONNECTEDNESS = _descriptor.EnumDescriptor(
    name="Connectedness",
    full_name="net.rpc.Connectedness",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CONNECTEDNESS_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONNECTEDNESS_NOT_CONNECTED",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONNECTEDNESS_CONNECTED",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONNECTEDNESS_CAN_CONNECT",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONNECTEDNESS_CANNOT_CONNECT",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONNECTEDNESS_ERROR",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=741,
    serialized_end=939,
)
_sym_db.RegisterEnumDescriptor(_CONNECTEDNESS)

Connectedness = enum_type_wrapper.EnumTypeWrapper(_CONNECTEDNESS)
CONNECTEDNESS_UNSPECIFIED = 0
CONNECTEDNESS_NOT_CONNECTED = 1
CONNECTEDNESS_CONNECTED = 2
CONNECTEDNESS_CAN_CONNECT = 3
CONNECTEDNESS_CANNOT_CONNECT = 4
CONNECTEDNESS_ERROR = 5


_PEERADDRINFO = _descriptor.Descriptor(
    name="PeerAddrInfo",
    full_name="net.rpc.PeerAddrInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="net.rpc.PeerAddrInfo.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="addrs",
            full_name="net.rpc.PeerAddrInfo.addrs",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=26,
    serialized_end=67,
)


_LOCATION = _descriptor.Descriptor(
    name="Location",
    full_name="net.rpc.Location",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="country",
            full_name="net.rpc.Location.country",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="latitude",
            full_name="net.rpc.Location.latitude",
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="longitude",
            full_name="net.rpc.Location.longitude",
            index=2,
            number=3,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=69,
    serialized_end=133,
)


_PEERINFO = _descriptor.Descriptor(
    name="PeerInfo",
    full_name="net.rpc.PeerInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="addr_info",
            full_name="net.rpc.PeerInfo.addr_info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="location",
            full_name="net.rpc.PeerInfo.location",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=135,
    serialized_end=224,
)


_LISTENADDRREQUEST = _descriptor.Descriptor(
    name="ListenAddrRequest",
    full_name="net.rpc.ListenAddrRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=226,
    serialized_end=245,
)


_LISTENADDRRESPONSE = _descriptor.Descriptor(
    name="ListenAddrResponse",
    full_name="net.rpc.ListenAddrResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="addr_info",
            full_name="net.rpc.ListenAddrResponse.addr_info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=247,
    serialized_end=309,
)


_PEERSREQUEST = _descriptor.Descriptor(
    name="PeersRequest",
    full_name="net.rpc.PeersRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=311,
    serialized_end=325,
)


_PEERSRESPONSE = _descriptor.Descriptor(
    name="PeersResponse",
    full_name="net.rpc.PeersResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="peers",
            full_name="net.rpc.PeersResponse.peers",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=327,
    serialized_end=376,
)


_FINDPEERREQUEST = _descriptor.Descriptor(
    name="FindPeerRequest",
    full_name="net.rpc.FindPeerRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="peer_id",
            full_name="net.rpc.FindPeerRequest.peer_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=378,
    serialized_end=412,
)


_FINDPEERRESPONSE = _descriptor.Descriptor(
    name="FindPeerResponse",
    full_name="net.rpc.FindPeerResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="peer_info",
            full_name="net.rpc.FindPeerResponse.peer_info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=414,
    serialized_end=470,
)


_CONNECTPEERREQUEST = _descriptor.Descriptor(
    name="ConnectPeerRequest",
    full_name="net.rpc.ConnectPeerRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="peer_info",
            full_name="net.rpc.ConnectPeerRequest.peer_info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=472,
    serialized_end=534,
)


_CONNECTPEERRESPONSE = _descriptor.Descriptor(
    name="ConnectPeerResponse",
    full_name="net.rpc.ConnectPeerResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=536,
    serialized_end=557,
)


_DISCONNECTPEERREQUEST = _descriptor.Descriptor(
    name="DisconnectPeerRequest",
    full_name="net.rpc.DisconnectPeerRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="peer_id",
            full_name="net.rpc.DisconnectPeerRequest.peer_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=559,
    serialized_end=599,
)


_DISCONNECTPEERRESPONSE = _descriptor.Descriptor(
    name="DisconnectPeerResponse",
    full_name="net.rpc.DisconnectPeerResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=601,
    serialized_end=625,
)


_CONNECTEDNESSREQUEST = _descriptor.Descriptor(
    name="ConnectednessRequest",
    full_name="net.rpc.ConnectednessRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="peer_id",
            full_name="net.rpc.ConnectednessRequest.peer_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=627,
    serialized_end=666,
)


_CONNECTEDNESSRESPONSE = _descriptor.Descriptor(
    name="ConnectednessResponse",
    full_name="net.rpc.ConnectednessResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="connectedness",
            full_name="net.rpc.ConnectednessResponse.connectedness",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=668,
    serialized_end=738,
)

_PEERINFO.fields_by_name["addr_info"].message_type = _PEERADDRINFO
_PEERINFO.fields_by_name["location"].message_type = _LOCATION
_LISTENADDRRESPONSE.fields_by_name["addr_info"].message_type = _PEERADDRINFO
_PEERSRESPONSE.fields_by_name["peers"].message_type = _PEERINFO
_FINDPEERRESPONSE.fields_by_name["peer_info"].message_type = _PEERINFO
_CONNECTPEERREQUEST.fields_by_name["peer_info"].message_type = _PEERADDRINFO
_CONNECTEDNESSRESPONSE.fields_by_name["connectedness"].enum_type = _CONNECTEDNESS
DESCRIPTOR.message_types_by_name["PeerAddrInfo"] = _PEERADDRINFO
DESCRIPTOR.message_types_by_name["Location"] = _LOCATION
DESCRIPTOR.message_types_by_name["PeerInfo"] = _PEERINFO
DESCRIPTOR.message_types_by_name["ListenAddrRequest"] = _LISTENADDRREQUEST
DESCRIPTOR.message_types_by_name["ListenAddrResponse"] = _LISTENADDRRESPONSE
DESCRIPTOR.message_types_by_name["PeersRequest"] = _PEERSREQUEST
DESCRIPTOR.message_types_by_name["PeersResponse"] = _PEERSRESPONSE
DESCRIPTOR.message_types_by_name["FindPeerRequest"] = _FINDPEERREQUEST
DESCRIPTOR.message_types_by_name["FindPeerResponse"] = _FINDPEERRESPONSE
DESCRIPTOR.message_types_by_name["ConnectPeerRequest"] = _CONNECTPEERREQUEST
DESCRIPTOR.message_types_by_name["ConnectPeerResponse"] = _CONNECTPEERRESPONSE
DESCRIPTOR.message_types_by_name["DisconnectPeerRequest"] = _DISCONNECTPEERREQUEST
DESCRIPTOR.message_types_by_name["DisconnectPeerResponse"] = _DISCONNECTPEERRESPONSE
DESCRIPTOR.message_types_by_name["ConnectednessRequest"] = _CONNECTEDNESSREQUEST
DESCRIPTOR.message_types_by_name["ConnectednessResponse"] = _CONNECTEDNESSRESPONSE
DESCRIPTOR.enum_types_by_name["Connectedness"] = _CONNECTEDNESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PeerAddrInfo = _reflection.GeneratedProtocolMessageType(
    "PeerAddrInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _PEERADDRINFO,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.PeerAddrInfo)
    },
)
_sym_db.RegisterMessage(PeerAddrInfo)

Location = _reflection.GeneratedProtocolMessageType(
    "Location",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOCATION,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.Location)
    },
)
_sym_db.RegisterMessage(Location)

PeerInfo = _reflection.GeneratedProtocolMessageType(
    "PeerInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _PEERINFO,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.PeerInfo)
    },
)
_sym_db.RegisterMessage(PeerInfo)

ListenAddrRequest = _reflection.GeneratedProtocolMessageType(
    "ListenAddrRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTENADDRREQUEST,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.ListenAddrRequest)
    },
)
_sym_db.RegisterMessage(ListenAddrRequest)

ListenAddrResponse = _reflection.GeneratedProtocolMessageType(
    "ListenAddrResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTENADDRRESPONSE,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.ListenAddrResponse)
    },
)
_sym_db.RegisterMessage(ListenAddrResponse)

PeersRequest = _reflection.GeneratedProtocolMessageType(
    "PeersRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _PEERSREQUEST,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.PeersRequest)
    },
)
_sym_db.RegisterMessage(PeersRequest)

PeersResponse = _reflection.GeneratedProtocolMessageType(
    "PeersResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _PEERSRESPONSE,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.PeersResponse)
    },
)
_sym_db.RegisterMessage(PeersResponse)

FindPeerRequest = _reflection.GeneratedProtocolMessageType(
    "FindPeerRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _FINDPEERREQUEST,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.FindPeerRequest)
    },
)
_sym_db.RegisterMessage(FindPeerRequest)

FindPeerResponse = _reflection.GeneratedProtocolMessageType(
    "FindPeerResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _FINDPEERRESPONSE,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.FindPeerResponse)
    },
)
_sym_db.RegisterMessage(FindPeerResponse)

ConnectPeerRequest = _reflection.GeneratedProtocolMessageType(
    "ConnectPeerRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONNECTPEERREQUEST,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.ConnectPeerRequest)
    },
)
_sym_db.RegisterMessage(ConnectPeerRequest)

ConnectPeerResponse = _reflection.GeneratedProtocolMessageType(
    "ConnectPeerResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONNECTPEERRESPONSE,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.ConnectPeerResponse)
    },
)
_sym_db.RegisterMessage(ConnectPeerResponse)

DisconnectPeerRequest = _reflection.GeneratedProtocolMessageType(
    "DisconnectPeerRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISCONNECTPEERREQUEST,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.DisconnectPeerRequest)
    },
)
_sym_db.RegisterMessage(DisconnectPeerRequest)

DisconnectPeerResponse = _reflection.GeneratedProtocolMessageType(
    "DisconnectPeerResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISCONNECTPEERRESPONSE,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.DisconnectPeerResponse)
    },
)
_sym_db.RegisterMessage(DisconnectPeerResponse)

ConnectednessRequest = _reflection.GeneratedProtocolMessageType(
    "ConnectednessRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONNECTEDNESSREQUEST,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.ConnectednessRequest)
    },
)
_sym_db.RegisterMessage(ConnectednessRequest)

ConnectednessResponse = _reflection.GeneratedProtocolMessageType(
    "ConnectednessResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONNECTEDNESSRESPONSE,
        "__module__": "net_rpc_pb2"
        # @@protoc_insertion_point(class_scope:net.rpc.ConnectednessResponse)
    },
)
_sym_db.RegisterMessage(ConnectednessResponse)


DESCRIPTOR._options = None

_RPCSERVICE = _descriptor.ServiceDescriptor(
    name="RPCService",
    full_name="net.rpc.RPCService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=942,
    serialized_end=1395,
    methods=[
        _descriptor.MethodDescriptor(
            name="ListenAddr",
            full_name="net.rpc.RPCService.ListenAddr",
            index=0,
            containing_service=None,
            input_type=_LISTENADDRREQUEST,
            output_type=_LISTENADDRRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Peers",
            full_name="net.rpc.RPCService.Peers",
            index=1,
            containing_service=None,
            input_type=_PEERSREQUEST,
            output_type=_PEERSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="FindPeer",
            full_name="net.rpc.RPCService.FindPeer",
            index=2,
            containing_service=None,
            input_type=_FINDPEERREQUEST,
            output_type=_FINDPEERRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ConnectPeer",
            full_name="net.rpc.RPCService.ConnectPeer",
            index=3,
            containing_service=None,
            input_type=_CONNECTPEERREQUEST,
            output_type=_CONNECTPEERRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="DisconnectPeer",
            full_name="net.rpc.RPCService.DisconnectPeer",
            index=4,
            containing_service=None,
            input_type=_DISCONNECTPEERREQUEST,
            output_type=_DISCONNECTPEERRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Connectedness",
            full_name="net.rpc.RPCService.Connectedness",
            index=5,
            containing_service=None,
            input_type=_CONNECTEDNESSREQUEST,
            output_type=_CONNECTEDNESSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_RPCSERVICE)

DESCRIPTOR.services_by_name["RPCService"] = _RPCSERVICE

# @@protoc_insertion_point(module_scope)
