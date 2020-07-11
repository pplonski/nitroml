"""Utilities for testing datasets."""

import json
import os

from nitroml.datasets import data_utils
from nitroml.datasets import openml_cc18
import requests_mock
import tensorflow as tf


def register_mock_urls(mocker: requests_mock.Mocker):
  """Registers mock URLs to the Mocker."""

  list_url = f'{openml_cc18._OPENML_API_URL}/data/list'  # pylint: disable=protected-access
  dataset_id = 1

  for name, value in data_utils.parse_dataset_filters(
      openml_cc18._DATASET_FILTERS).items():  # pylint: disable=protected-access
    list_url = f'{list_url}/{name}/{value}'

  with tf.io.gfile.GFile(
      _filename_path('openml_list.get.json'), mode='r') as fin:
    mocker.get(list_url, json=json.load(fin), status_code=200)

  desc_url = f'{openml_cc18._OPENML_API_URL}/data/{dataset_id}'  # pylint: disable=protected-access

  with tf.io.gfile.GFile(
      _filename_path('openml_description.get.json'), mode='r') as fin:
    mocker.get(desc_url, json=json.load(fin), status_code=200)

  qual_url = f'{openml_cc18._OPENML_API_URL}/data/qualities/{dataset_id}'  # pylint: disable=protected-access

  with tf.io.gfile.GFile(
      _filename_path('openml_qual.get.json'), mode='r') as fin:
    mocker.get(qual_url, json=json.load(fin), status_code=200)

  csv_url = f'{openml_cc18._OPENML_FILE_API_URL}/get_csv/{dataset_id}'  # pylint: disable=protected-access

  with tf.io.gfile.GFile(_filename_path('dataset.txt'), mode='r') as fin:
    mocker.get(csv_url, text=fin.read())


def _filename_path(filename: str) -> str:
  return os.path.join(os.path.dirname(__file__), 'testdata', filename)
