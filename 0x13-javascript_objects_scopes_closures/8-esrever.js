#!/usr/bin/node
module.exports.esrever = function (list) {
  let reverse = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverse.push(list[i]);
  }
  return reverse;
};
