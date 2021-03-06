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


class InlineObject(object):
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
        'client_id': 'str',
        'client_secret': 'str',
        'grant_type': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'grant_type': 'grant_type'
    }

    def __init__(self, client_id=None, client_secret=None, grant_type='client_credentials'):  # noqa: E501
        """InlineObject - a model defined in OpenAPI"""  # noqa: E501

        self._client_id = None
        self._client_secret = None
        self._grant_type = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if grant_type is not None:
            self.grant_type = grant_type

    @property
    def client_id(self):
        """Gets the client_id of this InlineObject.  # noqa: E501

        API Client-Id or Username  # noqa: E501

        :return: The client_id of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this InlineObject.

        API Client-Id or Username  # noqa: E501

        :param client_id: The client_id of this InlineObject.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this InlineObject.  # noqa: E501

        API Client secret or password  # noqa: E501

        :return: The client_secret of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this InlineObject.

        API Client secret or password  # noqa: E501

        :param client_secret: The client_secret of this InlineObject.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def grant_type(self):
        """Gets the grant_type of this InlineObject.  # noqa: E501

        Other grant types are not available  # noqa: E501

        :return: The grant_type of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """Sets the grant_type of this InlineObject.

        Other grant types are not available  # noqa: E501

        :param grant_type: The grant_type of this InlineObject.  # noqa: E501
        :type: str
        """

        self._grant_type = grant_type

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
        if not isinstance(other, InlineObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
