'use strict';

var utils = require('../utils/writer.js');
var VetResource = require('../service/VetResourceService');

module.exports.showResourcesVetListUsingGET = function showResourcesVetListUsingGET (req, res, next) {
  VetResource.showResourcesVetListUsingGET()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
