# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, person_id=None, old_mac=None, new_mac=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI

        :param person_id: The person_id of this InlineObject.  # noqa: E501
        :type person_id: str
        :param old_mac: The old_mac of this InlineObject.  # noqa: E501
        :type old_mac: str
        :param new_mac: The new_mac of this InlineObject.  # noqa: E501
        :type new_mac: str
        """
        self.openapi_types = {
            'person_id': str,
            'old_mac': str,
            'new_mac': str
        }

        self.attribute_map = {
            'person_id': 'person_id',
            'old_mac': 'old_MAC',
            'new_mac': 'new_MAC'
        }

        self._person_id = person_id
        self._old_mac = old_mac
        self._new_mac = new_mac

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object of this InlineObject.  # noqa: E501
        :rtype: InlineObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def person_id(self):
        """Gets the person_id of this InlineObject.


        :return: The person_id of this InlineObject.
        :rtype: str
        """
        return self._person_id

    @person_id.setter
    def person_id(self, person_id):
        """Sets the person_id of this InlineObject.


        :param person_id: The person_id of this InlineObject.
        :type person_id: str
        """

        self._person_id = person_id

    @property
    def old_mac(self):
        """Gets the old_mac of this InlineObject.


        :return: The old_mac of this InlineObject.
        :rtype: str
        """
        return self._old_mac

    @old_mac.setter
    def old_mac(self, old_mac):
        """Sets the old_mac of this InlineObject.


        :param old_mac: The old_mac of this InlineObject.
        :type old_mac: str
        """

        self._old_mac = old_mac

    @property
    def new_mac(self):
        """Gets the new_mac of this InlineObject.


        :return: The new_mac of this InlineObject.
        :rtype: str
        """
        return self._new_mac

    @new_mac.setter
    def new_mac(self, new_mac):
        """Sets the new_mac of this InlineObject.


        :param new_mac: The new_mac of this InlineObject.
        :type new_mac: str
        """

        self._new_mac = new_mac
