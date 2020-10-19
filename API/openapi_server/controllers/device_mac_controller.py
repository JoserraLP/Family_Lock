import connexion
import six
import json

from openapi_server.models.device_mac import DeviceMAC  # noqa: E501
from openapi_server import util
from ..__main__ import get_db

def delete_device_info(tx, device_mac):
    try:
        query = "MATCH (a:Person) WHERE $person_mac IN a.person_mac DETACH DELETE a"

        tx.run(query, person_mac=device_mac)

        return "Deleted", 200
    
    except Exception as e:
        return e

def delete_device_mac(device_mac):  # noqa: E501
    """Delete the device MAC.

    Delete the selected Device MAC. # noqa: E501

    :param type: Device MAC
    :type type: str

    :rtype: str
    """
    
    with get_db().session() as session:
        return session.write_transaction(delete_device_info, device_mac)

def get_device_info(tx, device_mac):

    devices = []

    if device_mac is None:
        query = "MATCH (a:Person) RETURN a AS person"
        results = tx.run(query)
    else:
        query = "MATCH (a:Person) WHERE $person_mac IN a.person_mac RETURN a AS person"
        results = tx.run(query, person_mac=device_mac)

    for record in results:
        dict_val = {}
        for k,v in record['person'].items():
            dict_val[k] = v
        devices.append(dict_val)

    return devices

def get_device_mac(device_mac=None):  # noqa: E501
    """Return all the devices MACs

    Return all the MAC devices # noqa: E501

    :param device_mac: Device MAC
    :type device_mac: str

    :rtype: str
    """
    try:
        with get_db().session() as session:
            return session.read_transaction(get_device_info, device_mac)

    except Exception as e:
        print(e)
        return "Failure", 500

def create_nearby_person(tx, device_mac):

    query = "CREATE (a:Person {person_mac: $person_mac, person_name: $person_name, person_phone_number: $person_phone_number, \
            notification: $notification}) RETURN a.person_name AS person"

    tx.run(query, person_mac=device_mac.person_mac, person_name=device_mac.person_name, 
    person_phone_number=device_mac.person_phone_number, notification=device_mac.notification)

    if device_mac.dest_mac != "":        
        tx.run("MATCH (a:Person),(b:Person)"
                " WHERE $person_mac IN a.person_mac AND $dest_mac IN b.person_mac"
                " CREATE (b)-[r:close_to]->(a)"
                " RETURN type(r)", person_mac=device_mac.person_mac[0], dest_mac=device_mac.dest_mac)


def post_device_mac(device_mac):  # noqa: E501
    """Add a new Device MAC.

    Addition of a new device MAC # noqa: E501

    :param device_mac: 
    :type device_mac: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        device_mac = DeviceMAC.from_dict(connexion.request.get_json())  # noqa: E501
    
    with get_db().session() as session:
        return session.write_transaction(create_nearby_person, device_mac)
    


def put_device_mac(new_device_mac):  # noqa: E501
    """Update a device MAC

    Update a device MAC # noqa: E501

    :param new_device_mac: 
    :type new_device_mac: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        new_device_mac = DeviceMAC.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
