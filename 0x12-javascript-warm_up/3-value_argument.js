#!/usr/bin/node
/**
* This script prinst the arguments passed
*/

const lists = process.argv;
if (lists[1] === undefined) {
	console.log("No argument");
} else {
	console.log(lists[2]);
}
