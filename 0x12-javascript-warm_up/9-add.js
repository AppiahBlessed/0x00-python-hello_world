#!/usr/bin/node
/**
* This script prinsts the sum of two numbers
*/

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

function add(a, b) {
	a = num1;
	b = num2;
// Checking if arg is a number
	if (isNaN(a) || isNaN(b)) {
		console.log("NaN");
} else {
	console.log(a + b);
}

// Calling the function
add(num1, num2);
