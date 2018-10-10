# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.bigquery.datatransfer_v1.proto import datatransfer_pb2 as google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2
from google.cloud.bigquery.datatransfer_v1.proto import transfer_pb2 as google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_transfer__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DataTransferServiceStub(object):
  """The Google BigQuery Data Transfer Service API enables BigQuery users to
  configure the transfer of their data from other Google Products into BigQuery.
  This service contains methods that are end user exposed. It backs up the
  frontend.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetDataSource = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/GetDataSource',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.GetDataSourceRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.DataSource.FromString,
        )
    self.ListDataSources = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/ListDataSources',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListDataSourcesRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListDataSourcesResponse.FromString,
        )
    self.CreateTransferConfig = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/CreateTransferConfig',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.CreateTransferConfigRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_transfer__pb2.TransferConfig.FromString,
        )
    self.UpdateTransferConfig = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/UpdateTransferConfig',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.UpdateTransferConfigRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_transfer__pb2.TransferConfig.FromString,
        )
    self.DeleteTransferConfig = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/DeleteTransferConfig',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.DeleteTransferConfigRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetTransferConfig = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/GetTransferConfig',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.GetTransferConfigRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_transfer__pb2.TransferConfig.FromString,
        )
    self.ListTransferConfigs = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/ListTransferConfigs',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListTransferConfigsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListTransferConfigsResponse.FromString,
        )
    self.ScheduleTransferRuns = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/ScheduleTransferRuns',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ScheduleTransferRunsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ScheduleTransferRunsResponse.FromString,
        )
    self.GetTransferRun = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/GetTransferRun',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.GetTransferRunRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_transfer__pb2.TransferRun.FromString,
        )
    self.DeleteTransferRun = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/DeleteTransferRun',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.DeleteTransferRunRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListTransferRuns = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/ListTransferRuns',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListTransferRunsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListTransferRunsResponse.FromString,
        )
    self.ListTransferLogs = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/ListTransferLogs',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListTransferLogsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListTransferLogsResponse.FromString,
        )
    self.CheckValidCreds = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/CheckValidCreds',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.CheckValidCredsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.CheckValidCredsResponse.FromString,
        )
    self.EnableDataTransferService = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/EnableDataTransferService',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.EnableDataTransferServiceRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.IsDataTransferServiceEnabled = channel.unary_unary(
        '/google.cloud.bigquery.datatransfer.v1.DataTransferService/IsDataTransferServiceEnabled',
        request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.IsDataTransferServiceEnabledRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.IsDataTransferServiceEnabledResponse.FromString,
        )


class DataTransferServiceServicer(object):
  """The Google BigQuery Data Transfer Service API enables BigQuery users to
  configure the transfer of their data from other Google Products into BigQuery.
  This service contains methods that are end user exposed. It backs up the
  frontend.
  """

  def GetDataSource(self, request, context):
    """Retrieves a supported data source and returns its settings,
    which can be used for UI rendering.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListDataSources(self, request, context):
    """Lists supported data sources and returns their settings,
    which can be used for UI rendering.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateTransferConfig(self, request, context):
    """Creates a new data transfer configuration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateTransferConfig(self, request, context):
    """Updates a data transfer configuration.
    All fields must be set, even if they are not updated.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteTransferConfig(self, request, context):
    """Deletes a data transfer configuration,
    including any associated transfer runs and logs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTransferConfig(self, request, context):
    """Returns information about a data transfer config.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTransferConfigs(self, request, context):
    """Returns information about all data transfers in the project.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ScheduleTransferRuns(self, request, context):
    """Creates transfer runs for a time range [start_time, end_time].
    For each date - or whatever granularity the data source supports - in the
    range, one transfer run is created.
    Note that runs are created per UTC time in the time range.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTransferRun(self, request, context):
    """Returns information about the particular transfer run.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteTransferRun(self, request, context):
    """Deletes the specified transfer run.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTransferRuns(self, request, context):
    """Returns information about running and completed jobs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTransferLogs(self, request, context):
    """Returns user facing log messages for the data transfer run.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckValidCreds(self, request, context):
    """Returns true if valid credentials exist for the given data source and
    requesting user.
    Some data sources doesn't support service account, so we need to talk to
    them on behalf of the end user. This API just checks whether we have OAuth
    token for the particular user, which is a pre-requisite before user can
    create a transfer config.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EnableDataTransferService(self, request, context):
    """Enables data transfer service for a given project. This
    method requires the additional scope of
    'https://www.googleapis.com/auth/cloudplatformprojects'
    to manage the cloud project permissions.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IsDataTransferServiceEnabled(self, request, context):
    """Returns true if data transfer is enabled for a project.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DataTransferServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetDataSource': grpc.unary_unary_rpc_method_handler(
          servicer.GetDataSource,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.GetDataSourceRequest.FromString,
          response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.DataSource.SerializeToString,
      ),
      'ListDataSources': grpc.unary_unary_rpc_method_handler(
          servicer.ListDataSources,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListDataSourcesRequest.FromString,
          response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListDataSourcesResponse.SerializeToString,
      ),
      'CreateTransferConfig': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTransferConfig,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.CreateTransferConfigRequest.FromString,
          response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_transfer__pb2.TransferConfig.SerializeToString,
      ),
      'UpdateTransferConfig': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateTransferConfig,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.UpdateTransferConfigRequest.FromString,
          response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_transfer__pb2.TransferConfig.SerializeToString,
      ),
      'DeleteTransferConfig': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteTransferConfig,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.DeleteTransferConfigRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetTransferConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetTransferConfig,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.GetTransferConfigRequest.FromString,
          response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_transfer__pb2.TransferConfig.SerializeToString,
      ),
      'ListTransferConfigs': grpc.unary_unary_rpc_method_handler(
          servicer.ListTransferConfigs,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListTransferConfigsRequest.FromString,
          response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListTransferConfigsResponse.SerializeToString,
      ),
      'ScheduleTransferRuns': grpc.unary_unary_rpc_method_handler(
          servicer.ScheduleTransferRuns,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ScheduleTransferRunsRequest.FromString,
          response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ScheduleTransferRunsResponse.SerializeToString,
      ),
      'GetTransferRun': grpc.unary_unary_rpc_method_handler(
          servicer.GetTransferRun,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.GetTransferRunRequest.FromString,
          response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_transfer__pb2.TransferRun.SerializeToString,
      ),
      'DeleteTransferRun': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteTransferRun,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.DeleteTransferRunRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListTransferRuns': grpc.unary_unary_rpc_method_handler(
          servicer.ListTransferRuns,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListTransferRunsRequest.FromString,
          response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListTransferRunsResponse.SerializeToString,
      ),
      'ListTransferLogs': grpc.unary_unary_rpc_method_handler(
          servicer.ListTransferLogs,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListTransferLogsRequest.FromString,
          response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.ListTransferLogsResponse.SerializeToString,
      ),
      'CheckValidCreds': grpc.unary_unary_rpc_method_handler(
          servicer.CheckValidCreds,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.CheckValidCredsRequest.FromString,
          response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.CheckValidCredsResponse.SerializeToString,
      ),
      'EnableDataTransferService': grpc.unary_unary_rpc_method_handler(
          servicer.EnableDataTransferService,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.EnableDataTransferServiceRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'IsDataTransferServiceEnabled': grpc.unary_unary_rpc_method_handler(
          servicer.IsDataTransferServiceEnabled,
          request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.IsDataTransferServiceEnabledRequest.FromString,
          response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datatransfer__pb2.IsDataTransferServiceEnabledResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.cloud.bigquery.datatransfer.v1.DataTransferService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
