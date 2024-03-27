#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me causing the server to respond with "You got me!"
curl -sL -X PUT -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me -d "user_id=98"
