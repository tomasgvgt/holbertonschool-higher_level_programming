#!/usr/local/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let xtring = '';
    for (i = 0; i < this.width; i++) {
      xtring += 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(xtring);
    }
  }
}
module.exports = Rectangle;
