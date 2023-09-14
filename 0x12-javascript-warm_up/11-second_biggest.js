#!/usr/bin/node

/*
 * This script finds the second biggest integer among command-line arguments.
 */

const args = process.argv.slice(2).map(Number); // Convert arguments to integers
const sortedArgs = args.sort((a, b) => b - a); // Sort in descending order

if (sortedArgs.length < 2) {
  console.log(0); // Not enough arguments
} else {
  console.log(sortedArgs[1]); // Print the second biggest integer
}
