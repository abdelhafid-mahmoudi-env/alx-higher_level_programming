#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
This script demonstrates the usage of the urllib package to make a request
and print the body of the response in a specific format.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    # Use a with statement to ensure proper acquisition
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
