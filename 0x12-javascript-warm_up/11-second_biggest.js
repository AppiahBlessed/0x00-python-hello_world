#!/usr/bin/node
/**
 * This script searches and prints the second biggest integer
 */

const lists = process.argv;

if (process.argv.length <= 3) {
  console.log("0");
} else {
  let max = parseInt(lists[2]);
  let secondMax = parseInt(lists[2]);

  for (let i = 3; i < process.argv.length; i++) {
    const current = parseInt(lists[i]);

    if (current > max) {
      secondMax = max;
      max = current;
    } else if (current > secondMax && current < max) {
      secondMax = current;
    }
  }

  console.log(secondMax);
}
