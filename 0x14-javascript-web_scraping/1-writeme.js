#!/usr/bin/node

const fs = require('fs');
const file_path = process.argv[2];
const string = process.argv[3];

if (process.argv.length < 4) {
  console.error('Argument Error: Usage ./0-readme.js [Argument]');
  process.exit(1);
}

fs.writeFile(file_path, string, 'utf8', (err) => {
  if (err) {
    console.log(err);
    return;
  }
})
