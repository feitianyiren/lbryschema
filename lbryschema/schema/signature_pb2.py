# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: signature.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import certificate_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='signature.proto',
  package='',
  serialized_pb=_b('\n\x0fsignature.proto\x1a\x11\x63\x65rtificate.proto\"\xa7\x01\n\tSignature\x12#\n\x07version\x18\x01 \x02(\x0e\x32\x12.Signature.Version\x12\x1f\n\rsignatureType\x18\x02 \x02(\x0e\x32\x08.KeyType\x12\x11\n\tsignature\x18\x03 \x02(\x0c\x12\x15\n\rcertificateId\x18\x04 \x02(\x0c\"*\n\x07Version\x12\x13\n\x0fUNKNOWN_VERSION\x10\x00\x12\n\n\x06_0_0_1\x10\x01')
  ,
  dependencies=[certificate_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SIGNATURE_VERSION = _descriptor.EnumDescriptor(
  name='Version',
  full_name='Signature.Version',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_VERSION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='_0_0_1', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=164,
  serialized_end=206,
)
_sym_db.RegisterEnumDescriptor(_SIGNATURE_VERSION)


_SIGNATURE = _descriptor.Descriptor(
  name='Signature',
  full_name='Signature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='Signature.version', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signatureType', full_name='Signature.signatureType', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='Signature.signature', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='certificateId', full_name='Signature.certificateId', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SIGNATURE_VERSION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=206,
)

_SIGNATURE.fields_by_name['version'].enum_type = _SIGNATURE_VERSION
_SIGNATURE.fields_by_name['signatureType'].enum_type = certificate_pb2._KEYTYPE
_SIGNATURE_VERSION.containing_type = _SIGNATURE
DESCRIPTOR.message_types_by_name['Signature'] = _SIGNATURE

Signature = _reflection.GeneratedProtocolMessageType('Signature', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATURE,
  __module__ = 'signature_pb2'
  # @@protoc_insertion_point(class_scope:Signature)
  ))
_sym_db.RegisterMessage(Signature)


# @@protoc_insertion_point(module_scope)