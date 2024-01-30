#!/usr/bin/node
/**
* This script converts numbers into bases
*/
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
