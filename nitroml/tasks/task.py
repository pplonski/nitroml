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
r"""An AutoML benchmark tasks."""

import abc
from typing import Any, Dict, List
from tfx import types
from tfx.components.base import base_component


class Task(abc.ABC):
  r"""Defines a Task for AutoML."""

  @abc.abstractproperty
  def name(self) -> str:
    """Returns the task's name."""

  @abc.abstractproperty
  def components(self) -> List[base_component.BaseComponent]:
    """Returns TFX components required for the task."""

  @abc.abstractproperty
  def examples(self) -> types.Channel:
    """Returns train and eval labeled examples."""

  @abc.abstractmethod
  def to_dict(self) -> Dict[str, Any]:
    """Convert task attributes to a dictionary."""
