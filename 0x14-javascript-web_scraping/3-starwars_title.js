#!/usr/bin/node
// Import the 'request' library to handle HTTP requests
const request = require('request');

// Retrieve the episode index from command line arguments
const filmIndex = process.argv[2];
// Set the base URL for the Star Wars films API endpoint
const SWAPI_FILMS_URL = 'https://swapi-api.hbtn.io/api/films/';

// Send a GET request to the Star Wars API with the film index to retrieve specific film data
request(SWAPI_FILMS_URL + filmIndex, function (error, httpResponse, responseBody) {
  if (error) {
    // Log any errors encountered during the HTTP request
    console.log(error);
  } else if (httpResponse.statusCode === 200) {
    // Convert the JSON response body to an object if the request was successful
    const filmData = JSON.parse(responseBody);
    // Print the title of the film
    console.log(filmData.title);
  } else {
    // Log the HTTP status code if it's not 200 (OK)
    console.log('Error code: ' + httpResponse.statusCode);
  }
});
