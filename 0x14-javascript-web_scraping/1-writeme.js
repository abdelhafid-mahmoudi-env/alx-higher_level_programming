#!/usr/bin/node
// Import the 'fs' module to interact with the file system
const fs = require('fs');

// Use writeFile function to write data to a file specified by a command line argument
// process.argv[2] is the file name, process.argv[3] is the data to write
fs.writeFile(process.argv[2], process.argv[3], error => {
  // Callback function to handle errors that may occur during the file writing process
  if (error) {
    // If an error occurs, log it to the console
    console.log(error);
  }
});
