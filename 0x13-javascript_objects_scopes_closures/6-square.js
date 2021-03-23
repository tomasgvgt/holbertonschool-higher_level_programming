#!/usr/bin/node
const Squared = require('./5-square');
// Square class that inherits from Square
class Square extends Squared {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let i;
      let ctring = '';
      for (i = 0; i < this.width; i++) {
        ctring += 'C';
      }
      for (i = 0; i < this.height; i++) {
        console.log(ctring);
      }
    }
  }
}
module.exports = Square;
