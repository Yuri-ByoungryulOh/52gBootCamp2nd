# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.route53 import AliasTarget  # noqa: F401


class Location(AWSProperty):
    """
    `Location <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrcollection-location.html>`__
    """

    props: PropsDictType = {
        "CidrList": ([str], True),
        "LocationName": (str, True),
    }


class CidrCollection(AWSObject):
    """
    `CidrCollection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-cidrcollection.html>`__
    """

    resource_type = "AWS::Route53::CidrCollection"

    props: PropsDictType = {
        "Locations": ([Location], False),
        "Name": (str, True),
    }


class DNSSEC(AWSObject):
    """
    `DNSSEC <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-dnssec.html>`__
    """

    resource_type = "AWS::Route53::DNSSEC"

    props: PropsDictType = {
        "HostedZoneId": (str, True),
    }


class AlarmIdentifier(AWSProperty):
    """
    `AlarmIdentifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Region": (str, True),
    }


class HealthCheckConfig(AWSProperty):
    """
    `HealthCheckConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html>`__
    """

    props: PropsDictType = {
        "AlarmIdentifier": (AlarmIdentifier, False),
        "ChildHealthChecks": ([str], False),
        "EnableSNI": (boolean, False),
        "FailureThreshold": (integer, False),
        "FullyQualifiedDomainName": (str, False),
        "HealthThreshold": (integer, False),
        "IPAddress": (str, False),
        "InsufficientDataHealthStatus": (str, False),
        "Inverted": (boolean, False),
        "MeasureLatency": (boolean, False),
        "Port": (integer, False),
        "Regions": ([str], False),
        "RequestInterval": (integer, False),
        "ResourcePath": (str, False),
        "RoutingControlArn": (str, False),
        "SearchString": (str, False),
        "Type": (str, True),
    }


class HealthCheck(AWSObject):
    """
    `HealthCheck <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html>`__
    """

    resource_type = "AWS::Route53::HealthCheck"

    props: PropsDictType = {
        "HealthCheckConfig": (HealthCheckConfig, True),
        "HealthCheckTags": (Tags, False),
    }


class HostedZoneConfiguration(AWSProperty):
    """
    `HostedZoneConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html>`__
    """

    props: PropsDictType = {
        "Comment": (str, False),
    }


class HostedZoneVPCs(AWSProperty):
    """
    `HostedZoneVPCs <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-vpc.html>`__
    """

    props: PropsDictType = {
        "VPCId": (str, True),
        "VPCRegion": (str, True),
    }


class QueryLoggingConfig(AWSProperty):
    """
    `QueryLoggingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html>`__
    """

    props: PropsDictType = {
        "CloudWatchLogsLogGroupArn": (str, True),
    }


class HostedZone(AWSObject):
    """
    `HostedZone <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html>`__
    """

    resource_type = "AWS::Route53::HostedZone"

    props: PropsDictType = {
        "HostedZoneConfig": (HostedZoneConfiguration, False),
        "HostedZoneTags": (Tags, False),
        "Name": (str, False),
        "QueryLoggingConfig": (QueryLoggingConfig, False),
        "VPCs": ([HostedZoneVPCs], False),
    }


class KeySigningKey(AWSObject):
    """
    `KeySigningKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html>`__
    """

    resource_type = "AWS::Route53::KeySigningKey"

    props: PropsDictType = {
        "HostedZoneId": (str, True),
        "KeyManagementServiceArn": (str, True),
        "Name": (str, True),
        "Status": (str, True),
    }


class CidrRoutingConfig(AWSProperty):
    """
    `CidrRoutingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrroutingconfig.html>`__
    """

    props: PropsDictType = {
        "CollectionId": (str, True),
        "LocationName": (str, True),
    }


class GeoLocation(AWSProperty):
    """
    `GeoLocation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html>`__
    """

    props: PropsDictType = {
        "ContinentCode": (str, False),
        "CountryCode": (str, False),
        "SubdivisionCode": (str, False),
    }


class RecordSet(AWSProperty):
    """
    `RecordSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html>`__
    """

    props: PropsDictType = {
        "AliasTarget": (AliasTarget, False),
        "CidrRoutingConfig": (CidrRoutingConfig, False),
        "Failover": (str, False),
        "GeoLocation": (GeoLocation, False),
        "HealthCheckId": (str, False),
        "HostedZoneId": (str, False),
        "HostedZoneName": (str, False),
        "MultiValueAnswer": (boolean, False),
        "Name": (str, True),
        "Region": (str, False),
        "ResourceRecords": ([str], False),
        "SetIdentifier": (str, False),
        "TTL": (str, False),
        "Type": (str, True),
        "Weight": (integer, False),
    }


class RecordSetGroup(AWSObject):
    """
    `RecordSetGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html>`__
    """

    resource_type = "AWS::Route53::RecordSetGroup"

    props: PropsDictType = {
        "Comment": (str, False),
        "HostedZoneId": (str, False),
        "HostedZoneName": (str, False),
        "RecordSets": ([RecordSet], False),
    }


class RecordSetType(AWSObject):
    """
    `RecordSetType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html>`__
    """

    resource_type = "AWS::Route53::RecordSet"

    props: PropsDictType = {
        "AliasTarget": (AliasTarget, False),
        "CidrRoutingConfig": (CidrRoutingConfig, False),
        "Comment": (str, False),
        "Failover": (str, False),
        "GeoLocation": (GeoLocation, False),
        "HealthCheckId": (str, False),
        "HostedZoneId": (str, False),
        "HostedZoneName": (str, False),
        "MultiValueAnswer": (boolean, False),
        "Name": (str, True),
        "Region": (str, False),
        "ResourceRecords": ([str], False),
        "SetIdentifier": (str, False),
        "TTL": (str, False),
        "Type": (str, True),
        "Weight": (integer, False),
    }
