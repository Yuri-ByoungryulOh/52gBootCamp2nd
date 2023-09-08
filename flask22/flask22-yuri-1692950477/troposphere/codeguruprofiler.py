# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags


class AgentPermissions(AWSProperty):
    """
    `AgentPermissions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeguruprofiler-profilinggroup-agentpermissions.html>`__
    """

    props: PropsDictType = {
        "Principals": ([str], True),
    }


class Channel(AWSProperty):
    """
    `Channel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeguruprofiler-profilinggroup-channel.html>`__
    """

    props: PropsDictType = {
        "channelId": (str, False),
        "channelUri": (str, True),
    }


class ProfilingGroup(AWSObject):
    """
    `ProfilingGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html>`__
    """

    resource_type = "AWS::CodeGuruProfiler::ProfilingGroup"

    props: PropsDictType = {
        "AgentPermissions": (AgentPermissions, False),
        "AnomalyDetectionNotificationConfiguration": ([Channel], False),
        "ComputePlatform": (str, False),
        "ProfilingGroupName": (str, True),
        "Tags": (Tags, False),
    }