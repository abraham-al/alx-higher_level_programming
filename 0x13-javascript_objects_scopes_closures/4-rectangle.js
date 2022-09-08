#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) return;
    this.width = w;
    this.height = h;
  }

  print () {
    let wid = '';
    for (let i = 0; i < this.width; i++) {
      wid += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(wid);
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
