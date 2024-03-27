#!/bin/bash
# This script sends a GET request to a specified URL and displays the body of the response
curl "$1" -sX GET -H "X-School-User-Id:98"
