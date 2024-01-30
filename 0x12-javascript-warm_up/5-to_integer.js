#!/usr/bin/node
const arg1 = process.argv[2];

if (!isNaN(parseFloat(arg1))) {
  iconst value = parseInt(arg1);
  console.log(`My number: ${value}`);
} else {
  console.log('Not a number');
}
