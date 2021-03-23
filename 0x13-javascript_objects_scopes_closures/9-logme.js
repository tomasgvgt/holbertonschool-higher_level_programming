#!/usr/local/bin/node
let printed = 0;
// Prints the number of argument already printed
// and the new argument value
exports.logMe = function (item) {
  console.log(printed + ': ' + item);
  printed++;
};
