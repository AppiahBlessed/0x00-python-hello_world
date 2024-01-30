#!/usr/bin/node
/**
* script that prints x times “C is fun”
*/
const num = process.argv[2];

if (process.argv.length !== 3) {
	console.log("Missing number of occurrences");
}

if (num >= 0) {
	for (let i = 0; i < num; i++) {
		console.log("C is fun");
//} else {
//	console.log("");
}
}
