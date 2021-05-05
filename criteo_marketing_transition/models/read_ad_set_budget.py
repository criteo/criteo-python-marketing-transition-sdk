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


class ReadAdSetBudget(object):
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
        'budget_strategy': 'str',
        'budget_renewal': 'str',
        'budget_delivery_smoothing': 'str',
        'budget_delivery_week': 'str',
        'budget_amount': 'NillableDecimal'
    }

    attribute_map = {
        'budget_strategy': 'budgetStrategy',
        'budget_renewal': 'budgetRenewal',
        'budget_delivery_smoothing': 'budgetDeliverySmoothing',
        'budget_delivery_week': 'budgetDeliveryWeek',
        'budget_amount': 'budgetAmount'
    }

    def __init__(self, budget_strategy=None, budget_renewal=None, budget_delivery_smoothing=None, budget_delivery_week=None, budget_amount=None):  # noqa: E501
        """ReadAdSetBudget - a model defined in OpenAPI"""  # noqa: E501

        self._budget_strategy = None
        self._budget_renewal = None
        self._budget_delivery_smoothing = None
        self._budget_delivery_week = None
        self._budget_amount = None
        self.discriminator = None

        if budget_strategy is not None:
            self.budget_strategy = budget_strategy
        if budget_renewal is not None:
            self.budget_renewal = budget_renewal
        if budget_delivery_smoothing is not None:
            self.budget_delivery_smoothing = budget_delivery_smoothing
        if budget_delivery_week is not None:
            self.budget_delivery_week = budget_delivery_week
        if budget_amount is not None:
            self.budget_amount = budget_amount

    @property
    def budget_strategy(self):
        """Gets the budget_strategy of this ReadAdSetBudget.  # noqa: E501

        Whether your budget is capped or not  # noqa: E501

        :return: The budget_strategy of this ReadAdSetBudget.  # noqa: E501
        :rtype: str
        """
        return self._budget_strategy

    @budget_strategy.setter
    def budget_strategy(self, budget_strategy):
        """Sets the budget_strategy of this ReadAdSetBudget.

        Whether your budget is capped or not  # noqa: E501

        :param budget_strategy: The budget_strategy of this ReadAdSetBudget.  # noqa: E501
        :type: str
        """

        self._budget_strategy = budget_strategy

    @property
    def budget_renewal(self):
        """Gets the budget_renewal of this ReadAdSetBudget.  # noqa: E501

        The pace of the budget renewal  # noqa: E501

        :return: The budget_renewal of this ReadAdSetBudget.  # noqa: E501
        :rtype: str
        """
        return self._budget_renewal

    @budget_renewal.setter
    def budget_renewal(self, budget_renewal):
        """Sets the budget_renewal of this ReadAdSetBudget.

        The pace of the budget renewal  # noqa: E501

        :param budget_renewal: The budget_renewal of this ReadAdSetBudget.  # noqa: E501
        :type: str
        """

        self._budget_renewal = budget_renewal

    @property
    def budget_delivery_smoothing(self):
        """Gets the budget_delivery_smoothing of this ReadAdSetBudget.  # noqa: E501

        The pace at which the budget can be spent  # noqa: E501

        :return: The budget_delivery_smoothing of this ReadAdSetBudget.  # noqa: E501
        :rtype: str
        """
        return self._budget_delivery_smoothing

    @budget_delivery_smoothing.setter
    def budget_delivery_smoothing(self, budget_delivery_smoothing):
        """Sets the budget_delivery_smoothing of this ReadAdSetBudget.

        The pace at which the budget can be spent  # noqa: E501

        :param budget_delivery_smoothing: The budget_delivery_smoothing of this ReadAdSetBudget.  # noqa: E501
        :type: str
        """

        self._budget_delivery_smoothing = budget_delivery_smoothing

    @property
    def budget_delivery_week(self):
        """Gets the budget_delivery_week of this ReadAdSetBudget.  # noqa: E501

        The delivery week for the budget  # noqa: E501

        :return: The budget_delivery_week of this ReadAdSetBudget.  # noqa: E501
        :rtype: str
        """
        return self._budget_delivery_week

    @budget_delivery_week.setter
    def budget_delivery_week(self, budget_delivery_week):
        """Sets the budget_delivery_week of this ReadAdSetBudget.

        The delivery week for the budget  # noqa: E501

        :param budget_delivery_week: The budget_delivery_week of this ReadAdSetBudget.  # noqa: E501
        :type: str
        """

        self._budget_delivery_week = budget_delivery_week

    @property
    def budget_amount(self):
        """Gets the budget_amount of this ReadAdSetBudget.  # noqa: E501


        :return: The budget_amount of this ReadAdSetBudget.  # noqa: E501
        :rtype: NillableDecimal
        """
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, budget_amount):
        """Sets the budget_amount of this ReadAdSetBudget.


        :param budget_amount: The budget_amount of this ReadAdSetBudget.  # noqa: E501
        :type: NillableDecimal
        """

        self._budget_amount = budget_amount

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
        if not isinstance(other, ReadAdSetBudget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
