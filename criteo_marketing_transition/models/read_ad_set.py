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


class ReadAdSet(object):
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
        'name': 'str',
        'advertiser_id': 'str',
        'campaign_id': 'str',
        'destination_environment': 'str',
        'schedule': 'ReadAdSetSchedule',
        'bidding': 'ReadAdSetBidding',
        'targeting': 'AdSetTargeting',
        'budget': 'ReadAdSetBudget'
    }

    attribute_map = {
        'name': 'name',
        'advertiser_id': 'advertiserId',
        'campaign_id': 'campaignId',
        'destination_environment': 'destinationEnvironment',
        'schedule': 'schedule',
        'bidding': 'bidding',
        'targeting': 'targeting',
        'budget': 'budget'
    }

    def __init__(self, name=None, advertiser_id=None, campaign_id=None, destination_environment=None, schedule=None, bidding=None, targeting=None, budget=None):  # noqa: E501
        """ReadAdSet - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._advertiser_id = None
        self._campaign_id = None
        self._destination_environment = None
        self._schedule = None
        self._bidding = None
        self._targeting = None
        self._budget = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if advertiser_id is not None:
            self.advertiser_id = advertiser_id
        if campaign_id is not None:
            self.campaign_id = campaign_id
        if destination_environment is not None:
            self.destination_environment = destination_environment
        if schedule is not None:
            self.schedule = schedule
        if bidding is not None:
            self.bidding = bidding
        if targeting is not None:
            self.targeting = targeting
        if budget is not None:
            self.budget = budget

    @property
    def name(self):
        """Gets the name of this ReadAdSet.  # noqa: E501

        Name of the ad set  # noqa: E501

        :return: The name of this ReadAdSet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReadAdSet.

        Name of the ad set  # noqa: E501

        :param name: The name of this ReadAdSet.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def advertiser_id(self):
        """Gets the advertiser_id of this ReadAdSet.  # noqa: E501

        Advertiser id of the campaign this ad set belongs to  # noqa: E501

        :return: The advertiser_id of this ReadAdSet.  # noqa: E501
        :rtype: str
        """
        return self._advertiser_id

    @advertiser_id.setter
    def advertiser_id(self, advertiser_id):
        """Sets the advertiser_id of this ReadAdSet.

        Advertiser id of the campaign this ad set belongs to  # noqa: E501

        :param advertiser_id: The advertiser_id of this ReadAdSet.  # noqa: E501
        :type: str
        """

        self._advertiser_id = advertiser_id

    @property
    def campaign_id(self):
        """Gets the campaign_id of this ReadAdSet.  # noqa: E501

        Campaign id this ad set belongs to  # noqa: E501

        :return: The campaign_id of this ReadAdSet.  # noqa: E501
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this ReadAdSet.

        Campaign id this ad set belongs to  # noqa: E501

        :param campaign_id: The campaign_id of this ReadAdSet.  # noqa: E501
        :type: str
        """

        self._campaign_id = campaign_id

    @property
    def destination_environment(self):
        """Gets the destination_environment of this ReadAdSet.  # noqa: E501

        The environment that an ad click will lead a user to  # noqa: E501

        :return: The destination_environment of this ReadAdSet.  # noqa: E501
        :rtype: str
        """
        return self._destination_environment

    @destination_environment.setter
    def destination_environment(self, destination_environment):
        """Sets the destination_environment of this ReadAdSet.

        The environment that an ad click will lead a user to  # noqa: E501

        :param destination_environment: The destination_environment of this ReadAdSet.  # noqa: E501
        :type: str
        """

        self._destination_environment = destination_environment

    @property
    def schedule(self):
        """Gets the schedule of this ReadAdSet.  # noqa: E501


        :return: The schedule of this ReadAdSet.  # noqa: E501
        :rtype: ReadAdSetSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ReadAdSet.


        :param schedule: The schedule of this ReadAdSet.  # noqa: E501
        :type: ReadAdSetSchedule
        """

        self._schedule = schedule

    @property
    def bidding(self):
        """Gets the bidding of this ReadAdSet.  # noqa: E501


        :return: The bidding of this ReadAdSet.  # noqa: E501
        :rtype: ReadAdSetBidding
        """
        return self._bidding

    @bidding.setter
    def bidding(self, bidding):
        """Sets the bidding of this ReadAdSet.


        :param bidding: The bidding of this ReadAdSet.  # noqa: E501
        :type: ReadAdSetBidding
        """

        self._bidding = bidding

    @property
    def targeting(self):
        """Gets the targeting of this ReadAdSet.  # noqa: E501


        :return: The targeting of this ReadAdSet.  # noqa: E501
        :rtype: AdSetTargeting
        """
        return self._targeting

    @targeting.setter
    def targeting(self, targeting):
        """Sets the targeting of this ReadAdSet.


        :param targeting: The targeting of this ReadAdSet.  # noqa: E501
        :type: AdSetTargeting
        """

        self._targeting = targeting

    @property
    def budget(self):
        """Gets the budget of this ReadAdSet.  # noqa: E501


        :return: The budget of this ReadAdSet.  # noqa: E501
        :rtype: ReadAdSetBudget
        """
        return self._budget

    @budget.setter
    def budget(self, budget):
        """Sets the budget of this ReadAdSet.


        :param budget: The budget of this ReadAdSet.  # noqa: E501
        :type: ReadAdSetBudget
        """

        self._budget = budget

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
        if not isinstance(other, ReadAdSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other