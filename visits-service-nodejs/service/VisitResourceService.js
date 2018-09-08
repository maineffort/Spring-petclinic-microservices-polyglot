'use strict';


/**
 * create
 *
 * visit Visit visit
 * petId Integer petId
 * no response value expected for this operation
 **/
exports.createUsingPOST = function(visit,petId) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * visits
 *
 * petId Integer petId
 * returns List
 **/
exports.visitsUsingGET = function(petId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

