#!/usr/bin/node
/**
* This script calculates the factrial of a number
*/

const num = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n)) {
    return (1);
} else {
    return (n * factorial(n - 1));
  }
}
console.log(factorial (num));
