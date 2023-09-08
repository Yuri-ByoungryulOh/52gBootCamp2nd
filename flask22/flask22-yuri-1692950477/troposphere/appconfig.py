# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.appconfig import (
    validate_growth_type,
    validate_replicate_to,
    validate_validator_type,
)


class Application(AWSObject):
    """
    `Application <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html>`__
    """

    resource_type = "AWS::AppConfig::Application"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class Validators(AWSProperty):
    """
    `Validators <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html>`__
    """

    props: PropsDictType = {
        "Content": (str, False),
        "Type": (validate_validator_type, False),
    }


class ConfigurationProfile(AWSObject):
    """
    `ConfigurationProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html>`__
    """

    resource_type = "AWS::AppConfig::ConfigurationProfile"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "Description": (str, False),
        "LocationUri": (str, True),
        "Name": (str, True),
        "RetrievalRoleArn": (str, False),
        "Tags": (Tags, False),
        "Type": (str, False),
        "Validators": ([Validators], False),
    }


class Deployment(AWSObject):
    """
    `Deployment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html>`__
    """

    resource_type = "AWS::AppConfig::Deployment"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "ConfigurationProfileId": (str, True),
        "ConfigurationVersion": (str, True),
        "DeploymentStrategyId": (str, True),
        "Description": (str, False),
        "EnvironmentId": (str, True),
        "KmsKeyIdentifier": (str, False),
        "Tags": (Tags, False),
    }


class DeploymentStrategy(AWSObject):
    """
    `DeploymentStrategy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html>`__
    """

    resource_type = "AWS::AppConfig::DeploymentStrategy"

    props: PropsDictType = {
        "DeploymentDurationInMinutes": (double, True),
        "Description": (str, False),
        "FinalBakeTimeInMinutes": (double, False),
        "GrowthFactor": (double, True),
        "GrowthType": (validate_growth_type, False),
        "Name": (str, True),
        "ReplicateTo": (validate_replicate_to, True),
        "Tags": (Tags, False),
    }


class Monitors(AWSProperty):
    """
    `Monitors <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html>`__
    """

    props: PropsDictType = {
        "AlarmArn": (str, False),
        "AlarmRoleArn": (str, False),
    }


class Environment(AWSObject):
    """
    `Environment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html>`__
    """

    resource_type = "AWS::AppConfig::Environment"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "Description": (str, False),
        "Monitors": ([Monitors], False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class Parameter(AWSProperty):
    """
    `Parameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-parameter.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "Required": (boolean, True),
    }


class Extension(AWSObject):
    """
    `Extension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html>`__
    """

    resource_type = "AWS::AppConfig::Extension"

    props: PropsDictType = {
        "Actions": (dict, True),
        "Description": (str, False),
        "LatestVersionNumber": (integer, False),
        "Name": (str, True),
        "Parameters": (dict, False),
        "Tags": (Tags, False),
    }


class ExtensionAssociation(AWSObject):
    """
    `ExtensionAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html>`__
    """

    resource_type = "AWS::AppConfig::ExtensionAssociation"

    props: PropsDictType = {
        "ExtensionIdentifier": (str, False),
        "ExtensionVersionNumber": (integer, False),
        "Parameters": (dict, False),
        "ResourceIdentifier": (str, False),
        "Tags": (Tags, False),
    }


class HostedConfigurationVersion(AWSObject):
    """
    `HostedConfigurationVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html>`__
    """

    resource_type = "AWS::AppConfig::HostedConfigurationVersion"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "ConfigurationProfileId": (str, True),
        "Content": (str, True),
        "ContentType": (str, True),
        "Description": (str, False),
        "LatestVersionNumber": (double, False),
        "VersionLabel": (str, False),
    }
