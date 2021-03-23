#!/usr/bin/node
// Converts a number from base 10 to another base pased as argument
exports.converter = function (base) {
  return function (num) {
    // .toString method converts a number to a given base
    return num.toString(base);
  };
};
