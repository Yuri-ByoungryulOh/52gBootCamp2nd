# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import integer


class ExperimentTemplateAction(AWSProperty):
    """
    `ExperimentTemplateAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html>`__
    """

    props: PropsDictType = {
        "ActionId": (str, True),
        "Description": (str, False),
        "Parameters": (dict, False),
        "StartAfter": ([str], False),
        "Targets": (dict, False),
    }


class CloudWatchLogsConfiguration(AWSProperty):
    """
    `CloudWatchLogsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-cloudwatchlogsconfiguration.html>`__
    """

    props: PropsDictType = {
        "LogGroupArn": (str, True),
    }


class S3Configuration(AWSProperty):
    """
    `S3Configuration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-s3configuration.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, True),
        "Prefix": (str, False),
    }


class ExperimentTemplateLogConfiguration(AWSProperty):
    """
    `ExperimentTemplateLogConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatelogconfiguration.html>`__
    """

    props: PropsDictType = {
        "CloudWatchLogsConfiguration": (CloudWatchLogsConfiguration, False),
        "LogSchemaVersion": (integer, True),
        "S3Configuration": (S3Configuration, False),
    }


class ExperimentTemplateStopCondition(AWSProperty):
    """
    `ExperimentTemplateStopCondition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html>`__
    """

    props: PropsDictType = {
        "Source": (str, True),
        "Value": (str, False),
    }


class ExperimentTemplateTargetFilter(AWSProperty):
    """
    `ExperimentTemplateTargetFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html>`__
    """

    props: PropsDictType = {
        "Path": (str, True),
        "Values": ([str], True),
    }


class ExperimentTemplateTarget(AWSProperty):
    """
    `ExperimentTemplateTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html>`__
    """

    props: PropsDictType = {
        "Filters": ([ExperimentTemplateTargetFilter], False),
        "Parameters": (dict, False),
        "ResourceArns": ([str], False),
        "ResourceTags": (dict, False),
        "ResourceType": (str, True),
        "SelectionMode": (str, True),
    }


class ExperimentTemplate(AWSObject):
    """
    `ExperimentTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html>`__
    """

    resource_type = "AWS::FIS::ExperimentTemplate"

    props: PropsDictType = {
        "Actions": (dict, False),
        "Description": (str, True),
        "LogConfiguration": (ExperimentTemplateLogConfiguration, False),
        "RoleArn": (str, True),
        "StopConditions": ([ExperimentTemplateStopCondition], True),
        "Tags": (dict, True),
        "Targets": (dict, True),
    }