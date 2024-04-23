#!/usr/bin/node
// Import the 'request' module to make HTTP requests
const request = require('request');

// Send a GET request to the URL specified in the first command line argument
request.get(process.argv[2])
  // Listen for the 'response' event to be emitted
  .on('response', function (response) {
    // When the response is received, log the status code to the console
    console.log(`code: ${response.statusCode}`);
  });
