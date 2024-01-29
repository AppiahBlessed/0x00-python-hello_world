#!/usr/bin/node
/**
* This script searches and prints the second biggest integer
*/

const lists = process.argv;
if (process.argv.length <= 3) {
	console.log("0");
} else {
// Getting the maximum number
	let max = lists[2];
	let secondmax = lists[2];
// Looping through the list
	for (let i = 3; i < process.argv.length; i++) {
		const current = lists[i];

		if (current > max) {
			secondmax = max;
			max = current;

		} else if (secondmax < current && current < max) {
			secondmax = current;

		} // End of inner else
	} // End of for lopp

	console.log(secondmax);
} // end of else
