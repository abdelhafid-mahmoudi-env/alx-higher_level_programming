#!/usr/bin/node
// Include the file system module from Node.js
const fs = require('fs');

// Read a file whose name is provided as the second command-line argument
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Output any errors to the console or the content of the file if there are no errors
  console.log(error || content);
});
