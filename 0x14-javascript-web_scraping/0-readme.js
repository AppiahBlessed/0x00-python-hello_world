#!/usr/bin/node

const fs = require('fs');
file_path = process.argv[2];

// Check if argument was provided
if (process.argv.length < 3) {
  console.error('Argument Error: Usage ./0-readme.js [Argument]');
  process.exit(1);
}
// Reading file
fs.readFile(file_path, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
