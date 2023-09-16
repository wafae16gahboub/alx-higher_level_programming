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
  rotate () {
    let swap = this.height;
    this.height = this.width;
    this.width = swap;
  }
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
const rectangle = Rectangle;
module.exports = rectangle;
