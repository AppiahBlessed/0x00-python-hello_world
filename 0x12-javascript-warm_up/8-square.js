#!/usr/bin/node

/*
 * This file script prints x times a squareof 'x'
 */

let i;

// Check if input is not a number...
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else { // Otherwise, proceed
  for (i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
