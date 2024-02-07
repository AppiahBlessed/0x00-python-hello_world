#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if both URL and file path are provided as command line arguments
if (process.argv.length < 4) {
  console.error('Please provide both the URL and the file path as arguments.');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make a request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
    return;
  }

  // Check if the response status code is 200 (OK)
  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    return;
  }

  // Write the body content to the specified file
  fs.writeFileSync(filePath, body, 'utf8');

  console.log(`Webpage content has been successfully written to: ${filePath}`);
});
