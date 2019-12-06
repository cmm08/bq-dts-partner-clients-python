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

"""Accesses the google.cloud.bigquery.datatransfer.v1 DataSourceService API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.cloud.bigquery.datatransfer_v1.gapic import data_source_service_client_config
from google.cloud.bigquery.datatransfer_v1.gapic import enums
from google.cloud.bigquery.datatransfer_v1.gapic.transports import data_source_service_grpc_transport
from google.cloud.bigquery.datatransfer_v1.proto import datasource_pb2
from google.cloud.bigquery.datatransfer_v1.proto import datasource_pb2_grpc
from google.cloud.bigquery.datatransfer_v1.proto import transfer_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2



_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    'google-cloud-bigquerydatatransfer',
).version


class DataSourceServiceClient(object):
    """
    The Google BigQuery Data Transfer API allows BigQuery users to
    configure transfer of their data from other Google Products into BigQuery.
    This service exposes methods that should be used by data source backend.
    """

    SERVICE_ADDRESS = 'bigquerydatatransfer.googleapis.com:443'
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = 'google.cloud.bigquery.datatransfer.v1.DataSourceService'


    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DataSourceServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(
            filename)
        kwargs['credentials'] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file


    @classmethod
    def data_source_definition_path(cls, project, location, data_source_definition):
        """Return a fully-qualified data_source_definition string."""
        return google.api_core.path_template.expand(
            'projects/{project}/locations/{location}/dataSourceDefinitions/{data_source_definition}',
            project=project,
            location=location,
            data_source_definition=data_source_definition,
        )

    @classmethod
    def location_path(cls, project, location):
        """Return a fully-qualified location string."""
        return google.api_core.path_template.expand(
            'projects/{project}/locations/{location}',
            project=project,
            location=location,
        )

    @classmethod
    def run_path(cls, project, location, transfer_config, run):
        """Return a fully-qualified run string."""
        return google.api_core.path_template.expand(
            'projects/{project}/locations/{location}/transferConfigs/{transfer_config}/runs/{run}',
            project=project,
            location=location,
            transfer_config=transfer_config,
            run=run,
        )

    def __init__(self, transport=None, channel=None, credentials=None,
            client_config=None, client_info=None, client_options=None):
        """Constructor.

        Args:
            transport (Union[~.DataSourceServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.DataSourceServiceGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn('The `client_config` argument is deprecated.',
                          PendingDeprecationWarning, stacklevel=2)
        else:
            client_config = data_source_service_client_config.config

        if channel:
            warnings.warn('The `channel` argument is deprecated; use '
                          '`transport` instead.',
                          PendingDeprecationWarning, stacklevel=2)

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(client_options)
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=data_source_service_grpc_transport.DataSourceServiceGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        'Received both a transport instance and '
                        'credentials; these are mutually exclusive.'
                    )
                self.transport = transport
        else:
            self.transport = data_source_service_grpc_transport.DataSourceServiceGrpcTransport(
                address=api_endpoint,
                channel=channel,
                credentials=credentials,
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION,
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config['interfaces'][self._INTERFACE_NAME],
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def update_transfer_run(
            self,
            transfer_run,
            update_mask,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Update a transfer run. If successful, resets
        data\_source.update\_deadline\_seconds timer.

        Example:
            >>> from google.cloud.bigquery import datatransfer_v1
            >>>
            >>> client = datatransfer_v1.DataSourceServiceClient()
            >>>
            >>> # TODO: Initialize `transfer_run`:
            >>> transfer_run = {}
            >>>
            >>> # TODO: Initialize `update_mask`:
            >>> update_mask = {}
            >>>
            >>> response = client.update_transfer_run(transfer_run, update_mask)

        Args:
            transfer_run (Union[dict, ~google.cloud.bigquery.datatransfer_v1.types.TransferRun]): Run name must be set and correspond to an already existing run. Only
                state, error\_status, and data\_version fields will be updated. All
                other fields will be ignored.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery.datatransfer_v1.types.TransferRun`
            update_mask (Union[dict, ~google.cloud.bigquery.datatransfer_v1.types.FieldMask]): Required list of fields to be updated in this request.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery.datatransfer_v1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery.datatransfer_v1.types.TransferRun` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_transfer_run' not in self._inner_api_calls:
            self._inner_api_calls['update_transfer_run'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_transfer_run,
                default_retry=self._method_configs['UpdateTransferRun'].retry,
                default_timeout=self._method_configs['UpdateTransferRun'].timeout,
                client_info=self._client_info,
            )

        request = datasource_pb2.UpdateTransferRunRequest(
            transfer_run=transfer_run,
            update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('transfer_run.name', transfer_run.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_transfer_run'](request, retry=retry, timeout=timeout, metadata=metadata)

    def log_transfer_run_messages(
            self,
            name,
            transfer_messages,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Log messages for a transfer run. If successful (at least 1 message),
        resets data\_source.update\_deadline\_seconds timer.

        Example:
            >>> from google.cloud.bigquery import datatransfer_v1
            >>>
            >>> client = datatransfer_v1.DataSourceServiceClient()
            >>>
            >>> name = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')
            >>>
            >>> # TODO: Initialize `transfer_messages`:
            >>> transfer_messages = []
            >>>
            >>> client.log_transfer_run_messages(name, transfer_messages)

        Args:
            name (str): Name of the resource in the form:
                "projects/{project\_id}/locations/{location\_id}/transferConfigs/{config\_id}/runs/{run\_id}"
            transfer_messages (list[Union[dict, ~google.cloud.bigquery.datatransfer_v1.types.TransferMessage]]): Messages to append.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery.datatransfer_v1.types.TransferMessage`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'log_transfer_run_messages' not in self._inner_api_calls:
            self._inner_api_calls['log_transfer_run_messages'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.log_transfer_run_messages,
                default_retry=self._method_configs['LogTransferRunMessages'].retry,
                default_timeout=self._method_configs['LogTransferRunMessages'].timeout,
                client_info=self._client_info,
            )

        request = datasource_pb2.LogTransferRunMessagesRequest(
            name=name,
            transfer_messages=transfer_messages,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['log_transfer_run_messages'](request, retry=retry, timeout=timeout, metadata=metadata)

    def start_big_query_jobs(
            self,
            name,
            imported_data,
            user_credentials=None,
            max_parallelism=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Notify the Data Transfer Service that data is ready for loading.
        The Data Transfer Service will start and monitor multiple BigQuery Load
        jobs for a transfer run. Monitored jobs will be automatically retried
        and produce log messages when starting and finishing a job.
        Can be called multiple times for the same transfer run.

        Example:
            >>> from google.cloud.bigquery import datatransfer_v1
            >>>
            >>> client = datatransfer_v1.DataSourceServiceClient()
            >>>
            >>> name = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')
            >>>
            >>> # TODO: Initialize `imported_data`:
            >>> imported_data = []
            >>>
            >>> client.start_big_query_jobs(name, imported_data)

        Args:
            name (str): Name of the resource in the form:
                "projects/{project\_id}/locations/{location\_id}/transferConfigs/{config\_id}/runs/{run\_id}"
            imported_data (list[Union[dict, ~google.cloud.bigquery.datatransfer_v1.types.ImportedDataInfo]]): Import jobs which should be started and monitored.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery.datatransfer_v1.types.ImportedDataInfo`
            user_credentials (bytes): User credentials which should be used to start/monitor
                BigQuery jobs. If not specified, then jobs
                are started using data source service account credentials.
                This may be OAuth token or JWT token.
            max_parallelism (int): The number of BQ Jobs that can run in parallel.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'start_big_query_jobs' not in self._inner_api_calls:
            self._inner_api_calls['start_big_query_jobs'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.start_big_query_jobs,
                default_retry=self._method_configs['StartBigQueryJobs'].retry,
                default_timeout=self._method_configs['StartBigQueryJobs'].timeout,
                client_info=self._client_info,
            )

        request = datasource_pb2.StartBigQueryJobsRequest(
            name=name,
            imported_data=imported_data,
            user_credentials=user_credentials,
            max_parallelism=max_parallelism,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['start_big_query_jobs'](request, retry=retry, timeout=timeout, metadata=metadata)

    def finish_run(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Notify the Data Transfer Service that the data source is done processing
        the run. No more status updates or requests to start/monitor jobs will be
        accepted. The run will be finalized by the Data Transfer Service when all
        monitored jobs are completed.
        Does not need to be called if the run is set to FAILED.

        Example:
            >>> from google.cloud.bigquery import datatransfer_v1
            >>>
            >>> client = datatransfer_v1.DataSourceServiceClient()
            >>>
            >>> name = client.run_path('[PROJECT]', '[LOCATION]', '[TRANSFER_CONFIG]', '[RUN]')
            >>>
            >>> client.finish_run(name)

        Args:
            name (str): Name of the resource in the form:
                "projects/{project\_id}/locations/{location\_id}/transferConfigs/{config\_id}/runs/{run\_id}"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'finish_run' not in self._inner_api_calls:
            self._inner_api_calls['finish_run'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.finish_run,
                default_retry=self._method_configs['FinishRun'].retry,
                default_timeout=self._method_configs['FinishRun'].timeout,
                client_info=self._client_info,
            )

        request = datasource_pb2.FinishRunRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['finish_run'](request, retry=retry, timeout=timeout, metadata=metadata)

    def create_data_source_definition(
            self,
            parent,
            data_source_definition,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
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

        Example:
            >>> from google.cloud.bigquery import datatransfer_v1
            >>>
            >>> client = datatransfer_v1.DataSourceServiceClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # TODO: Initialize `data_source_definition`:
            >>> data_source_definition = {}
            >>>
            >>> response = client.create_data_source_definition(parent, data_source_definition)

        Args:
            parent (str): The BigQuery project id for which data source definition is associated.
                Must be in the form: ``projects/{project_id}/locations/{location_id}``
            data_source_definition (Union[dict, ~google.cloud.bigquery.datatransfer_v1.types.DataSourceDefinition]): Data source definition.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery.datatransfer_v1.types.DataSourceDefinition`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery.datatransfer_v1.types.DataSourceDefinition` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_data_source_definition' not in self._inner_api_calls:
            self._inner_api_calls['create_data_source_definition'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_data_source_definition,
                default_retry=self._method_configs['CreateDataSourceDefinition'].retry,
                default_timeout=self._method_configs['CreateDataSourceDefinition'].timeout,
                client_info=self._client_info,
            )

        request = datasource_pb2.CreateDataSourceDefinitionRequest(
            parent=parent,
            data_source_definition=data_source_definition,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['create_data_source_definition'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_data_source_definition(
            self,
            data_source_definition,
            update_mask,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Updates an existing data source definition. If changing
        supported\_location\_ids, triggers same effects as mentioned in "Create
        a data source definition."

        Example:
            >>> from google.cloud.bigquery import datatransfer_v1
            >>>
            >>> client = datatransfer_v1.DataSourceServiceClient()
            >>>
            >>> # TODO: Initialize `data_source_definition`:
            >>> data_source_definition = {}
            >>>
            >>> # TODO: Initialize `update_mask`:
            >>> update_mask = {}
            >>>
            >>> response = client.update_data_source_definition(data_source_definition, update_mask)

        Args:
            data_source_definition (Union[dict, ~google.cloud.bigquery.datatransfer_v1.types.DataSourceDefinition]): Data source definition.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery.datatransfer_v1.types.DataSourceDefinition`
            update_mask (Union[dict, ~google.cloud.bigquery.datatransfer_v1.types.FieldMask]): Update field mask.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery.datatransfer_v1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery.datatransfer_v1.types.DataSourceDefinition` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_data_source_definition' not in self._inner_api_calls:
            self._inner_api_calls['update_data_source_definition'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_data_source_definition,
                default_retry=self._method_configs['UpdateDataSourceDefinition'].retry,
                default_timeout=self._method_configs['UpdateDataSourceDefinition'].timeout,
                client_info=self._client_info,
            )

        request = datasource_pb2.UpdateDataSourceDefinitionRequest(
            data_source_definition=data_source_definition,
            update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('data_source_definition.name', data_source_definition.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_data_source_definition'](request, retry=retry, timeout=timeout, metadata=metadata)

    def delete_data_source_definition(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
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

        Example:
            >>> from google.cloud.bigquery import datatransfer_v1
            >>>
            >>> client = datatransfer_v1.DataSourceServiceClient()
            >>>
            >>> name = client.data_source_definition_path('[PROJECT]', '[LOCATION]', '[DATA_SOURCE_DEFINITION]')
            >>>
            >>> client.delete_data_source_definition(name)

        Args:
            name (str): The field will contain name of the resource requested, for example:
                ``projects/{project_id}/locations/{location_id}/dataSourceDefinitions/{data_source_id}``
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'delete_data_source_definition' not in self._inner_api_calls:
            self._inner_api_calls['delete_data_source_definition'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_data_source_definition,
                default_retry=self._method_configs['DeleteDataSourceDefinition'].retry,
                default_timeout=self._method_configs['DeleteDataSourceDefinition'].timeout,
                client_info=self._client_info,
            )

        request = datasource_pb2.DeleteDataSourceDefinitionRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['delete_data_source_definition'](request, retry=retry, timeout=timeout, metadata=metadata)

    def get_data_source_definition(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves an existing data source definition.

        Example:
            >>> from google.cloud.bigquery import datatransfer_v1
            >>>
            >>> client = datatransfer_v1.DataSourceServiceClient()
            >>>
            >>> name = client.data_source_definition_path('[PROJECT]', '[LOCATION]', '[DATA_SOURCE_DEFINITION]')
            >>>
            >>> response = client.get_data_source_definition(name)

        Args:
            name (str): The field will contain name of the resource requested.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery.datatransfer_v1.types.DataSourceDefinition` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_data_source_definition' not in self._inner_api_calls:
            self._inner_api_calls['get_data_source_definition'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_data_source_definition,
                default_retry=self._method_configs['GetDataSourceDefinition'].retry,
                default_timeout=self._method_configs['GetDataSourceDefinition'].timeout,
                client_info=self._client_info,
            )

        request = datasource_pb2.GetDataSourceDefinitionRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_data_source_definition'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_data_source_definitions(
            self,
            parent,
            page_size=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Lists supported data source definitions.

        Example:
            >>> from google.cloud.bigquery import datatransfer_v1
            >>>
            >>> client = datatransfer_v1.DataSourceServiceClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_data_source_definitions(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_data_source_definitions(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): The BigQuery project id for which data sources should be returned. Must
                be in the form: ``projects/{project_id}/locations/{location_id}``
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.bigquery.datatransfer_v1.types.DataSourceDefinition` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_data_source_definitions' not in self._inner_api_calls:
            self._inner_api_calls['list_data_source_definitions'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_data_source_definitions,
                default_retry=self._method_configs['ListDataSourceDefinitions'].retry,
                default_timeout=self._method_configs['ListDataSourceDefinitions'].timeout,
                client_info=self._client_info,
            )

        request = datasource_pb2.ListDataSourceDefinitionsRequest(
            parent=parent,
            page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(self._inner_api_calls['list_data_source_definitions'], retry=retry, timeout=timeout, metadata=metadata),
            request=request,
            items_field='data_source_definitions',
            request_token_field='page_token',
            response_token_field='next_page_token',
        )
        return iterator
