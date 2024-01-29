#!/usr/bin/node
/**
* This script records the occurrence of an item in a list.
*/

exports.nbOccurences = function (list, searchElement) {
let count = 0;
// Loop to find element
	for (let i = 0; i <= list.length; list++){
		if (searchElement === list[i]);
			count++;
	}
return (count);
