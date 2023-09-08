# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import integer


class InputParallelism(AWSProperty):
    """
    `InputParallelism <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputparallelism.html>`__
    """

    props: PropsDictType = {
        "Count": (integer, False),
    }


class InputLambdaProcessor(AWSProperty):
    """
    `InputLambdaProcessor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html>`__
    """

    props: PropsDictType = {
        "ResourceARN": (str, True),
        "RoleARN": (str, True),
    }


class InputProcessingConfiguration(AWSProperty):
    """
    `InputProcessingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html>`__
    """

    props: PropsDictType = {
        "InputLambdaProcessor": (InputLambdaProcessor, False),
    }


class RecordColumn(AWSProperty):
    """
    `RecordColumn <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html>`__
    """

    props: PropsDictType = {
        "Mapping": (str, False),
        "Name": (str, True),
        "SqlType": (str, True),
    }


class CSVMappingParameters(AWSProperty):
    """
    `CSVMappingParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html>`__
    """

    props: PropsDictType = {
        "RecordColumnDelimiter": (str, True),
        "RecordRowDelimiter": (str, True),
    }


class JSONMappingParameters(AWSProperty):
    """
    `JSONMappingParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters.html>`__
    """

    props: PropsDictType = {
        "RecordRowPath": (str, True),
    }


class MappingParameters(AWSProperty):
    """
    `MappingParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html>`__
    """

    props: PropsDictType = {
        "CSVMappingParameters": (CSVMappingParameters, False),
        "JSONMappingParameters": (JSONMappingParameters, False),
    }


class RecordFormat(AWSProperty):
    """
    `RecordFormat <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html>`__
    """

    props: PropsDictType = {
        "MappingParameters": (MappingParameters, False),
        "RecordFormatType": (str, True),
    }


class InputSchema(AWSProperty):
    """
    `InputSchema <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html>`__
    """

    props: PropsDictType = {
        "RecordColumns": ([RecordColumn], True),
        "RecordEncoding": (str, False),
        "RecordFormat": (RecordFormat, True),
    }


class KinesisFirehoseInput(AWSProperty):
    """
    `KinesisFirehoseInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html>`__
    """

    props: PropsDictType = {
        "ResourceARN": (str, True),
        "RoleARN": (str, True),
    }


class KinesisStreamsInput(AWSProperty):
    """
    `KinesisStreamsInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html>`__
    """

    props: PropsDictType = {
        "ResourceARN": (str, True),
        "RoleARN": (str, True),
    }


class Input(AWSProperty):
    """
    `Input <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html>`__
    """

    props: PropsDictType = {
        "InputParallelism": (InputParallelism, False),
        "InputProcessingConfiguration": (InputProcessingConfiguration, False),
        "InputSchema": (InputSchema, True),
        "KinesisFirehoseInput": (KinesisFirehoseInput, False),
        "KinesisStreamsInput": (KinesisStreamsInput, False),
        "NamePrefix": (str, True),
    }


class Application(AWSObject):
    """
    `Application <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html>`__
    """

    resource_type = "AWS::KinesisAnalytics::Application"

    props: PropsDictType = {
        "ApplicationCode": (str, False),
        "ApplicationDescription": (str, False),
        "ApplicationName": (str, False),
        "Inputs": ([Input], True),
    }


class DestinationSchema(AWSProperty):
    """
    `DestinationSchema <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-destinationschema.html>`__
    """

    props: PropsDictType = {
        "RecordFormatType": (str, False),
    }


class KinesisFirehoseOutput(AWSProperty):
    """
    `KinesisFirehoseOutput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html>`__
    """

    props: PropsDictType = {
        "ResourceARN": (str, True),
        "RoleARN": (str, True),
    }


class KinesisStreamsOutput(AWSProperty):
    """
    `KinesisStreamsOutput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html>`__
    """

    props: PropsDictType = {
        "ResourceARN": (str, True),
        "RoleARN": (str, True),
    }


class LambdaOutput(AWSProperty):
    """
    `LambdaOutput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html>`__
    """

    props: PropsDictType = {
        "ResourceARN": (str, True),
        "RoleARN": (str, True),
    }


class Output(AWSProperty):
    """
    `Output <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html>`__
    """

    props: PropsDictType = {
        "DestinationSchema": (DestinationSchema, True),
        "KinesisFirehoseOutput": (KinesisFirehoseOutput, False),
        "KinesisStreamsOutput": (KinesisStreamsOutput, False),
        "LambdaOutput": (LambdaOutput, False),
        "Name": (str, False),
    }


class ApplicationOutput(AWSObject):
    """
    `ApplicationOutput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html>`__
    """

    resource_type = "AWS::KinesisAnalytics::ApplicationOutput"

    props: PropsDictType = {
        "ApplicationName": (str, True),
        "Output": (Output, True),
    }


class ReferenceSchema(AWSProperty):
    """
    `ReferenceSchema <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html>`__
    """

    props: PropsDictType = {
        "RecordColumns": ([RecordColumn], True),
        "RecordEncoding": (str, False),
        "RecordFormat": (RecordFormat, True),
    }


class S3ReferenceDataSource(AWSProperty):
    """
    `S3ReferenceDataSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html>`__
    """

    props: PropsDictType = {
        "BucketARN": (str, True),
        "FileKey": (str, True),
        "ReferenceRoleARN": (str, True),
    }


class ReferenceDataSource(AWSProperty):
    """
    `ReferenceDataSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html>`__
    """

    props: PropsDictType = {
        "ReferenceSchema": (ReferenceSchema, True),
        "S3ReferenceDataSource": (S3ReferenceDataSource, False),
        "TableName": (str, False),
    }


class ApplicationReferenceDataSource(AWSObject):
    """
    `ApplicationReferenceDataSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html>`__
    """

    resource_type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"

    props: PropsDictType = {
        "ApplicationName": (str, True),
        "ReferenceDataSource": (ReferenceDataSource, True),
    }
