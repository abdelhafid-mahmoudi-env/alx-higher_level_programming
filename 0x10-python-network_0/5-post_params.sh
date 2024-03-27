#!/bin/bash
# Takes to send a POST request with specific data and display the response body
curl "$1" -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD"
