#!/usr/bin/node

// Get variables
const request = require('request');
const url = process.argv[2];

// Check number of arguments
if (process.argv.length < 3) {
  console.error('Argument Error: Usage ./0-readme.js [Argument]');
  process.exit(1);
}

// Go to web url and print status code
request(url, (err, response) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(response.statusCode);
})
