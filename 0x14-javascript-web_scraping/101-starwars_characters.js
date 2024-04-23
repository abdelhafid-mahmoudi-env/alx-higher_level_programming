#!/usr/bin/node

const request = require('request');

const pathname = `https://swapi-api.alx-tools.com/api/films/`;
const slug = process.argv[2];

request(pathname + slug, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const res = JSON.parse(body);
    const chars = res.characters;
    const recursive = (index) => {
      if (index >= chars.length) {
        return;
      }
      request(chars[index], (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const char = JSON.parse(body);
          console.log(char.name);
          recursive(index + 1);
        }
      });
    };
    recursive(0);
  }
});
