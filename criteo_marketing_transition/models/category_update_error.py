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


class CategoryUpdateError(object):
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
        'category_hash_code': 'int',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'category_hash_code': 'categoryHashCode',
        'error_code': 'errorCode',
        'error_message': 'errorMessage'
    }

    def __init__(self, category_hash_code=None, error_code=None, error_message=None):  # noqa: E501
        """CategoryUpdateError - a model defined in OpenAPI"""  # noqa: E501

        self._category_hash_code = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if category_hash_code is not None:
            self.category_hash_code = category_hash_code
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def category_hash_code(self):
        """Gets the category_hash_code of this CategoryUpdateError.  # noqa: E501


        :return: The category_hash_code of this CategoryUpdateError.  # noqa: E501
        :rtype: int
        """
        return self._category_hash_code

    @category_hash_code.setter
    def category_hash_code(self, category_hash_code):
        """Sets the category_hash_code of this CategoryUpdateError.


        :param category_hash_code: The category_hash_code of this CategoryUpdateError.  # noqa: E501
        :type: int
        """

        self._category_hash_code = category_hash_code

    @property
    def error_code(self):
        """Gets the error_code of this CategoryUpdateError.  # noqa: E501


        :return: The error_code of this CategoryUpdateError.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CategoryUpdateError.


        :param error_code: The error_code of this CategoryUpdateError.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this CategoryUpdateError.  # noqa: E501


        :return: The error_message of this CategoryUpdateError.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this CategoryUpdateError.


        :param error_message: The error_message of this CategoryUpdateError.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if not isinstance(other, CategoryUpdateError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
