# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/logging_v2/proto/log_entry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import (
    monitored_resource_pb2 as google_dot_api_dot_monitored__resource__pb2,
)
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.logging.type import (
    http_request_pb2 as google_dot_logging_dot_type_dot_http__request__pb2,
)
from google.logging.type import (
    log_severity_pb2 as google_dot_logging_dot_type_dot_log__severity__pb2,
)
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/logging_v2/proto/log_entry.proto",
    package="google.logging.v2",
    syntax="proto3",
    serialized_options=b"\n\025com.google.logging.v2B\rLogEntryProtoP\001Z8google.golang.org/genproto/googleapis/logging/v2;logging\370\001\001\252\002\027Google.Cloud.Logging.V2\312\002\027Google\\Cloud\\Logging\\V2",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n-google/cloud/logging_v2/proto/log_entry.proto\x12\x11google.logging.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a#google/api/monitored_resource.proto\x1a\x19google/api/resource.proto\x1a&google/logging/type/http_request.proto\x1a&google/logging/type/log_severity.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x1cgoogle/api/annotations.proto"\xd2\x07\n\x08LogEntry\x12\x15\n\x08log_name\x18\x0c \x01(\tB\x03\xe0\x41\x02\x12\x34\n\x08resource\x18\x08 \x01(\x0b\x32\x1d.google.api.MonitoredResourceB\x03\xe0\x41\x02\x12-\n\rproto_payload\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12\x16\n\x0ctext_payload\x18\x03 \x01(\tH\x00\x12/\n\x0cjson_payload\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x12\x32\n\ttimestamp\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x01\x12:\n\x11receive_timestamp\x18\x18 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12\x37\n\x08severity\x18\n \x01(\x0e\x32 .google.logging.type.LogSeverityB\x03\xe0\x41\x01\x12\x16\n\tinsert_id\x18\x04 \x01(\tB\x03\xe0\x41\x01\x12;\n\x0chttp_request\x18\x07 \x01(\x0b\x32 .google.logging.type.HttpRequestB\x03\xe0\x41\x01\x12<\n\x06labels\x18\x0b \x03(\x0b\x32\'.google.logging.v2.LogEntry.LabelsEntryB\x03\xe0\x41\x01\x12<\n\toperation\x18\x0f \x01(\x0b\x32$.google.logging.v2.LogEntryOperationB\x03\xe0\x41\x01\x12\x12\n\x05trace\x18\x16 \x01(\tB\x03\xe0\x41\x01\x12\x14\n\x07span_id\x18\x1b \x01(\tB\x03\xe0\x41\x01\x12\x1a\n\rtrace_sampled\x18\x1e \x01(\x08\x42\x03\xe0\x41\x01\x12G\n\x0fsource_location\x18\x17 \x01(\x0b\x32).google.logging.v2.LogEntrySourceLocationB\x03\xe0\x41\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:\xbd\x01\xea\x41\xb9\x01\n\x1alogging.googleapis.com/Log\x12\x1dprojects/{project}/logs/{log}\x12\'organizations/{organization}/logs/{log}\x12\x1b\x66olders/{folder}/logs/{log}\x12,billingAccounts/{billing_account}/logs/{log}\x1a\x08log_nameB\t\n\x07payload"b\n\x11LogEntryOperation\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0\x41\x01\x12\x15\n\x08producer\x18\x02 \x01(\tB\x03\xe0\x41\x01\x12\x12\n\x05\x66irst\x18\x03 \x01(\x08\x42\x03\xe0\x41\x01\x12\x11\n\x04last\x18\x04 \x01(\x08\x42\x03\xe0\x41\x01"U\n\x16LogEntrySourceLocation\x12\x11\n\x04\x66ile\x18\x01 \x01(\tB\x03\xe0\x41\x01\x12\x11\n\x04line\x18\x02 \x01(\x03\x42\x03\xe0\x41\x01\x12\x15\n\x08\x66unction\x18\x03 \x01(\tB\x03\xe0\x41\x01\x42\x99\x01\n\x15\x63om.google.logging.v2B\rLogEntryProtoP\x01Z8google.golang.org/genproto/googleapis/logging/v2;logging\xf8\x01\x01\xaa\x02\x17Google.Cloud.Logging.V2\xca\x02\x17Google\\Cloud\\Logging\\V2b\x06proto3',
    dependencies=[
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_monitored__resource__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_logging_dot_type_dot_http__request__pb2.DESCRIPTOR,
        google_dot_logging_dot_type_dot_log__severity__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_any__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_rpc_dot_status__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_LOGENTRY_LABELSENTRY = _descriptor.Descriptor(
    name="LabelsEntry",
    full_name="google.logging.v2.LogEntry.LabelsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.logging.v2.LogEntry.LabelsEntry.key",
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
            name="value",
            full_name="google.logging.v2.LogEntry.LabelsEntry.value",
            index=1,
            number=2,
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
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1121,
    serialized_end=1166,
)

_LOGENTRY = _descriptor.Descriptor(
    name="LogEntry",
    full_name="google.logging.v2.LogEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="log_name",
            full_name="google.logging.v2.LogEntry.log_name",
            index=0,
            number=12,
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
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="resource",
            full_name="google.logging.v2.LogEntry.resource",
            index=1,
            number=8,
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
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="proto_payload",
            full_name="google.logging.v2.LogEntry.proto_payload",
            index=2,
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
        _descriptor.FieldDescriptor(
            name="text_payload",
            full_name="google.logging.v2.LogEntry.text_payload",
            index=3,
            number=3,
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
            name="json_payload",
            full_name="google.logging.v2.LogEntry.json_payload",
            index=4,
            number=6,
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
            name="timestamp",
            full_name="google.logging.v2.LogEntry.timestamp",
            index=5,
            number=9,
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
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="receive_timestamp",
            full_name="google.logging.v2.LogEntry.receive_timestamp",
            index=6,
            number=24,
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
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="severity",
            full_name="google.logging.v2.LogEntry.severity",
            index=7,
            number=10,
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
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="insert_id",
            full_name="google.logging.v2.LogEntry.insert_id",
            index=8,
            number=4,
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
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="http_request",
            full_name="google.logging.v2.LogEntry.http_request",
            index=9,
            number=7,
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
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="labels",
            full_name="google.logging.v2.LogEntry.labels",
            index=10,
            number=11,
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
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="operation",
            full_name="google.logging.v2.LogEntry.operation",
            index=11,
            number=15,
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
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="trace",
            full_name="google.logging.v2.LogEntry.trace",
            index=12,
            number=22,
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
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="span_id",
            full_name="google.logging.v2.LogEntry.span_id",
            index=13,
            number=27,
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
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="trace_sampled",
            full_name="google.logging.v2.LogEntry.trace_sampled",
            index=14,
            number=30,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="source_location",
            full_name="google.logging.v2.LogEntry.source_location",
            index=15,
            number=23,
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
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_LOGENTRY_LABELSENTRY],
    enum_types=[],
    serialized_options=b"\352A\271\001\n\032logging.googleapis.com/Log\022\035projects/{project}/logs/{log}\022'organizations/{organization}/logs/{log}\022\033folders/{folder}/logs/{log}\022,billingAccounts/{billing_account}/logs/{log}\032\010log_name",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="payload",
            full_name="google.logging.v2.LogEntry.payload",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        )
    ],
    serialized_start=391,
    serialized_end=1369,
)


_LOGENTRYOPERATION = _descriptor.Descriptor(
    name="LogEntryOperation",
    full_name="google.logging.v2.LogEntryOperation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="google.logging.v2.LogEntryOperation.id",
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
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="producer",
            full_name="google.logging.v2.LogEntryOperation.producer",
            index=1,
            number=2,
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
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="first",
            full_name="google.logging.v2.LogEntryOperation.first",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="last",
            full_name="google.logging.v2.LogEntryOperation.last",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
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
    serialized_start=1371,
    serialized_end=1469,
)


_LOGENTRYSOURCELOCATION = _descriptor.Descriptor(
    name="LogEntrySourceLocation",
    full_name="google.logging.v2.LogEntrySourceLocation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="file",
            full_name="google.logging.v2.LogEntrySourceLocation.file",
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
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="line",
            full_name="google.logging.v2.LogEntrySourceLocation.line",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="function",
            full_name="google.logging.v2.LogEntrySourceLocation.function",
            index=2,
            number=3,
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
            serialized_options=b"\340A\001",
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
    serialized_start=1471,
    serialized_end=1556,
)

_LOGENTRY_LABELSENTRY.containing_type = _LOGENTRY
_LOGENTRY.fields_by_name[
    "resource"
].message_type = google_dot_api_dot_monitored__resource__pb2._MONITOREDRESOURCE
_LOGENTRY.fields_by_name[
    "proto_payload"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_LOGENTRY.fields_by_name[
    "json_payload"
].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LOGENTRY.fields_by_name[
    "timestamp"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGENTRY.fields_by_name[
    "receive_timestamp"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGENTRY.fields_by_name[
    "severity"
].enum_type = google_dot_logging_dot_type_dot_log__severity__pb2._LOGSEVERITY
_LOGENTRY.fields_by_name[
    "http_request"
].message_type = google_dot_logging_dot_type_dot_http__request__pb2._HTTPREQUEST
_LOGENTRY.fields_by_name["labels"].message_type = _LOGENTRY_LABELSENTRY
_LOGENTRY.fields_by_name["operation"].message_type = _LOGENTRYOPERATION
_LOGENTRY.fields_by_name["source_location"].message_type = _LOGENTRYSOURCELOCATION
_LOGENTRY.oneofs_by_name["payload"].fields.append(
    _LOGENTRY.fields_by_name["proto_payload"]
)
_LOGENTRY.fields_by_name["proto_payload"].containing_oneof = _LOGENTRY.oneofs_by_name[
    "payload"
]
_LOGENTRY.oneofs_by_name["payload"].fields.append(
    _LOGENTRY.fields_by_name["text_payload"]
)
_LOGENTRY.fields_by_name["text_payload"].containing_oneof = _LOGENTRY.oneofs_by_name[
    "payload"
]
_LOGENTRY.oneofs_by_name["payload"].fields.append(
    _LOGENTRY.fields_by_name["json_payload"]
)
_LOGENTRY.fields_by_name["json_payload"].containing_oneof = _LOGENTRY.oneofs_by_name[
    "payload"
]
DESCRIPTOR.message_types_by_name["LogEntry"] = _LOGENTRY
DESCRIPTOR.message_types_by_name["LogEntryOperation"] = _LOGENTRYOPERATION
DESCRIPTOR.message_types_by_name["LogEntrySourceLocation"] = _LOGENTRYSOURCELOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogEntry = _reflection.GeneratedProtocolMessageType(
    "LogEntry",
    (_message.Message,),
    {
        "LabelsEntry": _reflection.GeneratedProtocolMessageType(
            "LabelsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _LOGENTRY_LABELSENTRY,
                "__module__": "google.cloud.logging_v2.proto.log_entry_pb2"
                # @@protoc_insertion_point(class_scope:google.logging.v2.LogEntry.LabelsEntry)
            },
        ),
        "DESCRIPTOR": _LOGENTRY,
        "__module__": "google.cloud.logging_v2.proto.log_entry_pb2",
        "__doc__": """An individual entry in a log.
  Attributes:
      log_name:
          Required. The resource name of the log to which this log entry
          belongs:  ::     "projects/[PROJECT_ID]/logs/[LOG_ID]"
          "organizations/[ORGANIZATION_ID]/logs/[LOG_ID]"
          "billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]"
          "folders/[FOLDER_ID]/logs/[LOG_ID]"  A project number may be
          used in place of PROJECT_ID. The project number is translated
          to its corresponding PROJECT_ID internally and the
          ``log_name`` field will contain PROJECT_ID in queries and
          exports.  ``[LOG_ID]`` must be URL-encoded within
          ``log_name``. Example: ``"organizations/1234567890/logs/cloudr
          esourcemanager.googleapis.com%2Factivity"``. ``[LOG_ID]`` must
          be less than 512 characters long and can only include the
          following characters: upper and lower case alphanumeric
          characters, forward-slash, underscore, hyphen, and period.
          For backward compatibility, if ``log_name`` begins with a
          forward-slash, such as ``/projects/...``, then the log entry
          is ingested as usual but the forward-slash is removed. Listing
          the log entry will not show the leading slash and filtering
          for a log name with a leading slash will never return any
          results.
      resource:
          Required. The monitored resource that produced this log entry.
          Example: a log entry that reports a database error would be
          associated with the monitored resource designating the
          particular database that reported the error.
      payload:
          The log entry payload, which can be one of multiple types.
      proto_payload:
          The log entry payload, represented as a protocol buffer. Some
          Google Cloud Platform services use this field for their log
          entry payloads.  The following protocol buffer types are
          supported; user-defined types are not supported:
          “type.googleapis.com/google.cloud.audit.AuditLog”
          “type.googleapis.com/google.appengine.logging.v1.RequestLog”
      text_payload:
          The log entry payload, represented as a Unicode string
          (UTF-8).
      json_payload:
          The log entry payload, represented as a structure that is
          expressed as a JSON object.
      timestamp:
          Optional. The time the event described by the log entry
          occurred. This time is used to compute the log entry’s age and
          to enforce the logs retention period. If this field is omitted
          in a new log entry, then Logging assigns it the current time.
          Timestamps have nanosecond accuracy, but trailing zeros in the
          fractional seconds might be omitted when the timestamp is
          displayed.  Incoming log entries should have timestamps that
          are no more than the `logs retention period
          <https://cloud.google.com/logging/quotas>`__ in the past, and
          no more than 24 hours in the future. Log entries outside those
          time boundaries will not be available when calling
          ``entries.list``, but those log entries can still be `exported
          with LogSinks
          <https://cloud.google.com/logging/docs/api/tasks/exporting-
          logs>`__.
      receive_timestamp:
          Output only. The time the log entry was received by Logging.
      severity:
          Optional. The severity of the log entry. The default value is
          ``LogSeverity.DEFAULT``.
      insert_id:
          Optional. A unique identifier for the log entry. If you
          provide a value, then Logging considers other log entries in
          the same project, with the same ``timestamp``, and with the
          same ``insert_id`` to be duplicates which are removed in a
          single query result. However, there are no guarantees of de-
          duplication in the export of logs.  If the ``insert_id`` is
          omitted when writing a log entry, the Logging API assigns its
          own unique identifier in this field.  In queries, the
          ``insert_id`` is also used to order log entries that have the
          same ``log_name`` and ``timestamp`` values.
      http_request:
          Optional. Information about the HTTP request associated with
          this log entry, if applicable.
      labels:
          Optional. A set of user-defined (key, value) data that
          provides additional information about the log entry.
      operation:
          Optional. Information about an operation associated with the
          log entry, if applicable.
      trace:
          Optional. Resource name of the trace associated with the log
          entry, if any. If it contains a relative resource name, the
          name is assumed to be relative to
          ``//tracing.googleapis.com``. Example: ``projects/my-
          projectid/traces/06796866738c859f2f19b7cfb3214824``
      span_id:
          Optional. The span ID within the trace associated with the log
          entry.  For Trace spans, this is the same format that the
          Trace API v2 uses: a 16-character hexadecimal encoding of an
          8-byte array, such as ``000000000000004a``.
      trace_sampled:
          Optional. The sampling decision of the trace associated with
          the log entry.  True means that the trace resource name in the
          ``trace`` field was sampled for storage in a trace backend.
          False means that the trace was not sampled for storage when
          this log entry was written, or the sampling decision was
          unknown at the time. A non-sampled ``trace`` value is still
          useful as a request correlation identifier. The default is
          False.
      source_location:
          Optional. Source code location information associated with the
          log entry, if any.
  """,
        # @@protoc_insertion_point(class_scope:google.logging.v2.LogEntry)
    },
)
_sym_db.RegisterMessage(LogEntry)
_sym_db.RegisterMessage(LogEntry.LabelsEntry)

LogEntryOperation = _reflection.GeneratedProtocolMessageType(
    "LogEntryOperation",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOGENTRYOPERATION,
        "__module__": "google.cloud.logging_v2.proto.log_entry_pb2",
        "__doc__": """Additional information about a potentially long-running operation with
  which a log entry is associated.
  Attributes:
      id:
          Optional. An arbitrary operation identifier. Log entries with
          the same identifier are assumed to be part of the same
          operation.
      producer:
          Optional. An arbitrary producer identifier. The combination of
          ``id`` and ``producer`` must be globally unique. Examples for
          ``producer``: ``"MyDivision.MyBigCompany.com"``,
          ``"github.com/MyProject/MyApplication"``.
      first:
          Optional. Set this to True if this is the first log entry in
          the operation.
      last:
          Optional. Set this to True if this is the last log entry in
          the operation.
  """,
        # @@protoc_insertion_point(class_scope:google.logging.v2.LogEntryOperation)
    },
)
_sym_db.RegisterMessage(LogEntryOperation)

LogEntrySourceLocation = _reflection.GeneratedProtocolMessageType(
    "LogEntrySourceLocation",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOGENTRYSOURCELOCATION,
        "__module__": "google.cloud.logging_v2.proto.log_entry_pb2",
        "__doc__": """Additional information about the source code location that produced
  the log entry.
  Attributes:
      file:
          Optional. Source file name. Depending on the runtime
          environment, this might be a simple name or a fully-qualified
          name.
      line:
          Optional. Line within the source file. 1-based; 0 indicates no
          line number available.
      function:
          Optional. Human-readable name of the function or method being
          invoked, with optional context such as the class or package
          name. This information may be used in contexts such as the
          logs viewer, where a file and line number are less meaningful.
          The format can vary by language. For example:
          ``qual.if.ied.Class.method`` (Java), ``dir/package.func``
          (Go), ``function`` (Python).
  """,
        # @@protoc_insertion_point(class_scope:google.logging.v2.LogEntrySourceLocation)
    },
)
_sym_db.RegisterMessage(LogEntrySourceLocation)


DESCRIPTOR._options = None
_LOGENTRY_LABELSENTRY._options = None
_LOGENTRY.fields_by_name["log_name"]._options = None
_LOGENTRY.fields_by_name["resource"]._options = None
_LOGENTRY.fields_by_name["timestamp"]._options = None
_LOGENTRY.fields_by_name["receive_timestamp"]._options = None
_LOGENTRY.fields_by_name["severity"]._options = None
_LOGENTRY.fields_by_name["insert_id"]._options = None
_LOGENTRY.fields_by_name["http_request"]._options = None
_LOGENTRY.fields_by_name["labels"]._options = None
_LOGENTRY.fields_by_name["operation"]._options = None
_LOGENTRY.fields_by_name["trace"]._options = None
_LOGENTRY.fields_by_name["span_id"]._options = None
_LOGENTRY.fields_by_name["trace_sampled"]._options = None
_LOGENTRY.fields_by_name["source_location"]._options = None
_LOGENTRY._options = None
_LOGENTRYOPERATION.fields_by_name["id"]._options = None
_LOGENTRYOPERATION.fields_by_name["producer"]._options = None
_LOGENTRYOPERATION.fields_by_name["first"]._options = None
_LOGENTRYOPERATION.fields_by_name["last"]._options = None
_LOGENTRYSOURCELOCATION.fields_by_name["file"]._options = None
_LOGENTRYSOURCELOCATION.fields_by_name["line"]._options = None
_LOGENTRYSOURCELOCATION.fields_by_name["function"]._options = None
# @@protoc_insertion_point(module_scope)
