# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class Destination(AWSObject):
    """
    `Destination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html>`__
    """

    resource_type = "AWS::IoTWireless::Destination"

    props: PropsDictType = {
        "Description": (str, False),
        "Expression": (str, True),
        "ExpressionType": (str, True),
        "Name": (str, True),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
    }


class LoRaWANDeviceProfile(AWSProperty):
    """
    `LoRaWANDeviceProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html>`__
    """

    props: PropsDictType = {
        "ClassBTimeout": (integer, False),
        "ClassCTimeout": (integer, False),
        "FactoryPresetFreqsList": ([integer], False),
        "MacVersion": (str, False),
        "MaxDutyCycle": (integer, False),
        "MaxEirp": (integer, False),
        "PingSlotDr": (integer, False),
        "PingSlotFreq": (integer, False),
        "PingSlotPeriod": (integer, False),
        "RegParamsRevision": (str, False),
        "RfRegion": (str, False),
        "RxDataRate2": (integer, False),
        "RxDelay1": (integer, False),
        "RxDrOffset1": (integer, False),
        "RxFreq2": (integer, False),
        "Supports32BitFCnt": (boolean, False),
        "SupportsClassB": (boolean, False),
        "SupportsClassC": (boolean, False),
        "SupportsJoin": (boolean, False),
    }


class DeviceProfile(AWSObject):
    """
    `DeviceProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html>`__
    """

    resource_type = "AWS::IoTWireless::DeviceProfile"

    props: PropsDictType = {
        "LoRaWAN": (LoRaWANDeviceProfile, False),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class FuotaTaskLoRaWAN(AWSProperty):
    """
    `FuotaTaskLoRaWAN <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html>`__
    """

    props: PropsDictType = {
        "RfRegion": (str, True),
        "StartTime": (str, False),
    }


class FuotaTask(AWSObject):
    """
    `FuotaTask <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html>`__
    """

    resource_type = "AWS::IoTWireless::FuotaTask"

    props: PropsDictType = {
        "AssociateMulticastGroup": (str, False),
        "AssociateWirelessDevice": (str, False),
        "Description": (str, False),
        "DisassociateMulticastGroup": (str, False),
        "DisassociateWirelessDevice": (str, False),
        "FirmwareUpdateImage": (str, True),
        "FirmwareUpdateRole": (str, True),
        "LoRaWAN": (FuotaTaskLoRaWAN, True),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class LoRaWAN(AWSProperty):
    """
    `LoRaWAN <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html>`__
    """

    props: PropsDictType = {
        "DlClass": (str, True),
        "NumberOfDevicesInGroup": (integer, False),
        "NumberOfDevicesRequested": (integer, False),
        "RfRegion": (str, True),
    }


class MulticastGroup(AWSObject):
    """
    `MulticastGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html>`__
    """

    resource_type = "AWS::IoTWireless::MulticastGroup"

    props: PropsDictType = {
        "AssociateWirelessDevice": (str, False),
        "Description": (str, False),
        "DisassociateWirelessDevice": (str, False),
        "LoRaWAN": (LoRaWAN, True),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class TraceContent(AWSProperty):
    """
    `TraceContent <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent.html>`__
    """

    props: PropsDictType = {
        "LogLevel": (str, False),
        "WirelessDeviceFrameInfo": (str, False),
    }


class NetworkAnalyzerConfiguration(AWSObject):
    """
    `NetworkAnalyzerConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html>`__
    """

    resource_type = "AWS::IoTWireless::NetworkAnalyzerConfiguration"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
        "TraceContent": (TraceContent, False),
        "WirelessDevices": ([str], False),
        "WirelessGateways": ([str], False),
    }


class SidewalkAccountInfo(AWSProperty):
    """
    `SidewalkAccountInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfo.html>`__
    """

    props: PropsDictType = {
        "AppServerPrivateKey": (str, True),
    }


class SidewalkAccountInfoWithFingerprint(AWSProperty):
    """
    `SidewalkAccountInfoWithFingerprint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint.html>`__
    """

    props: PropsDictType = {
        "AmazonId": (str, False),
        "Arn": (str, False),
        "Fingerprint": (str, False),
    }


class SidewalkUpdateAccount(AWSProperty):
    """
    `SidewalkUpdateAccount <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkupdateaccount.html>`__
    """

    props: PropsDictType = {
        "AppServerPrivateKey": (str, False),
    }


class PartnerAccount(AWSObject):
    """
    `PartnerAccount <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html>`__
    """

    resource_type = "AWS::IoTWireless::PartnerAccount"

    props: PropsDictType = {
        "AccountLinked": (boolean, False),
        "PartnerAccountId": (str, False),
        "PartnerType": (str, False),
        "Sidewalk": (SidewalkAccountInfo, False),
        "SidewalkResponse": (SidewalkAccountInfoWithFingerprint, False),
        "SidewalkUpdate": (SidewalkUpdateAccount, False),
        "Tags": (Tags, False),
    }


class LoRaWANServiceProfile(AWSProperty):
    """
    `LoRaWANServiceProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html>`__
    """

    props: PropsDictType = {
        "AddGwMetadata": (boolean, False),
        "ChannelMask": (str, False),
        "DevStatusReqFreq": (integer, False),
        "DlBucketSize": (integer, False),
        "DlRate": (integer, False),
        "DlRatePolicy": (str, False),
        "DrMax": (integer, False),
        "DrMin": (integer, False),
        "HrAllowed": (boolean, False),
        "MinGwDiversity": (integer, False),
        "NwkGeoLoc": (boolean, False),
        "PrAllowed": (boolean, False),
        "RaAllowed": (boolean, False),
        "ReportDevStatusBattery": (boolean, False),
        "ReportDevStatusMargin": (boolean, False),
        "TargetPer": (integer, False),
        "UlBucketSize": (integer, False),
        "UlRate": (integer, False),
        "UlRatePolicy": (str, False),
    }


class ServiceProfile(AWSObject):
    """
    `ServiceProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html>`__
    """

    resource_type = "AWS::IoTWireless::ServiceProfile"

    props: PropsDictType = {
        "LoRaWAN": (LoRaWANServiceProfile, False),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class LoRaWANGatewayVersion(AWSProperty):
    """
    `LoRaWANGatewayVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html>`__
    """

    props: PropsDictType = {
        "Model": (str, False),
        "PackageVersion": (str, False),
        "Station": (str, False),
    }


class LoRaWANUpdateGatewayTaskEntry(AWSProperty):
    """
    `LoRaWANUpdateGatewayTaskEntry <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html>`__
    """

    props: PropsDictType = {
        "CurrentVersion": (LoRaWANGatewayVersion, False),
        "UpdateVersion": (LoRaWANGatewayVersion, False),
    }


class LoRaWANUpdateGatewayTaskCreate(AWSProperty):
    """
    `LoRaWANUpdateGatewayTaskCreate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html>`__
    """

    props: PropsDictType = {
        "CurrentVersion": (LoRaWANGatewayVersion, False),
        "SigKeyCrc": (integer, False),
        "UpdateSignature": (str, False),
        "UpdateVersion": (LoRaWANGatewayVersion, False),
    }


class UpdateWirelessGatewayTaskCreate(AWSProperty):
    """
    `UpdateWirelessGatewayTaskCreate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html>`__
    """

    props: PropsDictType = {
        "LoRaWAN": (LoRaWANUpdateGatewayTaskCreate, False),
        "UpdateDataRole": (str, False),
        "UpdateDataSource": (str, False),
    }


class TaskDefinition(AWSObject):
    """
    `TaskDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html>`__
    """

    resource_type = "AWS::IoTWireless::TaskDefinition"

    props: PropsDictType = {
        "AutoCreateTasks": (boolean, True),
        "LoRaWANUpdateGatewayTaskEntry": (LoRaWANUpdateGatewayTaskEntry, False),
        "Name": (str, False),
        "Tags": (Tags, False),
        "TaskDefinitionType": (str, False),
        "Update": (UpdateWirelessGatewayTaskCreate, False),
    }


class SessionKeysAbpV10x(AWSProperty):
    """
    `SessionKeysAbpV10x <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html>`__
    """

    props: PropsDictType = {
        "AppSKey": (str, True),
        "NwkSKey": (str, True),
    }


class AbpV10x(AWSProperty):
    """
    `AbpV10x <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html>`__
    """

    props: PropsDictType = {
        "DevAddr": (str, True),
        "SessionKeys": (SessionKeysAbpV10x, True),
    }


class SessionKeysAbpV11(AWSProperty):
    """
    `SessionKeysAbpV11 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html>`__
    """

    props: PropsDictType = {
        "AppSKey": (str, True),
        "FNwkSIntKey": (str, True),
        "NwkSEncKey": (str, True),
        "SNwkSIntKey": (str, True),
    }


class AbpV11(AWSProperty):
    """
    `AbpV11 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html>`__
    """

    props: PropsDictType = {
        "DevAddr": (str, True),
        "SessionKeys": (SessionKeysAbpV11, True),
    }


class OtaaV10x(AWSProperty):
    """
    `OtaaV10x <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html>`__
    """

    props: PropsDictType = {
        "AppEui": (str, True),
        "AppKey": (str, True),
    }


class OtaaV11(AWSProperty):
    """
    `OtaaV11 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html>`__
    """

    props: PropsDictType = {
        "AppKey": (str, True),
        "JoinEui": (str, True),
        "NwkKey": (str, True),
    }


class LoRaWANDevice(AWSProperty):
    """
    `LoRaWANDevice <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html>`__
    """

    props: PropsDictType = {
        "AbpV10x": (AbpV10x, False),
        "AbpV11": (AbpV11, False),
        "DevEui": (str, False),
        "DeviceProfileId": (str, False),
        "OtaaV10x": (OtaaV10x, False),
        "OtaaV11": (OtaaV11, False),
        "ServiceProfileId": (str, False),
    }


class WirelessDevice(AWSObject):
    """
    `WirelessDevice <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html>`__
    """

    resource_type = "AWS::IoTWireless::WirelessDevice"

    props: PropsDictType = {
        "Description": (str, False),
        "DestinationName": (str, True),
        "LastUplinkReceivedAt": (str, False),
        "LoRaWAN": (LoRaWANDevice, False),
        "Name": (str, False),
        "Tags": (Tags, False),
        "ThingArn": (str, False),
        "Type": (str, True),
    }


class Sidewalk(AWSProperty):
    """
    `Sidewalk <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdeviceimporttask-sidewalk.html>`__
    """

    props: PropsDictType = {
        "DeviceCreationFile": (str, False),
        "DeviceCreationFileList": ([str], False),
        "Role": (str, False),
        "SidewalkManufacturingSn": (str, False),
    }


class WirelessDeviceImportTask(AWSObject):
    """
    `WirelessDeviceImportTask <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdeviceimporttask.html>`__
    """

    resource_type = "AWS::IoTWireless::WirelessDeviceImportTask"

    props: PropsDictType = {
        "DestinationName": (str, True),
        "Sidewalk": (Sidewalk, True),
        "Tags": (Tags, False),
    }


class LoRaWANGateway(AWSProperty):
    """
    `LoRaWANGateway <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html>`__
    """

    props: PropsDictType = {
        "GatewayEui": (str, True),
        "RfRegion": (str, True),
    }


class WirelessGateway(AWSObject):
    """
    `WirelessGateway <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html>`__
    """

    resource_type = "AWS::IoTWireless::WirelessGateway"

    props: PropsDictType = {
        "Description": (str, False),
        "LastUplinkReceivedAt": (str, False),
        "LoRaWAN": (LoRaWANGateway, True),
        "Name": (str, False),
        "Tags": (Tags, False),
        "ThingArn": (str, False),
        "ThingName": (str, False),
    }