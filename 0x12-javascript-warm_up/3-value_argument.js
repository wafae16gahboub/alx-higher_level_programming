#!/usr/bin/node
if (process.argv[2] == null) {
  console.log('No argument');
} else if (process.argv[2]) {
  console.log(process.argv[2]);
}
