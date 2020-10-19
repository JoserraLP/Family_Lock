# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.device_mac import DeviceMAC  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDeviceMACController(BaseTestCase):
    """DeviceMACController integration test stubs"""

    def test_delete_device_mac(self):
        """Test case for delete_device_mac

        Delete the device MAC.
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '/device_MAC',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_device_mac(self):
        """Test case for get_device_mac

        Return all the devices MACs
        """
        query_string = [('device_mac', 'device_mac_example')]
        response = self.client.open(
            '/device_MAC',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_device_mac(self):
        """Test case for post_device_mac

        Add a new Device MAC.
        """
        device_mac = DeviceMAC()
        response = self.client.open(
            '/device_MAC',
            method='POST',
            data=json.dumps(device_mac),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_device_mac(self):
        """Test case for put_device_mac

        Update a device MAC
        """
        device_mac = DeviceMAC()
        response = self.client.open(
            '/device_MAC',
            method='PUT',
            data=json.dumps(device_mac),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
