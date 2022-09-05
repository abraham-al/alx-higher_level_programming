#!/usr/bin/node
function Big (arr) {
    let maxnum = 0; let result = 0;
    for (const value of arr) {
      const nr = Number(value);
      if (nr > maxnum) {
        [result, maxnum] = [maxnum, nr];
      } else if (nr < maxnum && nr > result) {
        result = nr;
      }
    }
    return (result);
  }
  console.log(Big(process.argv));
