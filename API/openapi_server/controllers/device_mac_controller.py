import connexion
import six

from openapi_server.models.device_mac import DeviceMAC  # noqa: E501
from openapi_server.models.inline_object import InlineObject  # noqa: E501
from openapi_server import util


def delete_device_mac(type):  # noqa: E501
    """Delete the device MAC.

    Delete the selected Device MAC. # noqa: E501

    :param type: Device MAC
    :type type: str

    :rtype: str
    """
    return 'do some magic!'


def get_device_mac(device_mac=None):  # noqa: E501
    """Return all the devices MACs

    Return all the MAC devices # noqa: E501

    :param device_mac: Device MAC
    :type device_mac: str

    :rtype: str
    """
    return 'do some magic!'


def post_device_mac(device_macList):  # noqa: E501
    """Add a new Device MAC.

    Addition of a new device MAC # noqa: E501

    :param device_macList: 
    :type device_macList: list | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        device_macList = [DeviceMAC.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def put_device_mac(inline_object=None):  # noqa: E501
    """Update a device MAC

    Update a device MAC # noqa: E501

    :param inline_object: 
    :type inline_object: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        inline_object = InlineObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
