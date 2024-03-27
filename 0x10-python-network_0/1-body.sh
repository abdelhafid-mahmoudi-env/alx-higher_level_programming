#!/bin/bash
# Description: Sends a GET request to a URL and displays the body of the response if the status code is 200.
# Usage: ./1-body.sh <URL>
# Arguments:
#   <URL>: The URL to send the GET request to.

# Send a GET request to the provided URL and store the response body in a variable
response_body=$(curl -sL -w "%{http_code}" -o /dev/null "$1")

# Extract the HTTP status code from the response
http_status=$(echo "$response_body" | tail -n1)

# Check if the HTTP status code is 200
curl -sL "$1"
