# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ProMC.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ProMC.proto',
  package='promc',
  serialized_pb='\n\x0bProMC.proto\x12\x05promc\"\xaa\x05\n\nProMCEvent\x12&\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x17.promc.ProMCEvent.Event\x12.\n\tparticles\x18\x02 \x01(\x0b\x32\x1b.promc.ProMCEvent.Particles\x1a\xea\x01\n\x05\x45vent\x12\x12\n\x06Number\x18\x01 \x03(\x05\x42\x02\x10\x01\x12\x16\n\nProcess_ID\x18\x02 \x03(\x05\x42\x02\x10\x01\x12\x0f\n\x03MPI\x18\x03 \x03(\x05\x42\x02\x10\x01\x12\x0f\n\x03ID1\x18\x04 \x03(\x05\x42\x02\x10\x01\x12\x0f\n\x03ID2\x18\x05 \x03(\x05\x42\x02\x10\x01\x12\x10\n\x04PDF1\x18\x06 \x03(\x02\x42\x02\x10\x01\x12\x10\n\x04PDF2\x18\x07 \x03(\x02\x42\x02\x10\x01\x12\n\n\x02X1\x18\x08 \x03(\x02\x12\n\n\x02X2\x18\t \x03(\x02\x12\x11\n\tScale_PDF\x18\n \x03(\x02\x12\x11\n\tAlpha_QED\x18\x0b \x03(\x02\x12\r\n\x05Scale\x18\x0c \x03(\x02\x12\x11\n\tAlpha_QCD\x18\r \x03(\x02\x1a\xd6\x02\n\tParticles\x12\x0e\n\x02id\x18\x01 \x03(\rB\x02\x10\x01\x12\x12\n\x06pdg_id\x18\x02 \x03(\x11\x42\x02\x10\x01\x12\x12\n\x06status\x18\x03 \x03(\rB\x02\x10\x01\x12\x10\n\x04mass\x18\x04 \x03(\x04\x42\x02\x10\x01\x12\x0e\n\x02Px\x18\x05 \x03(\x12\x42\x02\x10\x01\x12\x0e\n\x02Py\x18\x06 \x03(\x12\x42\x02\x10\x01\x12\x0e\n\x02Pz\x18\x07 \x03(\x12\x42\x02\x10\x01\x12\x13\n\x07mother1\x18\x08 \x03(\rB\x02\x10\x01\x12\x13\n\x07mother2\x18\t \x03(\rB\x02\x10\x01\x12\x15\n\tdaughter1\x18\n \x03(\rB\x02\x10\x01\x12\x15\n\tdaughter2\x18\x0b \x03(\rB\x02\x10\x01\x12\x13\n\x07\x62\x61rcode\x18\x0c \x03(\x11\x42\x02\x10\x01\x12\r\n\x01X\x18\r \x03(\x11\x42\x02\x10\x01\x12\r\n\x01Y\x18\x0e \x03(\x11\x42\x02\x10\x01\x12\r\n\x01Z\x18\x0f \x03(\x11\x42\x02\x10\x01\x12\r\n\x01T\x18\x10 \x03(\rB\x02\x10\x01\x12\x12\n\x06weight\x18\x11 \x03(\x04\x42\x02\x10\x01\x12\x12\n\x06\x63harge\x18\x12 \x03(\x11\x42\x02\x10\x01\x42\x11\n\x08promc.ioB\x05ProMC')




_PROMCEVENT_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='promc.ProMCEvent.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Number', full_name='promc.ProMCEvent.Event.Number', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='Process_ID', full_name='promc.ProMCEvent.Event.Process_ID', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='MPI', full_name='promc.ProMCEvent.Event.MPI', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='ID1', full_name='promc.ProMCEvent.Event.ID1', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='ID2', full_name='promc.ProMCEvent.Event.ID2', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='PDF1', full_name='promc.ProMCEvent.Event.PDF1', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='PDF2', full_name='promc.ProMCEvent.Event.PDF2', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='X1', full_name='promc.ProMCEvent.Event.X1', index=7,
      number=8, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='X2', full_name='promc.ProMCEvent.Event.X2', index=8,
      number=9, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Scale_PDF', full_name='promc.ProMCEvent.Event.Scale_PDF', index=9,
      number=10, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Alpha_QED', full_name='promc.ProMCEvent.Event.Alpha_QED', index=10,
      number=11, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Scale', full_name='promc.ProMCEvent.Event.Scale', index=11,
      number=12, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Alpha_QCD', full_name='promc.ProMCEvent.Event.Alpha_QCD', index=12,
      number=13, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=126,
  serialized_end=360,
)

_PROMCEVENT_PARTICLES = _descriptor.Descriptor(
  name='Particles',
  full_name='promc.ProMCEvent.Particles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='promc.ProMCEvent.Particles.id', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='pdg_id', full_name='promc.ProMCEvent.Particles.pdg_id', index=1,
      number=2, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='status', full_name='promc.ProMCEvent.Particles.status', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='mass', full_name='promc.ProMCEvent.Particles.mass', index=3,
      number=4, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='Px', full_name='promc.ProMCEvent.Particles.Px', index=4,
      number=5, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='Py', full_name='promc.ProMCEvent.Particles.Py', index=5,
      number=6, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='Pz', full_name='promc.ProMCEvent.Particles.Pz', index=6,
      number=7, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='mother1', full_name='promc.ProMCEvent.Particles.mother1', index=7,
      number=8, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='mother2', full_name='promc.ProMCEvent.Particles.mother2', index=8,
      number=9, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='daughter1', full_name='promc.ProMCEvent.Particles.daughter1', index=9,
      number=10, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='daughter2', full_name='promc.ProMCEvent.Particles.daughter2', index=10,
      number=11, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='barcode', full_name='promc.ProMCEvent.Particles.barcode', index=11,
      number=12, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='X', full_name='promc.ProMCEvent.Particles.X', index=12,
      number=13, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='Y', full_name='promc.ProMCEvent.Particles.Y', index=13,
      number=14, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='Z', full_name='promc.ProMCEvent.Particles.Z', index=14,
      number=15, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='T', full_name='promc.ProMCEvent.Particles.T', index=15,
      number=16, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='weight', full_name='promc.ProMCEvent.Particles.weight', index=16,
      number=17, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='charge', full_name='promc.ProMCEvent.Particles.charge', index=17,
      number=18, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=363,
  serialized_end=705,
)

_PROMCEVENT = _descriptor.Descriptor(
  name='ProMCEvent',
  full_name='promc.ProMCEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='promc.ProMCEvent.event', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='particles', full_name='promc.ProMCEvent.particles', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PROMCEVENT_EVENT, _PROMCEVENT_PARTICLES, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=23,
  serialized_end=705,
)

_PROMCEVENT_EVENT.containing_type = _PROMCEVENT;
_PROMCEVENT_PARTICLES.containing_type = _PROMCEVENT;
_PROMCEVENT.fields_by_name['event'].message_type = _PROMCEVENT_EVENT
_PROMCEVENT.fields_by_name['particles'].message_type = _PROMCEVENT_PARTICLES
DESCRIPTOR.message_types_by_name['ProMCEvent'] = _PROMCEVENT

class ProMCEvent(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Event(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _PROMCEVENT_EVENT

    # @@protoc_insertion_point(class_scope:promc.ProMCEvent.Event)

  class Particles(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _PROMCEVENT_PARTICLES

    # @@protoc_insertion_point(class_scope:promc.ProMCEvent.Particles)
  DESCRIPTOR = _PROMCEVENT

  # @@protoc_insertion_point(class_scope:promc.ProMCEvent)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\010promc.ioB\005ProMC')
_PROMCEVENT_EVENT.fields_by_name['Number'].has_options = True
_PROMCEVENT_EVENT.fields_by_name['Number']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_EVENT.fields_by_name['Process_ID'].has_options = True
_PROMCEVENT_EVENT.fields_by_name['Process_ID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_EVENT.fields_by_name['MPI'].has_options = True
_PROMCEVENT_EVENT.fields_by_name['MPI']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_EVENT.fields_by_name['ID1'].has_options = True
_PROMCEVENT_EVENT.fields_by_name['ID1']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_EVENT.fields_by_name['ID2'].has_options = True
_PROMCEVENT_EVENT.fields_by_name['ID2']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_EVENT.fields_by_name['PDF1'].has_options = True
_PROMCEVENT_EVENT.fields_by_name['PDF1']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_EVENT.fields_by_name['PDF2'].has_options = True
_PROMCEVENT_EVENT.fields_by_name['PDF2']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['id'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['pdg_id'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['pdg_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['status'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['status']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['mass'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['mass']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['Px'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['Px']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['Py'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['Py']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['Pz'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['Pz']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['mother1'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['mother1']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['mother2'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['mother2']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['daughter1'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['daughter1']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['daughter2'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['daughter2']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['barcode'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['barcode']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['X'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['X']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['Y'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['Y']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['Z'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['Z']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['T'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['T']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['weight'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['weight']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_PROMCEVENT_PARTICLES.fields_by_name['charge'].has_options = True
_PROMCEVENT_PARTICLES.fields_by_name['charge']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
# @@protoc_insertion_point(module_scope)
