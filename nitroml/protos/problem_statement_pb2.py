# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_metadata/proto/v0/problem_statement.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from nitroml.protos import metric_pb2 as tensorflow__metadata_dot_proto_dot_v0_dot_metric__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_metadata/proto/v0/problem_statement.proto',
  package='tensorflow.metadata.v0',
  syntax='proto3',
  serialized_options=_b('\n\032org.tensorflow.metadata.v0P\001\370\001\001'),
  serialized_pb=_b('\n4tensorflow_metadata/proto/v0/problem_statement.proto\x12\x16tensorflow.metadata.v0\x1a google/protobuf/descriptor.proto\x1a)tensorflow_metadata/proto/v0/metric.proto\"E\n\x14\x42inaryClassification\x12\r\n\x05label\x18\x01 \x01(\t\x12\x16\n\x0e\x65xample_weight\x18\x02 \x01(\t:\x06\x98\xb6\xf8\x9a\x07\x01\"\x9d\x01\n\x10\x44ynamicClassSpec\x12M\n\x0eoov_class_spec\x18\x01 \x01(\x0b\x32\x35.tensorflow.metadata.v0.DynamicClassSpec.OovClassSpec\x1a:\n\x0cOovClassSpec\x12\x1b\n\x13\x66requency_threshold\x18\x01 \x01(\x03\x12\r\n\x05top_k\x18\x02 \x01(\x03\"\xb4\x01\n\x18MultiClassClassification\x12\r\n\x05label\x18\x01 \x01(\t\x12\x16\n\x0e\x65xample_weight\x18\x02 \x01(\t\x12\x13\n\tn_classes\x18\x03 \x01(\x04H\x00\x12\x46\n\x12\x64ynamic_class_spec\x18\x04 \x01(\x0b\x32(.tensorflow.metadata.v0.DynamicClassSpecH\x00:\x06\x98\xb6\xf8\x9a\x07\x02\x42\x0c\n\nclass_spec\"\xb4\x01\n\x18MultiLabelClassification\x12\r\n\x05label\x18\x01 \x01(\t\x12\x16\n\x0e\x65xample_weight\x18\x02 \x01(\t\x12\x13\n\tn_classes\x18\x03 \x01(\x04H\x00\x12\x46\n\x12\x64ynamic_class_spec\x18\x04 \x01(\x0b\x32(.tensorflow.metadata.v0.DynamicClassSpecH\x00:\x06\x98\xb6\xf8\x9a\x07\x05\x42\x0c\n\nclass_spec\"\xf8\x01\n\x12TopKClassification\x12\r\n\x05label\x18\x01 \x01(\t\x12\x16\n\x0e\x65xample_weight\x18\x02 \x01(\t\x12\x11\n\tn_classes\x18\x03 \x01(\x04\x12\x1a\n\x12n_predicted_labels\x18\x04 \x01(\x04\x12K\n\x11predictions_order\x18\x05 \x01(\x0e\x32\x30.tensorflow.metadata.v0.TopKClassification.Order\"7\n\x05Order\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0e\n\nSCORE_DESC\x10\x01\x12\r\n\tSCORE_ASC\x10\x02:\x06\x98\xb6\xf8\x9a\x07\x03\"A\n\x18OneDimensionalRegression\x12\r\n\x05label\x18\x01 \x01(\t\x12\x0e\n\x06weight\x18\x02 \x01(\t:\x06\x98\xb6\xf8\x9a\x07\x04\"\xb6\x03\n\x04Type\x12M\n\x15\x62inary_classification\x18\x01 \x01(\x0b\x32,.tensorflow.metadata.v0.BinaryClassificationH\x00\x12V\n\x1aone_dimensional_regression\x18\x02 \x01(\x0b\x32\x30.tensorflow.metadata.v0.OneDimensionalRegressionH\x00\x12V\n\x1amulti_class_classification\x18\x03 \x01(\x0b\x32\x30.tensorflow.metadata.v0.MultiClassClassificationH\x00\x12J\n\x14top_k_classification\x18\x04 \x01(\x0b\x32*.tensorflow.metadata.v0.TopKClassificationH\x00\x12V\n\x1amulti_label_classification\x18\x05 \x01(\x0b\x32\x30.tensorflow.metadata.v0.MultiLabelClassificationH\x00\x42\x0b\n\ttask_type\"\xe7\x01\n\x04Task\x12*\n\x04type\x18\x01 \x01(\x0b\x32\x1c.tensorflow.metadata.v0.Type\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x13\n\x0btask_weight\x18\x02 \x01(\x01\x12I\n\x12objective_function\x18\x03 \x01(\x0b\x32).tensorflow.metadata.v0.ObjectiveFunctionB\x02\x18\x01\x12\x45\n\x12performance_metric\x18\x04 \x03(\x0b\x32).tensorflow.metadata.v0.PerformanceMetric\"\xae\x01\n\x16MetaOptimizationTarget\x12\x11\n\ttask_name\x18\x01 \x01(\t\x12*\n\x04type\x18\x02 \x01(\x0b\x32\x1c.tensorflow.metadata.v0.Type\x12\x45\n\x12performance_metric\x18\x03 \x01(\x0b\x32).tensorflow.metadata.v0.PerformanceMetric\x12\x0e\n\x06weight\x18\x04 \x01(\x01\"\xe9\x01\n\x10ProblemStatement\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x03(\t\x12\x13\n\x0b\x65nvironment\x18\x04 \x01(\t\x12P\n\x18meta_optimization_target\x18\x07 \x03(\x0b\x32..tensorflow.metadata.v0.MetaOptimizationTarget\x12\x17\n\x0fmulti_objective\x18\x08 \x01(\x08\x12+\n\x05tasks\x18\t \x03(\x0b\x32\x1c.tensorflow.metadata.v0.TaskJ\x04\x08\x05\x10\x06*\xb1\x01\n\x08TaskType\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x19\n\x15\x42INARY_CLASSIFICATION\x10\x01\x12\x1e\n\x1aMULTI_CLASS_CLASSIFICATION\x10\x02\x12\x18\n\x14TOP_K_CLASSIFICATION\x10\x03\x12\x1e\n\x1aONE_DIMENSIONAL_REGRESSION\x10\x04\x12\x1e\n\x1aMULTI_LABEL_CLASSIFICATION\x10\x05:W\n\ttask_type\x12\x1f.google.protobuf.MessageOptions\x18\xe3\x86\xafs \x01(\x0e\x32 .tensorflow.metadata.v0.TaskTypeB!\n\x1aorg.tensorflow.metadata.v0P\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,tensorflow__metadata_dot_proto_dot_v0_dot_metric__pb2.DESCRIPTOR,])

_TASKTYPE = _descriptor.EnumDescriptor(
  name='TaskType',
  full_name='tensorflow.metadata.v0.TaskType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINARY_CLASSIFICATION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTI_CLASS_CLASSIFICATION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOP_K_CLASSIFICATION', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONE_DIMENSIONAL_REGRESSION', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTI_LABEL_CLASSIFICATION', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2161,
  serialized_end=2338,
)
_sym_db.RegisterEnumDescriptor(_TASKTYPE)

TaskType = enum_type_wrapper.EnumTypeWrapper(_TASKTYPE)
UNKNOWN_TYPE = 0
BINARY_CLASSIFICATION = 1
MULTI_CLASS_CLASSIFICATION = 2
TOP_K_CLASSIFICATION = 3
ONE_DIMENSIONAL_REGRESSION = 4
MULTI_LABEL_CLASSIFICATION = 5

TASK_TYPE_FIELD_NUMBER = 241943395
task_type = _descriptor.FieldDescriptor(
  name='task_type', full_name='tensorflow.metadata.v0.task_type', index=0,
  number=241943395, type=14, cpp_type=8, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)

_TOPKCLASSIFICATION_ORDER = _descriptor.EnumDescriptor(
  name='Order',
  full_name='tensorflow.metadata.v0.TopKClassification.Order',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCORE_DESC', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCORE_ASC', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=940,
  serialized_end=995,
)
_sym_db.RegisterEnumDescriptor(_TOPKCLASSIFICATION_ORDER)


_BINARYCLASSIFICATION = _descriptor.Descriptor(
  name='BinaryClassification',
  full_name='tensorflow.metadata.v0.BinaryClassification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='tensorflow.metadata.v0.BinaryClassification.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='example_weight', full_name='tensorflow.metadata.v0.BinaryClassification.example_weight', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\230\266\370\232\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=226,
)


_DYNAMICCLASSSPEC_OOVCLASSSPEC = _descriptor.Descriptor(
  name='OovClassSpec',
  full_name='tensorflow.metadata.v0.DynamicClassSpec.OovClassSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frequency_threshold', full_name='tensorflow.metadata.v0.DynamicClassSpec.OovClassSpec.frequency_threshold', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top_k', full_name='tensorflow.metadata.v0.DynamicClassSpec.OovClassSpec.top_k', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=386,
)

_DYNAMICCLASSSPEC = _descriptor.Descriptor(
  name='DynamicClassSpec',
  full_name='tensorflow.metadata.v0.DynamicClassSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='oov_class_spec', full_name='tensorflow.metadata.v0.DynamicClassSpec.oov_class_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DYNAMICCLASSSPEC_OOVCLASSSPEC, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=386,
)


_MULTICLASSCLASSIFICATION = _descriptor.Descriptor(
  name='MultiClassClassification',
  full_name='tensorflow.metadata.v0.MultiClassClassification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='tensorflow.metadata.v0.MultiClassClassification.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='example_weight', full_name='tensorflow.metadata.v0.MultiClassClassification.example_weight', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_classes', full_name='tensorflow.metadata.v0.MultiClassClassification.n_classes', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dynamic_class_spec', full_name='tensorflow.metadata.v0.MultiClassClassification.dynamic_class_spec', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\230\266\370\232\007\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='class_spec', full_name='tensorflow.metadata.v0.MultiClassClassification.class_spec',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=389,
  serialized_end=569,
)


_MULTILABELCLASSIFICATION = _descriptor.Descriptor(
  name='MultiLabelClassification',
  full_name='tensorflow.metadata.v0.MultiLabelClassification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='tensorflow.metadata.v0.MultiLabelClassification.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='example_weight', full_name='tensorflow.metadata.v0.MultiLabelClassification.example_weight', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_classes', full_name='tensorflow.metadata.v0.MultiLabelClassification.n_classes', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dynamic_class_spec', full_name='tensorflow.metadata.v0.MultiLabelClassification.dynamic_class_spec', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\230\266\370\232\007\005'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='class_spec', full_name='tensorflow.metadata.v0.MultiLabelClassification.class_spec',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=572,
  serialized_end=752,
)


_TOPKCLASSIFICATION = _descriptor.Descriptor(
  name='TopKClassification',
  full_name='tensorflow.metadata.v0.TopKClassification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='tensorflow.metadata.v0.TopKClassification.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='example_weight', full_name='tensorflow.metadata.v0.TopKClassification.example_weight', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_classes', full_name='tensorflow.metadata.v0.TopKClassification.n_classes', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_predicted_labels', full_name='tensorflow.metadata.v0.TopKClassification.n_predicted_labels', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='predictions_order', full_name='tensorflow.metadata.v0.TopKClassification.predictions_order', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TOPKCLASSIFICATION_ORDER,
  ],
  serialized_options=_b('\230\266\370\232\007\003'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=755,
  serialized_end=1003,
)


_ONEDIMENSIONALREGRESSION = _descriptor.Descriptor(
  name='OneDimensionalRegression',
  full_name='tensorflow.metadata.v0.OneDimensionalRegression',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='tensorflow.metadata.v0.OneDimensionalRegression.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='tensorflow.metadata.v0.OneDimensionalRegression.weight', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\230\266\370\232\007\004'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1005,
  serialized_end=1070,
)


_TYPE = _descriptor.Descriptor(
  name='Type',
  full_name='tensorflow.metadata.v0.Type',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binary_classification', full_name='tensorflow.metadata.v0.Type.binary_classification', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='one_dimensional_regression', full_name='tensorflow.metadata.v0.Type.one_dimensional_regression', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multi_class_classification', full_name='tensorflow.metadata.v0.Type.multi_class_classification', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top_k_classification', full_name='tensorflow.metadata.v0.Type.top_k_classification', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multi_label_classification', full_name='tensorflow.metadata.v0.Type.multi_label_classification', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='task_type', full_name='tensorflow.metadata.v0.Type.task_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1073,
  serialized_end=1511,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='tensorflow.metadata.v0.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.metadata.v0.Task.type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.metadata.v0.Task.name', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_weight', full_name='tensorflow.metadata.v0.Task.task_weight', index=2,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objective_function', full_name='tensorflow.metadata.v0.Task.objective_function', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='performance_metric', full_name='tensorflow.metadata.v0.Task.performance_metric', index=4,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1514,
  serialized_end=1745,
)


_METAOPTIMIZATIONTARGET = _descriptor.Descriptor(
  name='MetaOptimizationTarget',
  full_name='tensorflow.metadata.v0.MetaOptimizationTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_name', full_name='tensorflow.metadata.v0.MetaOptimizationTarget.task_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.metadata.v0.MetaOptimizationTarget.type', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='performance_metric', full_name='tensorflow.metadata.v0.MetaOptimizationTarget.performance_metric', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='tensorflow.metadata.v0.MetaOptimizationTarget.weight', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1748,
  serialized_end=1922,
)


_PROBLEMSTATEMENT = _descriptor.Descriptor(
  name='ProblemStatement',
  full_name='tensorflow.metadata.v0.ProblemStatement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='tensorflow.metadata.v0.ProblemStatement.description', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='tensorflow.metadata.v0.ProblemStatement.owner', index=1,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='environment', full_name='tensorflow.metadata.v0.ProblemStatement.environment', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta_optimization_target', full_name='tensorflow.metadata.v0.ProblemStatement.meta_optimization_target', index=3,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multi_objective', full_name='tensorflow.metadata.v0.ProblemStatement.multi_objective', index=4,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='tensorflow.metadata.v0.ProblemStatement.tasks', index=5,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1925,
  serialized_end=2158,
)

_DYNAMICCLASSSPEC_OOVCLASSSPEC.containing_type = _DYNAMICCLASSSPEC
_DYNAMICCLASSSPEC.fields_by_name['oov_class_spec'].message_type = _DYNAMICCLASSSPEC_OOVCLASSSPEC
_MULTICLASSCLASSIFICATION.fields_by_name['dynamic_class_spec'].message_type = _DYNAMICCLASSSPEC
_MULTICLASSCLASSIFICATION.oneofs_by_name['class_spec'].fields.append(
  _MULTICLASSCLASSIFICATION.fields_by_name['n_classes'])
_MULTICLASSCLASSIFICATION.fields_by_name['n_classes'].containing_oneof = _MULTICLASSCLASSIFICATION.oneofs_by_name['class_spec']
_MULTICLASSCLASSIFICATION.oneofs_by_name['class_spec'].fields.append(
  _MULTICLASSCLASSIFICATION.fields_by_name['dynamic_class_spec'])
_MULTICLASSCLASSIFICATION.fields_by_name['dynamic_class_spec'].containing_oneof = _MULTICLASSCLASSIFICATION.oneofs_by_name['class_spec']
_MULTILABELCLASSIFICATION.fields_by_name['dynamic_class_spec'].message_type = _DYNAMICCLASSSPEC
_MULTILABELCLASSIFICATION.oneofs_by_name['class_spec'].fields.append(
  _MULTILABELCLASSIFICATION.fields_by_name['n_classes'])
_MULTILABELCLASSIFICATION.fields_by_name['n_classes'].containing_oneof = _MULTILABELCLASSIFICATION.oneofs_by_name['class_spec']
_MULTILABELCLASSIFICATION.oneofs_by_name['class_spec'].fields.append(
  _MULTILABELCLASSIFICATION.fields_by_name['dynamic_class_spec'])
_MULTILABELCLASSIFICATION.fields_by_name['dynamic_class_spec'].containing_oneof = _MULTILABELCLASSIFICATION.oneofs_by_name['class_spec']
_TOPKCLASSIFICATION.fields_by_name['predictions_order'].enum_type = _TOPKCLASSIFICATION_ORDER
_TOPKCLASSIFICATION_ORDER.containing_type = _TOPKCLASSIFICATION
_TYPE.fields_by_name['binary_classification'].message_type = _BINARYCLASSIFICATION
_TYPE.fields_by_name['one_dimensional_regression'].message_type = _ONEDIMENSIONALREGRESSION
_TYPE.fields_by_name['multi_class_classification'].message_type = _MULTICLASSCLASSIFICATION
_TYPE.fields_by_name['top_k_classification'].message_type = _TOPKCLASSIFICATION
_TYPE.fields_by_name['multi_label_classification'].message_type = _MULTILABELCLASSIFICATION
_TYPE.oneofs_by_name['task_type'].fields.append(
  _TYPE.fields_by_name['binary_classification'])
_TYPE.fields_by_name['binary_classification'].containing_oneof = _TYPE.oneofs_by_name['task_type']
_TYPE.oneofs_by_name['task_type'].fields.append(
  _TYPE.fields_by_name['one_dimensional_regression'])
_TYPE.fields_by_name['one_dimensional_regression'].containing_oneof = _TYPE.oneofs_by_name['task_type']
_TYPE.oneofs_by_name['task_type'].fields.append(
  _TYPE.fields_by_name['multi_class_classification'])
_TYPE.fields_by_name['multi_class_classification'].containing_oneof = _TYPE.oneofs_by_name['task_type']
_TYPE.oneofs_by_name['task_type'].fields.append(
  _TYPE.fields_by_name['top_k_classification'])
_TYPE.fields_by_name['top_k_classification'].containing_oneof = _TYPE.oneofs_by_name['task_type']
_TYPE.oneofs_by_name['task_type'].fields.append(
  _TYPE.fields_by_name['multi_label_classification'])
_TYPE.fields_by_name['multi_label_classification'].containing_oneof = _TYPE.oneofs_by_name['task_type']
_TASK.fields_by_name['type'].message_type = _TYPE
_TASK.fields_by_name['objective_function'].message_type = tensorflow__metadata_dot_proto_dot_v0_dot_metric__pb2._OBJECTIVEFUNCTION
_TASK.fields_by_name['performance_metric'].message_type = tensorflow__metadata_dot_proto_dot_v0_dot_metric__pb2._PERFORMANCEMETRIC
_METAOPTIMIZATIONTARGET.fields_by_name['type'].message_type = _TYPE
_METAOPTIMIZATIONTARGET.fields_by_name['performance_metric'].message_type = tensorflow__metadata_dot_proto_dot_v0_dot_metric__pb2._PERFORMANCEMETRIC
_PROBLEMSTATEMENT.fields_by_name['meta_optimization_target'].message_type = _METAOPTIMIZATIONTARGET
_PROBLEMSTATEMENT.fields_by_name['tasks'].message_type = _TASK
DESCRIPTOR.message_types_by_name['BinaryClassification'] = _BINARYCLASSIFICATION
DESCRIPTOR.message_types_by_name['DynamicClassSpec'] = _DYNAMICCLASSSPEC
DESCRIPTOR.message_types_by_name['MultiClassClassification'] = _MULTICLASSCLASSIFICATION
DESCRIPTOR.message_types_by_name['MultiLabelClassification'] = _MULTILABELCLASSIFICATION
DESCRIPTOR.message_types_by_name['TopKClassification'] = _TOPKCLASSIFICATION
DESCRIPTOR.message_types_by_name['OneDimensionalRegression'] = _ONEDIMENSIONALREGRESSION
DESCRIPTOR.message_types_by_name['Type'] = _TYPE
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['MetaOptimizationTarget'] = _METAOPTIMIZATIONTARGET
DESCRIPTOR.message_types_by_name['ProblemStatement'] = _PROBLEMSTATEMENT
DESCRIPTOR.enum_types_by_name['TaskType'] = _TASKTYPE
DESCRIPTOR.extensions_by_name['task_type'] = task_type
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BinaryClassification = _reflection.GeneratedProtocolMessageType('BinaryClassification', (_message.Message,), {
  'DESCRIPTOR' : _BINARYCLASSIFICATION,
  '__module__' : 'tensorflow_metadata.proto.v0.problem_statement_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.metadata.v0.BinaryClassification)
  })
_sym_db.RegisterMessage(BinaryClassification)

DynamicClassSpec = _reflection.GeneratedProtocolMessageType('DynamicClassSpec', (_message.Message,), {

  'OovClassSpec' : _reflection.GeneratedProtocolMessageType('OovClassSpec', (_message.Message,), {
    'DESCRIPTOR' : _DYNAMICCLASSSPEC_OOVCLASSSPEC,
    '__module__' : 'tensorflow_metadata.proto.v0.problem_statement_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.metadata.v0.DynamicClassSpec.OovClassSpec)
    })
  ,
  'DESCRIPTOR' : _DYNAMICCLASSSPEC,
  '__module__' : 'tensorflow_metadata.proto.v0.problem_statement_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.metadata.v0.DynamicClassSpec)
  })
_sym_db.RegisterMessage(DynamicClassSpec)
_sym_db.RegisterMessage(DynamicClassSpec.OovClassSpec)

MultiClassClassification = _reflection.GeneratedProtocolMessageType('MultiClassClassification', (_message.Message,), {
  'DESCRIPTOR' : _MULTICLASSCLASSIFICATION,
  '__module__' : 'tensorflow_metadata.proto.v0.problem_statement_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.metadata.v0.MultiClassClassification)
  })
_sym_db.RegisterMessage(MultiClassClassification)

MultiLabelClassification = _reflection.GeneratedProtocolMessageType('MultiLabelClassification', (_message.Message,), {
  'DESCRIPTOR' : _MULTILABELCLASSIFICATION,
  '__module__' : 'tensorflow_metadata.proto.v0.problem_statement_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.metadata.v0.MultiLabelClassification)
  })
_sym_db.RegisterMessage(MultiLabelClassification)

TopKClassification = _reflection.GeneratedProtocolMessageType('TopKClassification', (_message.Message,), {
  'DESCRIPTOR' : _TOPKCLASSIFICATION,
  '__module__' : 'tensorflow_metadata.proto.v0.problem_statement_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.metadata.v0.TopKClassification)
  })
_sym_db.RegisterMessage(TopKClassification)

OneDimensionalRegression = _reflection.GeneratedProtocolMessageType('OneDimensionalRegression', (_message.Message,), {
  'DESCRIPTOR' : _ONEDIMENSIONALREGRESSION,
  '__module__' : 'tensorflow_metadata.proto.v0.problem_statement_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.metadata.v0.OneDimensionalRegression)
  })
_sym_db.RegisterMessage(OneDimensionalRegression)

Type = _reflection.GeneratedProtocolMessageType('Type', (_message.Message,), {
  'DESCRIPTOR' : _TYPE,
  '__module__' : 'tensorflow_metadata.proto.v0.problem_statement_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.metadata.v0.Type)
  })
_sym_db.RegisterMessage(Type)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'tensorflow_metadata.proto.v0.problem_statement_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.metadata.v0.Task)
  })
_sym_db.RegisterMessage(Task)

MetaOptimizationTarget = _reflection.GeneratedProtocolMessageType('MetaOptimizationTarget', (_message.Message,), {
  'DESCRIPTOR' : _METAOPTIMIZATIONTARGET,
  '__module__' : 'tensorflow_metadata.proto.v0.problem_statement_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.metadata.v0.MetaOptimizationTarget)
  })
_sym_db.RegisterMessage(MetaOptimizationTarget)

ProblemStatement = _reflection.GeneratedProtocolMessageType('ProblemStatement', (_message.Message,), {
  'DESCRIPTOR' : _PROBLEMSTATEMENT,
  '__module__' : 'tensorflow_metadata.proto.v0.problem_statement_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.metadata.v0.ProblemStatement)
  })
_sym_db.RegisterMessage(ProblemStatement)

task_type.enum_type = _TASKTYPE
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(task_type)

DESCRIPTOR._options = None
_BINARYCLASSIFICATION._options = None
_MULTICLASSCLASSIFICATION._options = None
_MULTILABELCLASSIFICATION._options = None
_TOPKCLASSIFICATION._options = None
_ONEDIMENSIONALREGRESSION._options = None
_TASK.fields_by_name['objective_function']._options = None
# @@protoc_insertion_point(module_scope)
