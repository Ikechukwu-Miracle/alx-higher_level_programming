#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


if len(sys.argv) != 2:
    sys.exit(1)

req = sys.argv[1]

with urllib.request.urlopen(req) as response:
    x_req_id = response.headers.get('X-Request-Id')
    if x_req_id:
        print(x_req_id)
