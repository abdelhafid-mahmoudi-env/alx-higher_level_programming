#!/usr/bin/node
const request = require('request');
const pathname = 'https://swapi-api.hbtn.io/api/films/';
const slug = process.argv[2];

function printCharacterNamesSequentially(chars, index) {
  request(chars[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chars.length) {
        printCharacterNamesSequentially(chars, index + 1);
      }
    }
  });
}

request(pathname + slug, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacterNamesSequentially(characters, 0);
  }
});
