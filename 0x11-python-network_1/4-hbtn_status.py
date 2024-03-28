#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""

import requests


def fetch_status():
    """
    Fetches the status from https://alx-intranet.hbtn.io/status
    and prints the body of the response.
    """
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    data = response.text

    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))


if __name__ == "__main__":
    fetch_status()
