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


class CategoryUpdatesPerCatalog(object):
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
        'catalog_id': 'int',
        'categories': 'list[CategoryUpdateInput]'
    }

    attribute_map = {
        'catalog_id': 'catalogId',
        'categories': 'categories'
    }

    def __init__(self, catalog_id=None, categories=None):  # noqa: E501
        """CategoryUpdatesPerCatalog - a model defined in OpenAPI"""  # noqa: E501

        self._catalog_id = None
        self._categories = None
        self.discriminator = None

        if catalog_id is not None:
            self.catalog_id = catalog_id
        if categories is not None:
            self.categories = categories

    @property
    def catalog_id(self):
        """Gets the catalog_id of this CategoryUpdatesPerCatalog.  # noqa: E501


        :return: The catalog_id of this CategoryUpdatesPerCatalog.  # noqa: E501
        :rtype: int
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """Sets the catalog_id of this CategoryUpdatesPerCatalog.


        :param catalog_id: The catalog_id of this CategoryUpdatesPerCatalog.  # noqa: E501
        :type: int
        """

        self._catalog_id = catalog_id

    @property
    def categories(self):
        """Gets the categories of this CategoryUpdatesPerCatalog.  # noqa: E501


        :return: The categories of this CategoryUpdatesPerCatalog.  # noqa: E501
        :rtype: list[CategoryUpdateInput]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this CategoryUpdatesPerCatalog.


        :param categories: The categories of this CategoryUpdatesPerCatalog.  # noqa: E501
        :type: list[CategoryUpdateInput]
        """

        self._categories = categories

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
        if not isinstance(other, CategoryUpdatesPerCatalog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
