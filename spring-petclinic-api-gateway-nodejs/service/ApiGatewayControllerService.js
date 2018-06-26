'use strict';


/**
 * getOwnerDetails
 *
 * ownerId Integer ownerId
 * returns OwnerDetails
 **/
exports.getOwnerDetailsUsingGET = function(ownerId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

