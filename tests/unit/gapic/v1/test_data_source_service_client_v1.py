# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
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

"""Unit tests."""

import mock
import pytest

from google.cloud.bigquery import datatransfer_v1
from google.cloud.bigquery.datatransfer_v1.proto import datasource_pb2
from google.cloud.bigquery.datatransfer_v1.proto import transfer_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2



class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""
    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response


class ChannelStub(object):
    """Stub for the grpc.Channel interface."""
    def __init__(self, responses = []):
        self.responses = responses
        self.requests = []

    def unary_unary(
            self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)


class CustomException(Exception):
    pass


class TestDataSourceServiceClient(object):

    def test_update_transfer_run(self):
        # Setup Expected Response
        name = 'name3373707'
        destination_dataset_id = 'destinationDatasetId1541564179'
        data_source_id = 'dataSourceId-1015796374'
        user_id = 147132913
        schedule = 'schedule-697920873'
        notification_pubsub_topic = 'notificationPubsubTopic1794281191'
        partner_token = 'partnerToken725173186'
        expected_response = {'name': name, 'destination_dataset_id': destination_dataset_id, 'data_source_id': data_source_id, 'user_id': user_id, 'schedule': schedule, 'notification_pubsub_topic': notification_pubsub_topic, 'partner_token': partner_token}
        expected_response = transfer_pb2.TransferRun(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup Request
        transfer_run = {}
        update_mask = {}

        response = client.update_transfer_run(transfer_run, update_mask)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = datasource_pb2.UpdateTransferRunRequest(transfer_run=transfer_run, update_mask=update_mask)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_transfer_run_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup request
        transfer_run = {}
        update_mask = {}

        with pytest.raises(CustomException):
            client.update_transfer_run(transfer_run, update_mask)

    def test_log_transfer_run_messages(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup Request
        name = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')
        transfer_messages = []

        client.log_transfer_run_messages(name, transfer_messages)

        assert len(channel.requests) == 1
        expected_request = datasource_pb2.LogTransferRunMessagesRequest(name=name, transfer_messages=transfer_messages)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_log_transfer_run_messages_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup request
        name = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')
        transfer_messages = []

        with pytest.raises(CustomException):
            client.log_transfer_run_messages(name, transfer_messages)

    def test_start_big_query_jobs(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup Request
        name = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')
        imported_data = []

        client.start_big_query_jobs(name, imported_data)

        assert len(channel.requests) == 1
        expected_request = datasource_pb2.StartBigQueryJobsRequest(name=name, imported_data=imported_data)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_start_big_query_jobs_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup request
        name = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')
        imported_data = []

        with pytest.raises(CustomException):
            client.start_big_query_jobs(name, imported_data)

    def test_finish_run(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup Request
        name = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')

        client.finish_run(name)

        assert len(channel.requests) == 1
        expected_request = datasource_pb2.FinishRunRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_finish_run_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup request
        name = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')

        with pytest.raises(CustomException):
            client.finish_run(name)

    def test_create_data_source_definition(self):
        # Setup Expected Response
        name = 'name3373707'
        transfer_run_pubsub_topic = 'transferRunPubsubTopic-1740562661'
        support_email = 'supportEmail-648030420'
        service_account = 'serviceAccount-1948028253'
        disabled = True
        transfer_config_pubsub_topic = 'transferConfigPubsubTopic71465884'
        expected_response = {'name': name, 'transfer_run_pubsub_topic': transfer_run_pubsub_topic, 'support_email': support_email, 'service_account': service_account, 'disabled': disabled, 'transfer_config_pubsub_topic': transfer_config_pubsub_topic}
        expected_response = datasource_pb2.DataSourceDefinition(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup Request
        parent = client.location_path('[PROJECT]', '[LOCATION]')
        data_source_definition = {}

        response = client.create_data_source_definition(parent, data_source_definition)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = datasource_pb2.CreateDataSourceDefinitionRequest(parent=parent, data_source_definition=data_source_definition)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_data_source_definition_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup request
        parent = client.location_path('[PROJECT]', '[LOCATION]')
        data_source_definition = {}

        with pytest.raises(CustomException):
            client.create_data_source_definition(parent, data_source_definition)

    def test_update_data_source_definition(self):
        # Setup Expected Response
        name = 'name3373707'
        transfer_run_pubsub_topic = 'transferRunPubsubTopic-1740562661'
        support_email = 'supportEmail-648030420'
        service_account = 'serviceAccount-1948028253'
        disabled = True
        transfer_config_pubsub_topic = 'transferConfigPubsubTopic71465884'
        expected_response = {'name': name, 'transfer_run_pubsub_topic': transfer_run_pubsub_topic, 'support_email': support_email, 'service_account': service_account, 'disabled': disabled, 'transfer_config_pubsub_topic': transfer_config_pubsub_topic}
        expected_response = datasource_pb2.DataSourceDefinition(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup Request
        data_source_definition = {}
        update_mask = {}

        response = client.update_data_source_definition(data_source_definition, update_mask)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = datasource_pb2.UpdateDataSourceDefinitionRequest(data_source_definition=data_source_definition, update_mask=update_mask)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_data_source_definition_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup request
        data_source_definition = {}
        update_mask = {}

        with pytest.raises(CustomException):
            client.update_data_source_definition(data_source_definition, update_mask)

    def test_delete_data_source_definition(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup Request
        name = client.data_source_definition_path('[PROJECT]', '[LOCATION]', '[DATA_SOURCE_DEFINITION]')

        client.delete_data_source_definition(name)

        assert len(channel.requests) == 1
        expected_request = datasource_pb2.DeleteDataSourceDefinitionRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_data_source_definition_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup request
        name = client.data_source_definition_path('[PROJECT]', '[LOCATION]', '[DATA_SOURCE_DEFINITION]')

        with pytest.raises(CustomException):
            client.delete_data_source_definition(name)

    def test_get_data_source_definition(self):
        # Setup Expected Response
        name_2 = 'name2-1052831874'
        transfer_run_pubsub_topic = 'transferRunPubsubTopic-1740562661'
        support_email = 'supportEmail-648030420'
        service_account = 'serviceAccount-1948028253'
        disabled = True
        transfer_config_pubsub_topic = 'transferConfigPubsubTopic71465884'
        expected_response = {'name': name_2, 'transfer_run_pubsub_topic': transfer_run_pubsub_topic, 'support_email': support_email, 'service_account': service_account, 'disabled': disabled, 'transfer_config_pubsub_topic': transfer_config_pubsub_topic}
        expected_response = datasource_pb2.DataSourceDefinition(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup Request
        name = client.data_source_definition_path('[PROJECT]', '[LOCATION]', '[DATA_SOURCE_DEFINITION]')

        response = client.get_data_source_definition(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = datasource_pb2.GetDataSourceDefinitionRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_data_source_definition_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup request
        name = client.data_source_definition_path('[PROJECT]', '[LOCATION]', '[DATA_SOURCE_DEFINITION]')

        with pytest.raises(CustomException):
            client.get_data_source_definition(name)

    def test_list_data_source_definitions(self):
        # Setup Expected Response
        next_page_token = ''
        data_source_definitions_element = {}
        data_source_definitions = [data_source_definitions_element]
        expected_response = {'next_page_token': next_page_token, 'data_source_definitions': data_source_definitions}
        expected_response = datasource_pb2.ListDataSourceDefinitionsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup Request
        parent = client.location_path('[PROJECT]', '[LOCATION]')

        paged_list_response = client.list_data_source_definitions(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.data_source_definitions[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = datasource_pb2.ListDataSourceDefinitionsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_data_source_definitions_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataSourceServiceClient()

        # Setup request
        parent = client.location_path('[PROJECT]', '[LOCATION]')

        paged_list_response = client.list_data_source_definitions(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)
