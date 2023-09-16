#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  let count = list.reduce(function (num, value) {
    return num + (value === searchElement);
  }, 0);
  return count;
};
