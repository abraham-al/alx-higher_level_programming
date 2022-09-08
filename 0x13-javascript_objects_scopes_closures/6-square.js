#!/usr/bin/node
const SquareModel = require('./5-square.js');

module.exports = class Square extends SquareModel {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined || c == null || c.length <= 0) {
      this.print();
    } else {
      let wid = '';
      for (let i = 0; i < this.width; i++) {
        wid += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(wid);
      }
    }
  }
};
