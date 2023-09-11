#!/usr/bin/node

/*
 * This script is meant to
 */

// Get the number
const arg3 = process.argv[2];

// Checks if arguement is not a number an uses '!' to negate

if (!isNaN(arg3)) {
  console.log('My number is: ' + arg3);
} else {
  console.log('Not a number');
}
