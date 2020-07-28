# Lint as: python3
# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for nitroml.components.tuner.executor."""

import json
import os
from kerastuner import HyperParameters
import tensorflow as tf
import tempfile

from absl import flags
from absl.testing import absltest
from tensorflow.python.lib.io import file_io  # pylint: disable=g-direct-tensorflow-import
from tfx.proto import trainer_pb2
from tfx.proto import tuner_pb2
from tfx.types import artifact_utils
from tfx.types import standard_artifacts
from tfx.utils import json_utils
from nitroml.protos import problem_statement_pb2 as ps_pb2
from nitroml.components.tuner import executor
from examples import auto_trainer as tuner_module
from google.protobuf import json_format
from google.protobuf import text_format


class ExecutorTest(absltest.TestCase):

  def setUp(self):
    super(ExecutorTest, self).setUp()

    source_data_dir = os.path.dirname(os.path.dirname(__file__))
    self._testdata_dir = os.path.join(source_data_dir, 'testdata')

    self._output_data_dir = os.path.join(
        os.environ.get('TEST_UNDECLARED_OUTPUTS_DIR',
                       tempfile.mkdtemp(dir=flags.FLAGS.test_tmpdir)),
        self._testMethodName)

    self._context = executor.Executor.Context(
        tmp_dir=self._output_data_dir, unique_id='1')

    # Create input dict.
    examples = standard_artifacts.Examples()
    examples.uri = os.path.join(self._testdata_dir, 'Transform.mockdata_1',
                                'transformed_examples', '10')
    examples.split_names = artifact_utils.encode_split_names(['train', 'eval'])

    schema = standard_artifacts.Schema()
    schema.uri = os.path.join(self._testdata_dir, 'SchemaGen.mockdata_1',
                              'schema', '1')

    transform_output = standard_artifacts.TransformGraph()
    transform_output.uri = os.path.join(self._testdata_dir,
                                        'Transform.mockdata_1',
                                        'transform_graph', '10')

    self._input_dict = {
        'examples': [examples],
        'schema': [schema],
        'transform_graph': [transform_output],
    }

    # Create output dict.
    self._best_hparams = standard_artifacts.Model()
    self._best_hparams.uri = os.path.join(self._output_data_dir, 'best_hparams')

    self._output_dict = {
        'best_hyperparameters': [self._best_hparams],
    }

    # Create exec properties.
    self._exec_properties = {
        'train_args':
            json_format.MessageToJson(
                trainer_pb2.TrainArgs(num_steps=100),
                preserving_proto_field_name=True),
        'eval_args':
            json_format.MessageToJson(
                trainer_pb2.EvalArgs(num_steps=10),
                preserving_proto_field_name=True),
    }

  def _verify_output(self):
    # Test best hparams.
    best_hparams_path = os.path.join(self._best_hparams.uri,
                                     'best_hyperparameters.txt')
    self.assertTrue(tf.io.gfile.exists(best_hparams_path))
    best_hparams_config = json.loads(
        file_io.read_file_to_string(best_hparams_path))
    best_hparams = HyperParameters.from_config(best_hparams_config)
    self.assertIn(best_hparams.get('learning_rate'), (1e-1, 1e-2, 1e-3))
    self.assertBetween(best_hparams.get('num_layers'), 1, 5)

  def testDoWithTunerFn(self):

    self._exec_properties['tuner_fn'] = '%s.%s' % (
        tuner_module.tuner_fn.__module__, tuner_module.tuner_fn.__name__)

    ps_type = ps_pb2.Type(
        binary_classification=ps_pb2.BinaryClassification(label='class'))
    ps = ps_pb2.ProblemStatement(
        owner=['nitroml'],
        tasks=[ps_pb2.Task(
            name='mockdata_1',
            type=ps_type,
        )])

    self._exec_properties['custom_config'] = json_utils.dumps({
        'problem_statement':
            text_format.MessageToString(message=ps, as_utf8=True),
    })

    tuner = executor.Executor(self._context)
    tuner.Do(
        input_dict=self._input_dict,
        output_dict=self._output_dict,
        exec_properties=self._exec_properties)

    self._verify_output()

  def testTuneArgs(self):
    with self.assertRaises(ValueError):
      self._exec_properties['tune_args'] = json_format.MessageToJson(
          tuner_pb2.TuneArgs(num_parallel_trials=3),
          preserving_proto_field_name=True)

      tuner = executor.Executor(self._context)
      tuner.Do(
          input_dict=self._input_dict,
          output_dict=self._output_dict,
          exec_properties=self._exec_properties)


if __name__ == '__main__':
  absltest.main()