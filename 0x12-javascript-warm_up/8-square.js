#!/usr/bin/node
/**
* This script prints a square
*/

const num = parseInt(process.argv[2]);

if (isNaN(num) || process.argv[2]  === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
