#!/usr/bin/node
// Include the 'request' module to make HTTP requests
const request = require('request');

// Make a HTTP request to the URL provided as the first command line argument
request(process.argv[2], function (error, response, body) {
  // Callback function to handle the HTTP response
  if (!error) {
    // No error during the request, proceed with processing the response body

    // Parse the JSON response body and extract the 'results' array
    const data = JSON.parse(body).results;

    // Use the 'reduce' function to count how many movies have a character with the ID ending in '/18/'
    console.log(data.reduce((count, movie) => {
      // Search for a character within the movie whose ID ends with '/18/'
      const findMovie = movie.characters.find((character) => character.endsWith('/18/'));

      // Increment the count if such a character is found, otherwise return the existing count
      return findMovie ? count + 1 : count;
    }, 0));  // Start counting from 0
  }
});
