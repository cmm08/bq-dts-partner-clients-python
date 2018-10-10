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
"""Wrappers for protocol buffer enum types."""

import enum


class NullValue(enum.IntEnum):
    """
    ``NullValue`` is a singleton enumeration to represent the null value for the
    ``Value`` type union.

     The JSON representation for ``NullValue`` is JSON ``null``.

    Attributes:
      NULL_VALUE (int): Null value.
    """
    NULL_VALUE = 0


class TransferType(enum.IntEnum):
    """
    DEPRECATED. Represents data transfer type.

    Attributes:
      TRANSFER_TYPE_UNSPECIFIED (int): Invalid or Unknown transfer type placeholder.
      BATCH (int): Batch data transfer.
      STREAMING (int): Streaming data transfer. Streaming data source currently doesn't
      support multiple transfer configs per project.
    """
    TRANSFER_TYPE_UNSPECIFIED = 0
    BATCH = 1
    STREAMING = 2


class TransferState(enum.IntEnum):
    """
    Represents data transfer run state.

    Attributes:
      TRANSFER_STATE_UNSPECIFIED (int): State placeholder.
      PENDING (int): Data transfer is scheduled and is waiting to be picked up by
      data transfer backend.
      RUNNING (int): Data transfer is in progress.
      SUCCEEDED (int): Data transfer completed successsfully.
      FAILED (int): Data transfer failed.
      CANCELLED (int): Data transfer is cancelled.
    """
    TRANSFER_STATE_UNSPECIFIED = 0
    PENDING = 2
    RUNNING = 3
    SUCCEEDED = 4
    FAILED = 5
    CANCELLED = 6


class WriteDisposition(enum.IntEnum):
    """
    Options for writing to the table.
    The WRITE_EMPTY option is intentionally excluded from the enum and is not
    supported by the data transfer service.

    Attributes:
      WRITE_DISPOSITION_UNSPECIFIED (int): The defult writeDispostion
      WRITE_TRUNCATE (int): overwrites the table data.
      WRITE_APPEND (int): the data is appended to the table.
      Note duplication might happen if this mode is used.
    """
    WRITE_DISPOSITION_UNSPECIFIED = 0
    WRITE_TRUNCATE = 1
    WRITE_APPEND = 2


class TransferMessage(object):
    class MessageSeverity(enum.IntEnum):
        """
        Represents data transfer user facing message severity.

        Attributes:
          MESSAGE_SEVERITY_UNSPECIFIED (int): No severity specified.
          INFO (int): Informational message.
          WARNING (int): Warning message.
          ERROR (int): Error message.
          DEBUG (int): Debug message.
        """
        MESSAGE_SEVERITY_UNSPECIFIED = 0
        INFO = 1
        WARNING = 2
        ERROR = 3
        DEBUG = 4


class DataSourceParameter(object):
    class Type(enum.IntEnum):
        """
        Parameter type.

        Attributes:
          TYPE_UNSPECIFIED (int): Type unspecified.
          STRING (int): String parameter.
          INTEGER (int): Integer parameter (64-bits).
          Will be serialized to json as string.
          DOUBLE (int): Double precision floating point parameter.
          BOOLEAN (int): Boolean parameter.
          RECORD (int): Deprecated. This field has no effect.
          PLUS_PAGE (int): Page ID for a Google+ Page.
        """
        TYPE_UNSPECIFIED = 0
        STRING = 1
        INTEGER = 2
        DOUBLE = 3
        BOOLEAN = 4
        RECORD = 5
        PLUS_PAGE = 6


class DataSource(object):
    class AuthorizationType(enum.IntEnum):
        """
        The type of authorization needed for this data source.

        Attributes:
          AUTHORIZATION_TYPE_UNSPECIFIED (int): Type unspecified.
          AUTHORIZATION_CODE (int): Use OAuth 2 authorization codes that can be exchanged
          for a refresh token on the backend.
          GOOGLE_PLUS_AUTHORIZATION_CODE (int): Return an authorization code for a given Google+ page that can then be
          exchanged for a refresh token on the backend.
        """
        AUTHORIZATION_TYPE_UNSPECIFIED = 0
        AUTHORIZATION_CODE = 1
        GOOGLE_PLUS_AUTHORIZATION_CODE = 2

    class DataRefreshType(enum.IntEnum):
        """
        Represents how the data source supports data auto refresh.

        Attributes:
          DATA_REFRESH_TYPE_UNSPECIFIED (int): The data source won't support data auto refresh, which is default value.
          SLIDING_WINDOW (int): The data source supports data auto refresh, and runs will be scheduled
          for the past few days. Does not allow custom values to be set for each
          transfer config.
          CUSTOM_SLIDING_WINDOW (int): The data source supports data auto refresh, and runs will be scheduled
          for the past few days. Allows custom values to be set for each transfer
          config.
        """
        DATA_REFRESH_TYPE_UNSPECIFIED = 0
        SLIDING_WINDOW = 1
        CUSTOM_SLIDING_WINDOW = 2


class ListTransferRunsRequest(object):
    class RunAttempt(enum.IntEnum):
        """
        Represents which runs should be pulled.

        Attributes:
          RUN_ATTEMPT_UNSPECIFIED (int): All runs should be returned.
          LATEST (int): Only latest run per day should be returned.
        """
        RUN_ATTEMPT_UNSPECIFIED = 0
        LATEST = 1


class ImportedDataInfo(object):
    class Format(enum.IntEnum):
        """
        Data format.

        Attributes:
          FORMAT_UNSPECIFIED (int): Unspecified format. In this case, we have to infer the format from the
          data source.
          CSV (int): CSV format.
          JSON (int): Newline-delimited JSON.
          AVRO (int): Avro format. See http://avro.apache.org .
          RECORDIO (int): RecordIO.
          COLUMNIO (int): ColumnIO.
          CAPACITOR (int): Capacitor.
          PARQUET (int): Parquet format. See https://parquet.apache.org .
          ORC (int): ORC format. See https://orc.apache.org .
        """
        FORMAT_UNSPECIFIED = 0
        CSV = 1
        JSON = 2
        AVRO = 3
        RECORDIO = 4
        COLUMNIO = 5
        CAPACITOR = 6
        PARQUET = 7
        ORC = 8

    class Encoding(enum.IntEnum):
        """
        Encoding of input data in CSV/JSON format.

        Attributes:
          ENCODING_UNSPECIFIED (int): Default encoding (UTF8).
          ISO_8859_1 (int): ISO_8859_1 encoding.
          UTF8 (int): UTF8 encoding.
        """
        ENCODING_UNSPECIFIED = 0
        ISO_8859_1 = 1
        UTF8 = 2

    class FieldSchema(object):
        class Type(enum.IntEnum):
            """
            LINT.IfChange
            Field type.

            Attributes:
              TYPE_UNSPECIFIED (int): Illegal value.
              STRING (int): 64K, UTF8.
              INTEGER (int): 64-bit signed.
              FLOAT (int): 64-bit IEEE floating point.
              RECORD (int): Aggregate type.
              BYTES (int): 64K, Binary.
              BOOLEAN (int): 2-valued.
              TIMESTAMP (int): 64-bit signed usec since UTC epoch.
              DATE (int): Civil date - Year, Month, Day.
              TIME (int): Civil time - Hour, Minute, Second, Microseconds.
              DATETIME (int): Combination of civil date and civil time.
              NUMERIC (int): Numeric type with 38 decimal digits of precision and 9 decimal digits
              of scale.
              GEOGRAPHY (int): Geography object (go/googlesql_geography).
            """
            TYPE_UNSPECIFIED = 0
            STRING = 1
            INTEGER = 2
            FLOAT = 3
            RECORD = 4
            BYTES = 5
            BOOLEAN = 6
            TIMESTAMP = 7
            DATE = 8
            TIME = 9
            DATETIME = 10
            NUMERIC = 11
            GEOGRAPHY = 12
