#!/usr/bin/node
const dict = require('./101-data').dict;
const di = {};
for (const key in dict) {
  if (di[dict[key]] === undefined) {
    di[dict[key]] = [];
  }
  di[dict[key]].push(key);
}

console.log(di);
