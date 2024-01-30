#!/usr/bin/node
/**
* This script logs a count to function calls
*/

let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
