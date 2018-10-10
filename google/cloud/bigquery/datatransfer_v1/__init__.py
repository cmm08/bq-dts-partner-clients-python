# -*- coding: utf-8 -*-
#
# Copyright 2018 Google LLC
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

from __future__ import absolute_import

from google.cloud.bigquery.datatransfer_v1 import types
from google.cloud.bigquery.datatransfer_v1.gapic import data_source_service_client
from google.cloud.bigquery.datatransfer_v1.gapic import data_transfer_service_client
from google.cloud.bigquery.datatransfer_v1.gapic import enums


class DataTransferServiceClient(
        data_transfer_service_client.DataTransferServiceClient):
    __doc__ = data_transfer_service_client.DataTransferServiceClient.__doc__
    enums = enums


class DataSourceServiceClient(
        data_source_service_client.DataSourceServiceClient):
    __doc__ = data_source_service_client.DataSourceServiceClient.__doc__
    enums = enums


__all__ = (
    'enums',
    'types',
    'DataTransferServiceClient',
    'DataSourceServiceClient',
)