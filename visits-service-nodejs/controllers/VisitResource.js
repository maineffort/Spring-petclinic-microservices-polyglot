'use strict';

var utils = require('../utils/writer.js');
var VisitResource = require('../service/VisitResourceService');

module.exports.createUsingPOST = function createUsingPOST (req, res, next) {
  var visit = req.swagger.params['visit'].value;
  var petId = req.swagger.params['petId'].value;
  VisitResource.createUsingPOST(visit,petId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.visitsUsingGET = function visitsUsingGET (req, res, next) {
  var petId = req.swagger.params['petId'].value;
  VisitResource.visitsUsingGET(petId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
