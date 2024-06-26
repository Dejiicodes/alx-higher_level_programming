#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/' + process.argv[2];

request(url, function (err, response, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const characters = resp.characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
