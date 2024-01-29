#!/usr/bin/node
/**
* This script calculates the factrial of a number
*/

// Get integer first and cast it if neccessary
const num == parseInt(process.argv[2]);

// Function to compute the factorial

function factorial(n) {
	if (n === 1 || n === 0) {
		return (1);
	} else {
		return (n * factorial(n - 1));
	}
}

// Prints the result of the factorial
console.log(factorial (num));
