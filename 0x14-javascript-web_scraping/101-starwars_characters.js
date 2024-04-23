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

// Function to fetch characters recursively
async function fetchCharactersRecursively(urls, characters = []) {
  if (urls.length === 0) {
    return characters;
  }

  const [url, ...remainingUrls] = urls;
  try {
    const characterData = await fetchMovieData(url);
    characters.push(characterData.name);
    return fetchCharactersRecursively(remainingUrls, characters);
  } catch (error) {
    console.error(error);
  }
}

// Print characters in the right order
async function printCharactersInOrder(movieId) {
  try {
    const movieData = await fetchMovieData(apiUrl);
    const charactersUrls = movieData.characters;
    const characters = await fetchCharactersRecursively(charactersUrls);
    characters.forEach(character => console.log(character));
  } catch (error) {
    console.error(error);
  }
}

printCharactersInOrder(movieId);
