#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response (only for 200 status code)
curl -sL -w "%{http_code}" "$1" -o /tmp/body_response.txt && { [ $(cat /tmp/body_response.txt) -eq 200 ] && cat /tmp/body_response.txt || echo ""; } | sed '$d'
