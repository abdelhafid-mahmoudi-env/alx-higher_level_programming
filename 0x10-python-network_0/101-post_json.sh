#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument
# It sends the contents of a file passed as the second argument as the body of the request

# Check if the file exists
if [ ! -f "$2" ]; then
    echo "File not found"
    exit 1
fi

# Check if the file contains valid JSON
if ! jq . "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 2
fi

# Send the POST request with curl and display the body of the response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
