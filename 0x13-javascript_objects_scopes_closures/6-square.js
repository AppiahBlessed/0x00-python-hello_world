#!/usr/bin/node

const square = require('./5-square.js');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (C) {
    if (C === undefined) {
      C = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += C;
      }
      console.log(s);
    }
  }
}
module.exports = Square;
