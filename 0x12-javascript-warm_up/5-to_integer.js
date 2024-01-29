#!/usr/bin/node
const arg1 = process.argv[2];;

if (!isNaN(parseInt(arg1))) {
	console.log(`My number is ${arg1}`);
} else {
	console.log("Not a number");
}
