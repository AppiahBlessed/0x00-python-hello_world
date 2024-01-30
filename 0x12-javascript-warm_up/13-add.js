#!/usr/bin/node
/**
 * This script defines a function 'add' to return the addition of two integers
 */

const add = (a, b) => a + b;

// Example usage
const result = add(5, 3);
console.log(result); // Output: 8

// Export the function to make it visible from outside
module.exports = add;
