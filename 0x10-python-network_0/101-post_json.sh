#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file in the body
if [ -f "$2" ]; then
    curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
    echo ""
else
    echo "Not a valid JSON"
fi
