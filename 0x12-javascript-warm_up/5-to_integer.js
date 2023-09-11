#!/usr/bin/node

/*
 * This script is meant to
 */

// Get the number
const arg3 = process.argv[2];

// Attempt to convert arg to in
const num = parseInt(arg3)

// Checks if arguement is not a number an uses '!' to negate

if (!isNaN(num)) {
  console.log('My number is: ' + num);
} else {
  console.log('Not a number');
}
