'use strict';


/**
 * showResourcesVetList
 *
 * returns List
 **/
exports.showResourcesVetListUsingGET = function() {
  return new Promise(function(resolve, reject) {
    var examples = {};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

