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
};
const rectangle = Rectangle;
module.exports = rectangle;
