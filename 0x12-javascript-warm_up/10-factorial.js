#!/usr/bin/node

/*
 * This file script finds the factorial of a given number
 */

// Function that adds tw numbers
function facto (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * facto(n - 1);
  }
}

const num = parseInt(process.argv[2]);

// If not number return 1
if (isNaN(num)) {
  console.log('1');
} else {
  console.log(facto(num));
}
