#!/usr/bin/node
class Rectangle {
  // The constructor initializes with and height to w and h
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
