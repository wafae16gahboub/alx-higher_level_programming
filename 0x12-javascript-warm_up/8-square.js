#!/usr/bin/node
let a;
a = process.argv[2];
if (isNaN(a) || a === null) {
  console.log('Missing size');
} else {
  let inc ;
  for (let i = 0; i < a; i++) {
    inc = "";
    for (let j = 0; j < a; j++) {
      inc += "X";
    }

    console.log(inc);
  }
}
