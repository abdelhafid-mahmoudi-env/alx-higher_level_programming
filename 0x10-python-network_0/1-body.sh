#!/bin/bash
curl -sL -w "%{http_code}" -o /dev/null "$1" | { [ $(tail -n1) -eq 200 ] && curl -sL "$1" || echo ""; }
