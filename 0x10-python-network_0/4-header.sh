#!/bin/bash
# This script sends a GET request to a specified URL and displays the body of the response.
# It includes a header 'X-School-User-Id' with the value '98' in the request.
# Usage: ./4-header.sh <URL>
#   <URL>: The URL to which the GET request will be sent

# Check if an argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send GET request with the specified header and display the response body
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id:98"
