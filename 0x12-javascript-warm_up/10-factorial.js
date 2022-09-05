#!/usr/bin/node
function factorial (n) {
    let result = 1;
    for (let i = 1; i <= n; i++) {
      result *= i;
    }
    return (result);
  }
  console.log(factorial(parseInt(process.argv[2])));
