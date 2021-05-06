# coding: utf-8

"""
    Criteo API Transition Swagger

    This is used to help Criteo clients transition from MAPI to Criteo API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CampaignMessage(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'campaign_type': 'str',
        'advertiser_name': 'str',
        'categories': 'list[int]',
        'budget_id': 'int',
        'campaign_id': 'int',
        'campaign_name': 'str',
        'advertiser_id': 'int',
        'campaign_status': 'str',
        'campaign_bid': 'BidMessage'
    }

    attribute_map = {
        'campaign_type': 'campaignType',
        'advertiser_name': 'advertiserName',
        'categories': 'categories',
        'budget_id': 'budgetId',
        'campaign_id': 'campaignId',
        'campaign_name': 'campaignName',
        'advertiser_id': 'advertiserId',
        'campaign_status': 'campaignStatus',
        'campaign_bid': 'campaignBid'
    }

    def __init__(self, campaign_type=None, advertiser_name=None, categories=None, budget_id=None, campaign_id=None, campaign_name=None, advertiser_id=None, campaign_status=None, campaign_bid=None):  # noqa: E501
        """CampaignMessage - a model defined in OpenAPI"""  # noqa: E501

        self._campaign_type = None
        self._advertiser_name = None
        self._categories = None
        self._budget_id = None
        self._campaign_id = None
        self._campaign_name = None
        self._advertiser_id = None
        self._campaign_status = None
        self._campaign_bid = None
        self.discriminator = None

        if campaign_type is not None:
            self.campaign_type = campaign_type
        if advertiser_name is not None:
            self.advertiser_name = advertiser_name
        if categories is not None:
            self.categories = categories
        if budget_id is not None:
            self.budget_id = budget_id
        if campaign_id is not None:
            self.campaign_id = campaign_id
        if campaign_name is not None:
            self.campaign_name = campaign_name
        if advertiser_id is not None:
            self.advertiser_id = advertiser_id
        if campaign_status is not None:
            self.campaign_status = campaign_status
        if campaign_bid is not None:
            self.campaign_bid = campaign_bid

    @property
    def campaign_type(self):
        """Gets the campaign_type of this CampaignMessage.  # noqa: E501


        :return: The campaign_type of this CampaignMessage.  # noqa: E501
        :rtype: str
        """
        return self._campaign_type

    @campaign_type.setter
    def campaign_type(self, campaign_type):
        """Sets the campaign_type of this CampaignMessage.


        :param campaign_type: The campaign_type of this CampaignMessage.  # noqa: E501
        :type: str
        """

        self._campaign_type = campaign_type

    @property
    def advertiser_name(self):
        """Gets the advertiser_name of this CampaignMessage.  # noqa: E501


        :return: The advertiser_name of this CampaignMessage.  # noqa: E501
        :rtype: str
        """
        return self._advertiser_name

    @advertiser_name.setter
    def advertiser_name(self, advertiser_name):
        """Sets the advertiser_name of this CampaignMessage.


        :param advertiser_name: The advertiser_name of this CampaignMessage.  # noqa: E501
        :type: str
        """

        self._advertiser_name = advertiser_name

    @property
    def categories(self):
        """Gets the categories of this CampaignMessage.  # noqa: E501


        :return: The categories of this CampaignMessage.  # noqa: E501
        :rtype: list[int]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this CampaignMessage.


        :param categories: The categories of this CampaignMessage.  # noqa: E501
        :type: list[int]
        """

        self._categories = categories

    @property
    def budget_id(self):
        """Gets the budget_id of this CampaignMessage.  # noqa: E501


        :return: The budget_id of this CampaignMessage.  # noqa: E501
        :rtype: int
        """
        return self._budget_id

    @budget_id.setter
    def budget_id(self, budget_id):
        """Sets the budget_id of this CampaignMessage.


        :param budget_id: The budget_id of this CampaignMessage.  # noqa: E501
        :type: int
        """

        self._budget_id = budget_id

    @property
    def campaign_id(self):
        """Gets the campaign_id of this CampaignMessage.  # noqa: E501


        :return: The campaign_id of this CampaignMessage.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this CampaignMessage.


        :param campaign_id: The campaign_id of this CampaignMessage.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def campaign_name(self):
        """Gets the campaign_name of this CampaignMessage.  # noqa: E501


        :return: The campaign_name of this CampaignMessage.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this CampaignMessage.


        :param campaign_name: The campaign_name of this CampaignMessage.  # noqa: E501
        :type: str
        """

        self._campaign_name = campaign_name

    @property
    def advertiser_id(self):
        """Gets the advertiser_id of this CampaignMessage.  # noqa: E501


        :return: The advertiser_id of this CampaignMessage.  # noqa: E501
        :rtype: int
        """
        return self._advertiser_id

    @advertiser_id.setter
    def advertiser_id(self, advertiser_id):
        """Sets the advertiser_id of this CampaignMessage.


        :param advertiser_id: The advertiser_id of this CampaignMessage.  # noqa: E501
        :type: int
        """

        self._advertiser_id = advertiser_id

    @property
    def campaign_status(self):
        """Gets the campaign_status of this CampaignMessage.  # noqa: E501


        :return: The campaign_status of this CampaignMessage.  # noqa: E501
        :rtype: str
        """
        return self._campaign_status

    @campaign_status.setter
    def campaign_status(self, campaign_status):
        """Sets the campaign_status of this CampaignMessage.


        :param campaign_status: The campaign_status of this CampaignMessage.  # noqa: E501
        :type: str
        """

        self._campaign_status = campaign_status

    @property
    def campaign_bid(self):
        """Gets the campaign_bid of this CampaignMessage.  # noqa: E501


        :return: The campaign_bid of this CampaignMessage.  # noqa: E501
        :rtype: BidMessage
        """
        return self._campaign_bid

    @campaign_bid.setter
    def campaign_bid(self, campaign_bid):
        """Sets the campaign_bid of this CampaignMessage.


        :param campaign_bid: The campaign_bid of this CampaignMessage.  # noqa: E501
        :type: BidMessage
        """

        self._campaign_bid = campaign_bid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CampaignMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other