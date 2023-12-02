#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.

Usage: ./1-hbtn_header.py <URL>
"""
from urllib.request import Request, urlopen
import sys


if __name__ == "__main__":
    req = Request(sys.argv[1])
    
    with urlopen(req) as response:
        print(dict(response.headers).get('X-Request-Id'))
