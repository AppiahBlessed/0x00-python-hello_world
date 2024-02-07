#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided as a command line argument
if (process.argv.length < 3) {
  console.error('Please provide the API URL as an argument.');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = 18;

// Make a request to the SWAPI
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
    return;
  }

  // Check if the response status code is 200 (OK)
  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    return;
  }

  // Parse the JSON response body
  const filmsData = JSON.parse(body);

  // Filter films where Wedge Antilles is present
  const filmsWithWedge = filmsData.results.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  // Print the number of films with Wedge Antilles
  console.log(filmsWithWedge.length);
});

