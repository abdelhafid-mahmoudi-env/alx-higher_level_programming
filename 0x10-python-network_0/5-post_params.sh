#!/bin/bash
# Takes to send a POST request with specific data and display the response body
curl "$1" -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
