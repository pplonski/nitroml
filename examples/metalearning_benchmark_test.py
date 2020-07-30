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
# =============================================================================
# Lint as: python3
"""Tests for nitroml.examples.metalearning_benchmark."""

import os

from nitroml import results
from examples import metalearning_benchmark
from nitroml.suites import testing_utils
from nitroml.testing import e2etest
import requests_mock

from ml_metadata import metadata_store


class MetaLearningTest(e2etest.TestCase):

  def setUp(self):
    super(MetaLearningTest, self).setUp('nitroml_metalearning_openml')

  @e2etest.parameterized.named_parameters({
      'testcase_name': 'metalearning_algo_majority-voting',
      'algorithm': 'majority_voting',
  })
  def test(self, algorithm):
    with requests_mock.Mocker() as mocker:
      testing_utils.register_mock_urls(mocker)
      self.run_benchmarks([metalearning_benchmark.MetaLearningBenchmark()],
                          data_dir=os.path.join(self.pipeline_root,
                                                'mock_metalearning_openml'),
                          mock_data=True,
                          algorithm=algorithm)

    self.assertComponentExecutionCount(14)

    train_dataset_ids = [1]
    for ix in train_dataset_ids:
      instance_name = 'MetaLearningBenchmark.benchmark.OpenML.mockdata_2'
      self.assertComponentSucceeded(
          f'CsvExampleGen.OpenML.mockdata_{ix}.{instance_name}')
      self.assertComponentSucceeded(
          f'Tuner.train_OpenML.mockdata_{ix}.{instance_name}')
      self.assertComponentSucceeded(
          f'SchemaGen.AutoData.train_OpenML.mockdata_{ix}.{instance_name}')
      self.assertComponentSucceeded(
          f'StatisticsGen.AutoData.train_OpenML.mockdata_{ix}.{instance_name}')
      self.assertComponentSucceeded(
          f'Transform.AutoData.train_OpenML.mockdata_{ix}.{instance_name}')

    test_dataset_ids = [2]
    for ix in test_dataset_ids:
      instance_name = 'MetaLearningBenchmark.benchmark.OpenML.mockdata_2'
      self.assertComponentSucceeded(
          f'CsvExampleGen.OpenML.mockdata_{ix}.{instance_name}')
      self.assertComponentSucceeded(
          f'SchemaGen.AutoData.test_OpenML.mockdata_{ix}.{instance_name}')
      self.assertComponentSucceeded(
          f'StatisticsGen.AutoData.test_OpenML.mockdata_{ix}.{instance_name}')
      self.assertComponentSucceeded(
          f'Transform.AutoData.test_OpenML.mockdata_{ix}.{instance_name}')

    instance_name = 'MetaLearningBenchmark.benchmark.OpenML.mockdata_2'
    self.assertComponentSucceeded(f'Evaluator.{instance_name}')
    self.assertComponentSucceeded(f'BenchmarkResultPublisher.{instance_name}')

    # Load benchmark results.
    store = metadata_store.MetadataStore(self.metadata_config)
    df = results.overview(store)
    # Check benchmark results overview values.
    self.assertEqual(len(df.index), 1)
    self.assertContainsSubset([
        'benchmark',
        'run',
        'num_runs',
        'accuracy',
        'average_loss',
        'post_export_metrics/example_count',
    ], df.columns.values.tolist())
    self.assertSameElements([1], df['run'].tolist())
    self.assertSameElements([1], df['num_runs'].tolist())
    self.assertSameElements([instance_name], df.benchmark.unique())


if __name__ == '__main__':
  e2etest.main()