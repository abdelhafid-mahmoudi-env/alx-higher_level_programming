#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body).results;
    console.log(data.reduce((count, movie) => {
      const findMovie = movie.characters.find((character) => character.endsWith('/18/'));
      return findMovie ? count + 1 : count;
    }, 0));
  }
});
