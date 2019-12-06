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


import google.api_core.grpc_helpers

from google.cloud.bigquery.datatransfer_v1.proto import datasource_pb2_grpc


class DataSourceServiceGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.bigquery.datatransfer.v1 DataSourceService API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """
    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = (
        'https://www.googleapis.com/auth/bigquery',
        'https://www.googleapis.com/auth/bigquery.readonly',
        'https://www.googleapis.com/auth/cloud-platform',
        'https://www.googleapis.com/auth/cloud-platform.read-only',
    )

    def __init__(self, channel=None, credentials=None,
                 address='bigquerydatatransfer.googleapis.com:443'):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                'The `channel` and `credentials` arguments are mutually '
                'exclusive.',
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    'grpc.max_send_message_length': -1,
                    'grpc.max_receive_message_length': -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            'data_source_service_stub': datasource_pb2_grpc.DataSourceServiceStub(channel),
        }


    @classmethod
    def create_channel(
                cls,
                address='bigquerydatatransfer.googleapis.com:443',
                credentials=None,
                **kwargs):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address,
            credentials=credentials,
            scopes=cls._OAUTH_SCOPES,
            **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def update_transfer_run(self):
        """Return the gRPC stub for :meth:`DataSourceServiceClient.update_transfer_run`.

        Update a transfer run. If successful, resets
        data\_source.update\_deadline\_seconds timer.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['data_source_service_stub'].UpdateTransferRun

    @property
    def log_transfer_run_messages(self):
        """Return the gRPC stub for :meth:`DataSourceServiceClient.log_transfer_run_messages`.

        Log messages for a transfer run. If successful (at least 1 message),
        resets data\_source.update\_deadline\_seconds timer.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['data_source_service_stub'].LogTransferRunMessages

    @property
    def start_big_query_jobs(self):
        """Return the gRPC stub for :meth:`DataSourceServiceClient.start_big_query_jobs`.

        Notify the Data Transfer Service that data is ready for loading.
        The Data Transfer Service will start and monitor multiple BigQuery Load
        jobs for a transfer run. Monitored jobs will be automatically retried
        and produce log messages when starting and finishing a job.
        Can be called multiple times for the same transfer run.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['data_source_service_stub'].StartBigQueryJobs

    @property
    def finish_run(self):
        """Return the gRPC stub for :meth:`DataSourceServiceClient.finish_run`.

        Notify the Data Transfer Service that the data source is done processing
        the run. No more status updates or requests to start/monitor jobs will be
        accepted. The run will be finalized by the Data Transfer Service when all
        monitored jobs are completed.
        Does not need to be called if the run is set to FAILED.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['data_source_service_stub'].FinishRun

    @property
    def create_data_source_definition(self):
        """Return the gRPC stub for :meth:`DataSourceServiceClient.create_data_source_definition`.

        Creates a data source definition. Calling this method will automatically
        use your credentials to create the following Google Cloud resources in
        YOUR Google Cloud project.

        1. OAuth client
        2. Pub/Sub Topics and Subscriptions in each supported\_location\_ids.
           e.g.,
           projects/{project\_id}/{topics\|subscriptions}/bigquerydatatransfer.{data\_source\_id}.{location\_id}.run
           The field data\_source.client\_id should be left empty in the input
           request, as the API will create a new OAuth client on behalf of the
           caller. On the other hand data\_source.scopes usually need to be set
           when there are OAuth scopes that need to be granted by end users.
        3. We need a longer deadline due to the 60 seconds SLO from Pub/Sub
           admin Operations. This also applies to update and delete data source
           definition.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['data_source_service_stub'].CreateDataSourceDefinition

    @property
    def update_data_source_definition(self):
        """Return the gRPC stub for :meth:`DataSourceServiceClient.update_data_source_definition`.

        Updates an existing data source definition. If changing
        supported\_location\_ids, triggers same effects as mentioned in "Create
        a data source definition."

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['data_source_service_stub'].UpdateDataSourceDefinition

    @property
    def delete_data_source_definition(self):
        """Return the gRPC stub for :meth:`DataSourceServiceClient.delete_data_source_definition`.

        Deletes a data source definition, all of the transfer configs associated
        with this data source definition (if any) must be deleted first by the user
        in ALL regions, in order to delete the data source definition.
        This method is primarily meant for deleting data sources created during
        testing stage.
        If the data source is referenced by transfer configs in the region
        specified in the request URL, the method will fail immediately. If in the
        current region (e.g., US) it's not used by any transfer configs, but in
        another region (e.g., EU) it is, then although the method will succeed in
        region US, but it will fail when the deletion operation is replicated to
        region EU. And eventually, the system will replicate the data source
        definition back from EU to US, in order to bring all regions to
        consistency. The final effect is that the data source appears to be
        'undeleted' in the US region.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['data_source_service_stub'].DeleteDataSourceDefinition

    @property
    def get_data_source_definition(self):
        """Return the gRPC stub for :meth:`DataSourceServiceClient.get_data_source_definition`.

        Retrieves an existing data source definition.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['data_source_service_stub'].GetDataSourceDefinition

    @property
    def list_data_source_definitions(self):
        """Return the gRPC stub for :meth:`DataSourceServiceClient.list_data_source_definitions`.

        Lists supported data source definitions.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['data_source_service_stub'].ListDataSourceDefinitions