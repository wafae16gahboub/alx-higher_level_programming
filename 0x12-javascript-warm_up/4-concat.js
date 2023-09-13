#!/usr/bin/node

if (process.argv[2] == null) {
  console.log('undefined is undefined');
} else if (process.argv[3]) {
  console.log(process.argv[2]  + ' is ' + process.argv[3]);
} else {
  console.log(process.argv[2] + ' is undefined');
}
