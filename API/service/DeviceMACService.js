'use strict';


/**
 * Delete the device MAC.
 * Delete the selected Device MAC.
 *
 * type String Device MAC
 * returns String
 **/
module.exports.deleteDeviceMAC = function(req, res, next) {
    //Parameters
    console.log(req);
    res.send({
        message: 'This is the mockup controller for deleteDeviceMAC'
    });
};


/**
 * Return all the devices MACs
 * Return all the MAC devices
 *
 * deviceMAC String Device MAC (optional)
 * returns String
 **/
module.exports.getDeviceMAC = function(req, res, next) {
    //Parameters
    console.log(req);
    res.send({
        message: 'This is the mockup controller for getDeviceMAC'
    });
};


/**
 * Add a new Device MAC.
 * Addition of a new device MAC
 *
 * deviceMAC object
 * returns String
 **/
module.exports.postDeviceMAC = function(req, res, next) {
    //Parameters
    console.log(req);
    res.send({
        message: 'This is the mockup controller for postDeviceMAC'
    });
};


/**
 * Update a device MAC
 * Update a device MAC
 *
 * deviceMAC object (optional)
 * returns String
 **/
module.exports.putDeviceMAC = function(req, res, next) {
    //Parameters
    console.log(req);
    res.send({
        message: 'This is the mockup controller for putDeviceMAC'
    });
};




