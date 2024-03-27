#!/bin/bash
# Description: Sends a GET request to a URL and displays the body of the response if the status code is 200.
# Usage: ./1-body.sh <URL>
# Arguments:
#   <URL>: The URL to send the GET request to.

# Send a GET request to the provided URL, follow redirects, and suppress progress output
response=$(curl -sX GET "$1" -L)

# Display the body of the response
echo "$response"
