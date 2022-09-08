#!/usr/bin/node
const fs = require('fs');
const one = process.argv[2];
const two = process.argv[3];
const three = process.argv[4];
const A = fs.readFileSync(one, 'utf8');
const B = fs.readFileSync(two, 'utf-8');
fs.writeFileSync(three, A + B);
