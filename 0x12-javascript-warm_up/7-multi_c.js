#!/usr/bin/node

/*
 * This file scrip prints x times of 'C'
 */

let i;

// Check if input is not a number...
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else { // Otherwise, proceed
  for (i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
