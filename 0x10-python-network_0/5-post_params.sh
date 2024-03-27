#!/bin/bash
# Declare email and subject variables
email="test@gmail.com"
subject="I will always be here for PLD"
# Sends a POST request with email and subject parameters to the provided URL
curl "$1" -sX POST -d "email=$email&subject=$subject"
