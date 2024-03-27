#!/bin/bash

# Sends a POST request with email and subject parameters to the provided URL
curl -sX POST $1 -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
