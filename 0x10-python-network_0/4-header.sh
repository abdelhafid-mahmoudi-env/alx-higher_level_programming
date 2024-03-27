#!/bin/bash
# This script sends a GET request to a specified URL and displays the body of the response.
# It includes a header 'X-School-User-Id' with the value '98' in the request.
# Usage: ./4-header.sh <URL>
#   <URL>: The URL to which the GET request will be sen
curl -sH "X-School-User-Id: 98" "$1"
