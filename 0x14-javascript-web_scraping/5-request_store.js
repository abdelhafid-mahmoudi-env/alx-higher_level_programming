#!/usr/bin/node
// Set the environment to use Node.js

const fs = require('fs');
const request = require('request');
// Make an HTTP request to the URL provided
request(process.argv[2])
  .pipe(fs.createWriteStream(process.argv[3]));
