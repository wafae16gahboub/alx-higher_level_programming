#!/usr/bin/node
let counter = 0;
module.exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter++;
};
