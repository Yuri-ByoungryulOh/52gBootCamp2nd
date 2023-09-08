# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.groundstation import validate_json_checker


class Bandwidth(AWSProperty):
    """
    `Bandwidth <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html>`__
    """

    props: PropsDictType = {
        "Units": (str, False),
        "Value": (double, False),
    }


class Frequency(AWSProperty):
    """
    `Frequency <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html>`__
    """

    props: PropsDictType = {
        "Units": (str, False),
        "Value": (double, False),
    }


class SpectrumConfig(AWSProperty):
    """
    `SpectrumConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html>`__
    """

    props: PropsDictType = {
        "Bandwidth": (Bandwidth, False),
        "CenterFrequency": (Frequency, False),
        "Polarization": (str, False),
    }


class AntennaDownlinkConfig(AWSProperty):
    """
    `AntennaDownlinkConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.html>`__
    """

    props: PropsDictType = {
        "SpectrumConfig": (SpectrumConfig, False),
    }


class DecodeConfig(AWSProperty):
    """
    `DecodeConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-decodeconfig.html>`__
    """

    props: PropsDictType = {
        "UnvalidatedJSON": (validate_json_checker, False),
    }


class DemodulationConfig(AWSProperty):
    """
    `DemodulationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-demodulationconfig.html>`__
    """

    props: PropsDictType = {
        "UnvalidatedJSON": (validate_json_checker, False),
    }


class AntennaDownlinkDemodDecodeConfig(AWSProperty):
    """
    `AntennaDownlinkDemodDecodeConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html>`__
    """

    props: PropsDictType = {
        "DecodeConfig": (DecodeConfig, False),
        "DemodulationConfig": (DemodulationConfig, False),
        "SpectrumConfig": (SpectrumConfig, False),
    }


class Eirp(AWSProperty):
    """
    `Eirp <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html>`__
    """

    props: PropsDictType = {
        "Units": (str, False),
        "Value": (double, False),
    }


class AntennaUplinkConfig(AWSProperty):
    """
    `AntennaUplinkConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html>`__
    """

    props: PropsDictType = {
        "SpectrumConfig": (SpectrumConfig, False),
        "TargetEirp": (Eirp, False),
        "TransmitDisabled": (boolean, False),
    }


class DataflowEndpointConfig(AWSProperty):
    """
    `DataflowEndpointConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html>`__
    """

    props: PropsDictType = {
        "DataflowEndpointName": (str, False),
        "DataflowEndpointRegion": (str, False),
    }


class S3RecordingConfig(AWSProperty):
    """
    `S3RecordingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html>`__
    """

    props: PropsDictType = {
        "BucketArn": (str, False),
        "Prefix": (str, False),
        "RoleArn": (str, False),
    }


class TrackingConfig(AWSProperty):
    """
    `TrackingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.html>`__
    """

    props: PropsDictType = {
        "Autotrack": (str, False),
    }


class UplinkEchoConfig(AWSProperty):
    """
    `UplinkEchoConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html>`__
    """

    props: PropsDictType = {
        "AntennaUplinkConfigArn": (str, False),
        "Enabled": (boolean, False),
    }


class ConfigData(AWSProperty):
    """
    `ConfigData <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html>`__
    """

    props: PropsDictType = {
        "AntennaDownlinkConfig": (AntennaDownlinkConfig, False),
        "AntennaDownlinkDemodDecodeConfig": (AntennaDownlinkDemodDecodeConfig, False),
        "AntennaUplinkConfig": (AntennaUplinkConfig, False),
        "DataflowEndpointConfig": (DataflowEndpointConfig, False),
        "S3RecordingConfig": (S3RecordingConfig, False),
        "TrackingConfig": (TrackingConfig, False),
        "UplinkEchoConfig": (UplinkEchoConfig, False),
    }


class Config(AWSObject):
    """
    `Config <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html>`__
    """

    resource_type = "AWS::GroundStation::Config"

    props: PropsDictType = {
        "ConfigData": (ConfigData, True),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class SocketAddress(AWSProperty):
    """
    `SocketAddress <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Port": (integer, False),
    }


class ConnectionDetails(AWSProperty):
    """
    `ConnectionDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-connectiondetails.html>`__
    """

    props: PropsDictType = {
        "Mtu": (integer, False),
        "SocketAddress": (SocketAddress, False),
    }


class IntegerRange(AWSProperty):
    """
    `IntegerRange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-integerrange.html>`__
    """

    props: PropsDictType = {
        "Maximum": (integer, False),
        "Minimum": (integer, False),
    }


class RangedSocketAddress(AWSProperty):
    """
    `RangedSocketAddress <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedsocketaddress.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "PortRange": (IntegerRange, False),
    }


class RangedConnectionDetails(AWSProperty):
    """
    `RangedConnectionDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedconnectiondetails.html>`__
    """

    props: PropsDictType = {
        "Mtu": (integer, False),
        "SocketAddress": (RangedSocketAddress, False),
    }


class AwsGroundStationAgentEndpoint(AWSProperty):
    """
    `AwsGroundStationAgentEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html>`__
    """

    props: PropsDictType = {
        "AgentStatus": (str, False),
        "AuditResults": (str, False),
        "EgressAddress": (ConnectionDetails, False),
        "IngressAddress": (RangedConnectionDetails, False),
        "Name": (str, False),
    }


class DataflowEndpoint(AWSProperty):
    """
    `DataflowEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html>`__
    """

    props: PropsDictType = {
        "Address": (SocketAddress, False),
        "Mtu": (integer, False),
        "Name": (str, False),
    }


class SecurityDetails(AWSProperty):
    """
    `SecurityDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html>`__
    """

    props: PropsDictType = {
        "RoleArn": (str, False),
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], False),
    }


class EndpointDetails(AWSProperty):
    """
    `EndpointDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html>`__
    """

    props: PropsDictType = {
        "AwsGroundStationAgentEndpoint": (AwsGroundStationAgentEndpoint, False),
        "Endpoint": (DataflowEndpoint, False),
        "SecurityDetails": (SecurityDetails, False),
    }


class DataflowEndpointGroup(AWSObject):
    """
    `DataflowEndpointGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html>`__
    """

    resource_type = "AWS::GroundStation::DataflowEndpointGroup"

    props: PropsDictType = {
        "ContactPostPassDurationSeconds": (integer, False),
        "ContactPrePassDurationSeconds": (integer, False),
        "EndpointDetails": ([EndpointDetails], True),
        "Tags": (Tags, False),
    }


class DataflowEdge(AWSProperty):
    """
    `DataflowEdge <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html>`__
    """

    props: PropsDictType = {
        "Destination": (str, False),
        "Source": (str, False),
    }


class StreamsKmsKey(AWSProperty):
    """
    `StreamsKmsKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-streamskmskey.html>`__
    """

    props: PropsDictType = {
        "KmsAliasArn": (str, False),
        "KmsKeyArn": (str, False),
    }


class MissionProfile(AWSObject):
    """
    `MissionProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html>`__
    """

    resource_type = "AWS::GroundStation::MissionProfile"

    props: PropsDictType = {
        "ContactPostPassDurationSeconds": (integer, False),
        "ContactPrePassDurationSeconds": (integer, False),
        "DataflowEdges": ([DataflowEdge], True),
        "MinimumViableContactDurationSeconds": (integer, True),
        "Name": (str, True),
        "StreamsKmsKey": (StreamsKmsKey, False),
        "StreamsKmsRole": (str, False),
        "Tags": (Tags, False),
        "TrackingConfigArn": (str, True),
    }