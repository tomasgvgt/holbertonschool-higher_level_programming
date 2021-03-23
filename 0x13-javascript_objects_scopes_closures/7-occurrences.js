#!/usr/bin/node

// Returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let i;
  let count = 0;
  for (i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      count++;
    }
  }
  return count;
};
