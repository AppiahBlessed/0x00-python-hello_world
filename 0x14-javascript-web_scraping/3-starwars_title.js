#!/usr/bin/node

// Get variables
const request = require('request');
const movie_id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

// Check number of arguments
if (process.argv.length < 3) {
  console.error('Argument Error: Usage ./3-starwars_title.js [Argument]');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const movieData = JSON.parse(body);
  console.log(movieData.title)
})
