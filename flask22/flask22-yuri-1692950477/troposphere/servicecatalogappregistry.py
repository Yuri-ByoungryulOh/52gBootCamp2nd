# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, PropsDictType


class Application(AWSObject):
    """
    `Application <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-application.html>`__
    """

    resource_type = "AWS::ServiceCatalogAppRegistry::Application"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (dict, False),
    }


class AttributeGroup(AWSObject):
    """
    `AttributeGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroup.html>`__
    """

    resource_type = "AWS::ServiceCatalogAppRegistry::AttributeGroup"

    props: PropsDictType = {
        "Attributes": (dict, True),
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (dict, False),
    }


class AttributeGroupAssociation(AWSObject):
    """
    `AttributeGroupAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroupassociation.html>`__
    """

    resource_type = "AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation"

    props: PropsDictType = {
        "Application": (str, True),
        "AttributeGroup": (str, True),
    }


class ResourceAssociation(AWSObject):
    """
    `ResourceAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-resourceassociation.html>`__
    """

    resource_type = "AWS::ServiceCatalogAppRegistry::ResourceAssociation"

    props: PropsDictType = {
        "Application": (str, True),
        "Resource": (str, True),
        "ResourceType": (str, True),
    }
