#!/bin/bash
# Takes in a URL as an argument and sends a POST request with specific data
# Usage: ./5-post_params.sh <URL>
#   <URL>: The URL to which the POST request will be sent

# Check if the script is provided with exactly one argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a POST request with specific data and display the response body
curl "$1" -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
