#!/usr/bin/node

const a = process.argv;
if (isNaN(a[2]) || a[2] == null) {
  console.log('Not a number');
} else {
  console.log('My number: ' + a[2]);
}
