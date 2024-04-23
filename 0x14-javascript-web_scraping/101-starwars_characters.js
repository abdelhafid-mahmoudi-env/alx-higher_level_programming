#!/usr/bin/node
const request = require('request');
const pathname = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(pathname, function (error, response, body) {
  if (!error) {
    const chars = JSON.parse(body).characters;
    _recursive_print_chars(chars, 0);
  }
});

function _recursive_print_chars(chars, index) {
  request(chars[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chars.length) {
        _recursive_print_chars(chars, index + 1);
      }
    }
  });
}
