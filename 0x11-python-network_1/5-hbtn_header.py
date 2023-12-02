#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    response = requests.get(url)
    x_req_id = response.headers.get('X-request-id')
    if x_req_id:
        print(x_req_id)
