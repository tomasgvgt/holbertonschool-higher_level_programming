#!/usr/bin/node
const Rectangle = require('./4-rectangle');
// Square class that inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    // super calls the contrusctor from Rectangle, to be used in Square
    super(size, size);
  }
}
module.exports = Square;
