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
from google.cloud.bigquery.datatransfer_v1.proto import datatransfer_pb2
from google.cloud.bigquery.datatransfer_v1.proto import transfer_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import timestamp_pb2



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


class TestDataTransferServiceClient(object):

    def test_get_data_source(self):
        # Setup Expected Response
        name_2 = 'name2-1052831874'
        data_source_id = 'dataSourceId-1015796374'
        display_name = 'displayName1615086568'
        description = 'description-1724546052'
        client_id = 'clientId-1904089585'
        supports_multiple_transfers = True
        update_deadline_seconds = 991471694
        default_schedule = 'defaultSchedule-800168235'
        supports_custom_schedule = True
        help_url = 'helpUrl-789431439'
        default_data_refresh_window_days = 1804935157
        manual_runs_disabled = True
        partner_legal_name = 'partnerLegalName-1307326424'
        redirect_url = 'redirectUrl951230092'
        expected_response = {'name': name_2, 'data_source_id': data_source_id, 'display_name': display_name, 'description': description, 'client_id': client_id, 'supports_multiple_transfers': supports_multiple_transfers, 'update_deadline_seconds': update_deadline_seconds, 'default_schedule': default_schedule, 'supports_custom_schedule': supports_custom_schedule, 'help_url': help_url, 'default_data_refresh_window_days': default_data_refresh_window_days, 'manual_runs_disabled': manual_runs_disabled, 'partner_legal_name': partner_legal_name, 'redirect_url': redirect_url}
        expected_response = datatransfer_pb2.DataSource(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        name = client.data_source_path('[PROJECT]', '[LOCATION]', '[DATA_SOURCE]')

        response = client.get_data_source(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.GetDataSourceRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_data_source_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        name = client.data_source_path('[PROJECT]', '[LOCATION]', '[DATA_SOURCE]')

        with pytest.raises(CustomException):
            client.get_data_source(name)

    def test_list_data_sources(self):
        # Setup Expected Response
        next_page_token = ''
        data_sources_element = {}
        data_sources = [data_sources_element]
        expected_response = {'next_page_token': next_page_token, 'data_sources': data_sources}
        expected_response = datatransfer_pb2.ListDataSourcesResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        parent = client.location_path('[PROJECT]', '[LOCATION]')

        paged_list_response = client.list_data_sources(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.data_sources[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.ListDataSourcesRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_data_sources_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        parent = client.location_path('[PROJECT]', '[LOCATION]')

        paged_list_response = client.list_data_sources(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_create_transfer_config(self):
        # Setup Expected Response
        name = 'name3373707'
        destination_dataset_id = 'destinationDatasetId1541564179'
        display_name = 'displayName1615086568'
        data_source_id = 'dataSourceId-1015796374'
        schedule = 'schedule-697920873'
        data_refresh_window_days = 327632845
        disabled = True
        user_id = 147132913
        dataset_region = 'datasetRegion959248539'
        notification_pubsub_topic = 'notificationPubsubTopic1794281191'
        partner_token = 'partnerToken725173186'
        expected_response = {'name': name, 'destination_dataset_id': destination_dataset_id, 'display_name': display_name, 'data_source_id': data_source_id, 'schedule': schedule, 'data_refresh_window_days': data_refresh_window_days, 'disabled': disabled, 'user_id': user_id, 'dataset_region': dataset_region, 'notification_pubsub_topic': notification_pubsub_topic, 'partner_token': partner_token}
        expected_response = transfer_pb2.TransferConfig(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        parent = client.location_path('[PROJECT]', '[LOCATION]')
        transfer_config = {}

        response = client.create_transfer_config(parent, transfer_config)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.CreateTransferConfigRequest(parent=parent, transfer_config=transfer_config)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_transfer_config_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        parent = client.location_path('[PROJECT]', '[LOCATION]')
        transfer_config = {}

        with pytest.raises(CustomException):
            client.create_transfer_config(parent, transfer_config)

    def test_update_transfer_config(self):
        # Setup Expected Response
        name = 'name3373707'
        destination_dataset_id = 'destinationDatasetId1541564179'
        display_name = 'displayName1615086568'
        data_source_id = 'dataSourceId-1015796374'
        schedule = 'schedule-697920873'
        data_refresh_window_days = 327632845
        disabled = True
        user_id = 147132913
        dataset_region = 'datasetRegion959248539'
        notification_pubsub_topic = 'notificationPubsubTopic1794281191'
        partner_token = 'partnerToken725173186'
        expected_response = {'name': name, 'destination_dataset_id': destination_dataset_id, 'display_name': display_name, 'data_source_id': data_source_id, 'schedule': schedule, 'data_refresh_window_days': data_refresh_window_days, 'disabled': disabled, 'user_id': user_id, 'dataset_region': dataset_region, 'notification_pubsub_topic': notification_pubsub_topic, 'partner_token': partner_token}
        expected_response = transfer_pb2.TransferConfig(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        transfer_config = {}
        authorization_code = 'authorizationCode1571154419'
        update_mask = {}

        response = client.update_transfer_config(transfer_config, authorization_code, update_mask)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.UpdateTransferConfigRequest(transfer_config=transfer_config, authorization_code=authorization_code, update_mask=update_mask)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_transfer_config_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        transfer_config = {}
        authorization_code = 'authorizationCode1571154419'
        update_mask = {}

        with pytest.raises(CustomException):
            client.update_transfer_config(transfer_config, authorization_code, update_mask)

    def test_delete_transfer_config(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        name = client.transfer_config_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]')

        client.delete_transfer_config(name)

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.DeleteTransferConfigRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_transfer_config_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        name = client.transfer_config_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]')

        with pytest.raises(CustomException):
            client.delete_transfer_config(name)

    def test_get_transfer_config(self):
        # Setup Expected Response
        name_2 = 'name2-1052831874'
        destination_dataset_id = 'destinationDatasetId1541564179'
        display_name = 'displayName1615086568'
        data_source_id = 'dataSourceId-1015796374'
        schedule = 'schedule-697920873'
        data_refresh_window_days = 327632845
        disabled = True
        user_id = 147132913
        dataset_region = 'datasetRegion959248539'
        notification_pubsub_topic = 'notificationPubsubTopic1794281191'
        partner_token = 'partnerToken725173186'
        expected_response = {'name': name_2, 'destination_dataset_id': destination_dataset_id, 'display_name': display_name, 'data_source_id': data_source_id, 'schedule': schedule, 'data_refresh_window_days': data_refresh_window_days, 'disabled': disabled, 'user_id': user_id, 'dataset_region': dataset_region, 'notification_pubsub_topic': notification_pubsub_topic, 'partner_token': partner_token}
        expected_response = transfer_pb2.TransferConfig(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        name = client.transfer_config_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]')

        response = client.get_transfer_config(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.GetTransferConfigRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_transfer_config_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        name = client.transfer_config_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]')

        with pytest.raises(CustomException):
            client.get_transfer_config(name)

    def test_list_transfer_configs(self):
        # Setup Expected Response
        next_page_token = ''
        transfer_configs_element = {}
        transfer_configs = [transfer_configs_element]
        expected_response = {'next_page_token': next_page_token, 'transfer_configs': transfer_configs}
        expected_response = datatransfer_pb2.ListTransferConfigsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        parent = client.location_path('[PROJECT]', '[LOCATION]')
        data_source_ids = []

        paged_list_response = client.list_transfer_configs(parent, data_source_ids)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.transfer_configs[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.ListTransferConfigsRequest(parent=parent, data_source_ids=data_source_ids)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_transfer_configs_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        parent = client.location_path('[PROJECT]', '[LOCATION]')
        data_source_ids = []

        paged_list_response = client.list_transfer_configs(parent, data_source_ids)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_schedule_transfer_runs(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = datatransfer_pb2.ScheduleTransferRunsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        parent = client.transfer_config_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]')
        labels = {}
        start_time = {}
        end_time = {}

        response = client.schedule_transfer_runs(parent, labels, start_time, end_time)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.ScheduleTransferRunsRequest(parent=parent, labels=labels, start_time=start_time, end_time=end_time)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_schedule_transfer_runs_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        parent = client.transfer_config_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]')
        labels = {}
        start_time = {}
        end_time = {}

        with pytest.raises(CustomException):
            client.schedule_transfer_runs(parent, labels, start_time, end_time)

    def test_start_manual_transfer_runs(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = datatransfer_pb2.StartManualTransferRunsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        parent = client.transfer_config_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]')

        response = client.start_manual_transfer_runs(parent)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.StartManualTransferRunsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_start_manual_transfer_runs_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        parent = client.transfer_config_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]')

        with pytest.raises(CustomException):
            client.start_manual_transfer_runs(parent)

    def test_get_transfer_run(self):
        # Setup Expected Response
        name_2 = 'name2-1052831874'
        destination_dataset_id = 'destinationDatasetId1541564179'
        data_source_id = 'dataSourceId-1015796374'
        user_id = 147132913
        schedule = 'schedule-697920873'
        notification_pubsub_topic = 'notificationPubsubTopic1794281191'
        partner_token = 'partnerToken725173186'
        expected_response = {'name': name_2, 'destination_dataset_id': destination_dataset_id, 'data_source_id': data_source_id, 'user_id': user_id, 'schedule': schedule, 'notification_pubsub_topic': notification_pubsub_topic, 'partner_token': partner_token}
        expected_response = transfer_pb2.TransferRun(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        name = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')

        response = client.get_transfer_run(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.GetTransferRunRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_transfer_run_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        name = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')

        with pytest.raises(CustomException):
            client.get_transfer_run(name)

    def test_delete_transfer_run(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        name = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')

        client.delete_transfer_run(name)

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.DeleteTransferRunRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_transfer_run_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        name = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')

        with pytest.raises(CustomException):
            client.delete_transfer_run(name)

    def test_list_transfer_runs(self):
        # Setup Expected Response
        next_page_token = ''
        transfer_runs_element = {}
        transfer_runs = [transfer_runs_element]
        expected_response = {'next_page_token': next_page_token, 'transfer_runs': transfer_runs}
        expected_response = datatransfer_pb2.ListTransferRunsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        parent = client.transfer_config_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]')

        paged_list_response = client.list_transfer_runs(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.transfer_runs[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.ListTransferRunsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_transfer_runs_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        parent = client.transfer_config_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]')

        paged_list_response = client.list_transfer_runs(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_list_transfer_logs(self):
        # Setup Expected Response
        next_page_token = ''
        transfer_messages_element = {}
        transfer_messages = [transfer_messages_element]
        expected_response = {'next_page_token': next_page_token, 'transfer_messages': transfer_messages}
        expected_response = datatransfer_pb2.ListTransferLogsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        parent = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')

        paged_list_response = client.list_transfer_logs(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.transfer_messages[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.ListTransferLogsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_transfer_logs_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        parent = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')

        paged_list_response = client.list_transfer_logs(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_check_valid_creds(self):
        # Setup Expected Response
        has_valid_creds = False
        expected_response = {'has_valid_creds': has_valid_creds}
        expected_response = datatransfer_pb2.CheckValidCredsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        name = client.data_source_path('[PROJECT]', '[LOCATION]', '[DATA_SOURCE]')

        response = client.check_valid_creds(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.CheckValidCredsRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_check_valid_creds_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        name = client.data_source_path('[PROJECT]', '[LOCATION]', '[DATA_SOURCE]')

        with pytest.raises(CustomException):
            client.check_valid_creds(name)

    def test_enable_data_transfer_service(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        name = client.location_path('[PROJECT]', '[LOCATION]')

        client.enable_data_transfer_service(name)

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.EnableDataTransferServiceRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_enable_data_transfer_service_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        name = client.location_path('[PROJECT]', '[LOCATION]')

        with pytest.raises(CustomException):
            client.enable_data_transfer_service(name)

    def test_is_data_transfer_service_enabled(self):
        # Setup Expected Response
        enabled = False
        reason = 'reason-934964668'
        expected_response = {'enabled': enabled, 'reason': reason}
        expected_response = datatransfer_pb2.IsDataTransferServiceEnabledResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup Request
        name = client.location_path('[PROJECT]', '[LOCATION]')

        response = client.is_data_transfer_service_enabled(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = datatransfer_pb2.IsDataTransferServiceEnabledRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_is_data_transfer_service_enabled_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = datatransfer_v1.DataTransferServiceClient()

        # Setup request
        name = client.location_path('[PROJECT]', '[LOCATION]')

        with pytest.raises(CustomException):
            client.is_data_transfer_service_enabled(name)
