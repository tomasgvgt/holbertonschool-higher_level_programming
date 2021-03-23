#!/usr/bin/node
const Squared = require('./5-square');
// Square class that inherits from Square
class Square extends Squared {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    } else {
      c = 'C';
    }
    let i;
    let ctring = '';
    for (i = 0; i < this.width; i++) {
      ctring += c;
    }
    for (i = 0; i < this.height; i++) {
      console.log(ctring);
    }
  }
}
module.exports = Square;
