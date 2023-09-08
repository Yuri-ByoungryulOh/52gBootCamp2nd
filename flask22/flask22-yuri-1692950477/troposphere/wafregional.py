# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, integer
from .validators.wafregional import validate_waf_action_type


class FieldToMatch(AWSProperty):
    """
    `FieldToMatch <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html>`__
    """

    props: PropsDictType = {
        "Data": (str, False),
        "Type": (str, True),
    }


class ByteMatchTuples(AWSProperty):
    """
    `ByteMatchTuples <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html>`__
    """

    props: PropsDictType = {
        "FieldToMatch": (FieldToMatch, True),
        "PositionalConstraint": (str, True),
        "TargetString": (str, False),
        "TargetStringBase64": (str, False),
        "TextTransformation": (str, True),
    }


class ByteMatchSet(AWSObject):
    """
    `ByteMatchSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html>`__
    """

    resource_type = "AWS::WAFRegional::ByteMatchSet"

    props: PropsDictType = {
        "ByteMatchTuples": ([ByteMatchTuples], False),
        "Name": (str, True),
    }


class GeoMatchConstraints(AWSProperty):
    """
    `GeoMatchConstraints <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (str, True),
    }


class GeoMatchSet(AWSObject):
    """
    `GeoMatchSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html>`__
    """

    resource_type = "AWS::WAFRegional::GeoMatchSet"

    props: PropsDictType = {
        "GeoMatchConstraints": ([GeoMatchConstraints], False),
        "Name": (str, True),
    }


class IPSetDescriptors(AWSProperty):
    """
    `IPSetDescriptors <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (str, True),
    }


class IPSet(AWSObject):
    """
    `IPSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html>`__
    """

    resource_type = "AWS::WAFRegional::IPSet"

    props: PropsDictType = {
        "IPSetDescriptors": ([IPSetDescriptors], False),
        "Name": (str, True),
    }


class Predicates(AWSProperty):
    """
    `Predicates <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html>`__
    """

    props: PropsDictType = {
        "DataId": (str, True),
        "Negated": (boolean, True),
        "Type": (str, True),
    }


class RateBasedRule(AWSObject):
    """
    `RateBasedRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html>`__
    """

    resource_type = "AWS::WAFRegional::RateBasedRule"

    props: PropsDictType = {
        "MatchPredicates": ([Predicates], False),
        "MetricName": (str, True),
        "Name": (str, True),
        "RateKey": (str, True),
        "RateLimit": (integer, True),
    }


class RegexPatternSet(AWSObject):
    """
    `RegexPatternSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html>`__
    """

    resource_type = "AWS::WAFRegional::RegexPatternSet"

    props: PropsDictType = {
        "Name": (str, True),
        "RegexPatternStrings": ([str], True),
    }


class Rule(AWSObject):
    """
    `Rule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html>`__
    """

    resource_type = "AWS::WAFRegional::Rule"

    props: PropsDictType = {
        "MetricName": (str, True),
        "Name": (str, True),
        "Predicates": ([Predicates], False),
    }


class SizeConstraint(AWSProperty):
    """
    `SizeConstraint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html>`__
    """

    props: PropsDictType = {
        "ComparisonOperator": (str, True),
        "FieldToMatch": (FieldToMatch, True),
        "Size": (integer, True),
        "TextTransformation": (str, True),
    }


class SizeConstraintSet(AWSObject):
    """
    `SizeConstraintSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html>`__
    """

    resource_type = "AWS::WAFRegional::SizeConstraintSet"

    props: PropsDictType = {
        "Name": (str, True),
        "SizeConstraints": ([SizeConstraint], False),
    }


class SqlInjectionMatchTuples(AWSProperty):
    """
    `SqlInjectionMatchTuples <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html>`__
    """

    props: PropsDictType = {
        "FieldToMatch": (FieldToMatch, True),
        "TextTransformation": (str, True),
    }


class SqlInjectionMatchSet(AWSObject):
    """
    `SqlInjectionMatchSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html>`__
    """

    resource_type = "AWS::WAFRegional::SqlInjectionMatchSet"

    props: PropsDictType = {
        "Name": (str, True),
        "SqlInjectionMatchTuples": ([SqlInjectionMatchTuples], False),
    }


class Action(AWSProperty):
    """
    `Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-action.html>`__
    """

    props: PropsDictType = {
        "Type": (validate_waf_action_type, True),
    }


class Rules(AWSProperty):
    """
    `Rules <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html>`__
    """

    props: PropsDictType = {
        "Action": (Action, True),
        "Priority": (integer, True),
        "RuleId": (str, True),
    }


class WebACL(AWSObject):
    """
    `WebACL <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html>`__
    """

    resource_type = "AWS::WAFRegional::WebACL"

    props: PropsDictType = {
        "DefaultAction": (Action, True),
        "MetricName": (str, True),
        "Name": (str, True),
        "Rules": ([Rules], False),
    }


class WebACLAssociation(AWSObject):
    """
    `WebACLAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html>`__
    """

    resource_type = "AWS::WAFRegional::WebACLAssociation"

    props: PropsDictType = {
        "ResourceArn": (str, True),
        "WebACLId": (str, True),
    }


class XssMatchTuple(AWSProperty):
    """
    `XssMatchTuple <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html>`__
    """

    props: PropsDictType = {
        "FieldToMatch": (FieldToMatch, True),
        "TextTransformation": (str, True),
    }


class XssMatchSet(AWSObject):
    """
    `XssMatchSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html>`__
    """

    resource_type = "AWS::WAFRegional::XssMatchSet"

    props: PropsDictType = {
        "Name": (str, True),
        "XssMatchTuples": ([XssMatchTuple], False),
    }
