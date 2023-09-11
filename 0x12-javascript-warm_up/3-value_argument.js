#!/usr/bin/node

/*
 * This file script prints messages for each argument condition
 */

if (process.argv[2] === undefined) { // If there is no argument
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
