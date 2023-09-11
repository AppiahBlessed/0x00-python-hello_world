#!/usr/bin/node
/*
 * File script prints line depending on cmd args passed
 */

// Get the lenght of arguments passed
const arglen = process.argv.length;

// If no args
if (arglen < 3) {
  console.log('No argument');
} else if (arglen === 3) {
  // If one argument is passed
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
