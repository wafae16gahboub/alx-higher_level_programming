#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (c === undefined || c === '') {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
const square = Square;
module.exports = square;
