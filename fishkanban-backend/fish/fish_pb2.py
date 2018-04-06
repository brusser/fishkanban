# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fish.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fish.proto',
  package='fishmodel',
  syntax='proto3',
  serialized_pb=_b('\n\nfish.proto\x12\tfishmodel\"\x8c\x02\n\x04\x46ish\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12&\n\x04type\x18\x03 \x01(\x0e\x32\x18.fishmodel.Fish.FishType\x12(\n\x05state\x18\x04 \x01(\x0e\x32\x19.fishmodel.Fish.FishState\x12\x0c\n\x04tags\x18\x05 \x01(\t\x12\x0f\n\x07\x64\x65tails\x18\x06 \x01(\t\"/\n\x08\x46ishType\x12\r\n\tTYPE_NONE\x10\x00\x12\n\n\x06SALMON\x10\x01\x12\x08\n\x04TUNA\x10\x02\"C\n\tFishState\x12\x0e\n\nSTATE_NONE\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\x0e\n\nPROCESSING\x10\x02\x12\r\n\tCOMPLETED\x10\x03\x62\x06proto3')
)



_FISH_FISHTYPE = _descriptor.EnumDescriptor(
  name='FishType',
  full_name='fishmodel.Fish.FishType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SALMON', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TUNA', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=178,
  serialized_end=225,
)
_sym_db.RegisterEnumDescriptor(_FISH_FISHTYPE)

_FISH_FISHSTATE = _descriptor.EnumDescriptor(
  name='FishState',
  full_name='fishmodel.Fish.FishState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROCESSING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=227,
  serialized_end=294,
)
_sym_db.RegisterEnumDescriptor(_FISH_FISHSTATE)


_FISH = _descriptor.Descriptor(
  name='Fish',
  full_name='fishmodel.Fish',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='fishmodel.Fish.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_time', full_name='fishmodel.Fish.date_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='fishmodel.Fish.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='fishmodel.Fish.state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='fishmodel.Fish.tags', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='details', full_name='fishmodel.Fish.details', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FISH_FISHTYPE,
    _FISH_FISHSTATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=294,
)

_FISH.fields_by_name['type'].enum_type = _FISH_FISHTYPE
_FISH.fields_by_name['state'].enum_type = _FISH_FISHSTATE
_FISH_FISHTYPE.containing_type = _FISH
_FISH_FISHSTATE.containing_type = _FISH
DESCRIPTOR.message_types_by_name['Fish'] = _FISH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Fish = _reflection.GeneratedProtocolMessageType('Fish', (_message.Message,), dict(
  DESCRIPTOR = _FISH,
  __module__ = 'fish_pb2'
  # @@protoc_insertion_point(class_scope:fishmodel.Fish)
  ))
_sym_db.RegisterMessage(Fish)


# @@protoc_insertion_point(module_scope)
