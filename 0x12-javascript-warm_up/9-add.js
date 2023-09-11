#!/usr/bin/node

/*
 * This file script adds two integers
 */

// Function that adds tw numbers
function add (a, b) {
  return a + b;
}

// Convert list items into integer
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
console.log(add(a, b));
