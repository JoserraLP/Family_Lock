




'use strict';

var DeviceMAC = require('../service/DeviceMACService');

module.exports.deleteDeviceMAC = function deleteDeviceMAC (req, res, next) {

    DeviceMAC.deleteDeviceMAC(req.swagger.params, res, next);

};

module.exports.getDeviceMAC = function getDeviceMAC (req, res, next) {

    DeviceMAC.getDeviceMAC(req.swagger.params, res, next);

};

module.exports.postDeviceMAC = function postDeviceMAC (req, res, next) {

    DeviceMAC.postDeviceMAC(req.swagger.params, res, next);

};

module.exports.putDeviceMAC = function putDeviceMAC (req, res, next) {

    DeviceMAC.putDeviceMAC(req.swagger.params, res, next);

};
