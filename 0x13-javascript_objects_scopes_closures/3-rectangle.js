#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (!Number.isInteger(w) || !Number.isInteger(h)) {
      return;
    }
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
const rectangle = Rectangle;
module.exports = rectangle;
