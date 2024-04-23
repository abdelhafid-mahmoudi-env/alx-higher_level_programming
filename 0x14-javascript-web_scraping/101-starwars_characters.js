#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to fetch movie data
function fetchMovieData(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Unexpected status code: ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Function to fetch characters in the right order
async function fetchCharactersInOrder(movieId) {
  try {
    const movieData = await fetchMovieData(apiUrl);
    const charactersUrl = movieData.characters;
    const characters = await Promise.all(charactersUrl.map(url => fetchMovieData(url)));
    return characters.map(character => character.name);
  } catch (error) {
    console.error(error);
  }
}

// Print characters in the right order
async function printCharactersInOrder(movieId) {
  const characters = await fetchCharactersInOrder(movieId);
  characters.forEach(character => console.log(character));
}

printCharactersInOrder(movieId);
