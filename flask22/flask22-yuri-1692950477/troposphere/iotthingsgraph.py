# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import double


class DefinitionDocument(AWSProperty):
    """
    `DefinitionDocument <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html>`__
    """

    props: PropsDictType = {
        "Language": (str, True),
        "Text": (str, True),
    }


class FlowTemplate(AWSObject):
    """
    `FlowTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html>`__
    """

    resource_type = "AWS::IoTThingsGraph::FlowTemplate"

    props: PropsDictType = {
        "CompatibleNamespaceVersion": (double, False),
        "Definition": (DefinitionDocument, True),
    }
