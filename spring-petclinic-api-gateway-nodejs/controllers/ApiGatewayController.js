'use strict';

var utils = require('../utils/writer.js');
var ApiGatewayController = require('../service/ApiGatewayControllerService');

module.exports.getOwnerDetailsUsingGET = function getOwnerDetailsUsingGET (req, res, next) {
  var ownerId = req.swagger.params['ownerId'].value;
  ApiGatewayController.getOwnerDetailsUsingGET(ownerId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
