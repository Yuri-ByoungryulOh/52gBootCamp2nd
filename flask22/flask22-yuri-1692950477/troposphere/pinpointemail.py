# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean


class DeliveryOptions(AWSProperty):
    """
    `DeliveryOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-deliveryoptions.html>`__
    """

    props: PropsDictType = {
        "SendingPoolName": (str, False),
    }


class ReputationOptions(AWSProperty):
    """
    `ReputationOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-reputationoptions.html>`__
    """

    props: PropsDictType = {
        "ReputationMetricsEnabled": (boolean, False),
    }


class SendingOptions(AWSProperty):
    """
    `SendingOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-sendingoptions.html>`__
    """

    props: PropsDictType = {
        "SendingEnabled": (boolean, False),
    }


class TrackingOptions(AWSProperty):
    """
    `TrackingOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-trackingoptions.html>`__
    """

    props: PropsDictType = {
        "CustomRedirectDomain": (str, False),
    }


class ConfigurationSet(AWSObject):
    """
    `ConfigurationSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html>`__
    """

    resource_type = "AWS::PinpointEmail::ConfigurationSet"

    props: PropsDictType = {
        "DeliveryOptions": (DeliveryOptions, False),
        "Name": (str, True),
        "ReputationOptions": (ReputationOptions, False),
        "SendingOptions": (SendingOptions, False),
        "Tags": (Tags, False),
        "TrackingOptions": (TrackingOptions, False),
    }


class DimensionConfiguration(AWSProperty):
    """
    `DimensionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html>`__
    """

    props: PropsDictType = {
        "DefaultDimensionValue": (str, True),
        "DimensionName": (str, True),
        "DimensionValueSource": (str, True),
    }


class CloudWatchDestination(AWSProperty):
    """
    `CloudWatchDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination.html>`__
    """

    props: PropsDictType = {
        "DimensionConfigurations": ([DimensionConfiguration], False),
    }


class KinesisFirehoseDestination(AWSProperty):
    """
    `KinesisFirehoseDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html>`__
    """

    props: PropsDictType = {
        "DeliveryStreamArn": (str, True),
        "IamRoleArn": (str, True),
    }


class PinpointDestination(AWSProperty):
    """
    `PinpointDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination.html>`__
    """

    props: PropsDictType = {
        "ApplicationArn": (str, False),
    }


class SnsDestination(AWSProperty):
    """
    `SnsDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-snsdestination.html>`__
    """

    props: PropsDictType = {
        "TopicArn": (str, True),
    }


class EventDestination(AWSProperty):
    """
    `EventDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html>`__
    """

    props: PropsDictType = {
        "CloudWatchDestination": (CloudWatchDestination, False),
        "Enabled": (boolean, False),
        "KinesisFirehoseDestination": (KinesisFirehoseDestination, False),
        "MatchingEventTypes": ([str], True),
        "PinpointDestination": (PinpointDestination, False),
        "SnsDestination": (SnsDestination, False),
    }


class ConfigurationSetEventDestination(AWSObject):
    """
    `ConfigurationSetEventDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html>`__
    """

    resource_type = "AWS::PinpointEmail::ConfigurationSetEventDestination"

    props: PropsDictType = {
        "ConfigurationSetName": (str, True),
        "EventDestination": (EventDestination, False),
        "EventDestinationName": (str, True),
    }


class DedicatedIpPool(AWSObject):
    """
    `DedicatedIpPool <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html>`__
    """

    resource_type = "AWS::PinpointEmail::DedicatedIpPool"

    props: PropsDictType = {
        "PoolName": (str, False),
        "Tags": (Tags, False),
    }


class MailFromAttributes(AWSProperty):
    """
    `MailFromAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html>`__
    """

    props: PropsDictType = {
        "BehaviorOnMxFailure": (str, False),
        "MailFromDomain": (str, False),
    }


class Identity(AWSObject):
    """
    `Identity <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html>`__
    """

    resource_type = "AWS::PinpointEmail::Identity"

    props: PropsDictType = {
        "DkimSigningEnabled": (boolean, False),
        "FeedbackForwardingEnabled": (boolean, False),
        "MailFromAttributes": (MailFromAttributes, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }