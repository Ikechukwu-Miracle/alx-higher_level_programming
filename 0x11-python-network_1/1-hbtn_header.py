#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""
from urllib.request import Request, urlopen
import sys


req = Request(sys.argv[1])

with urlopen(req) as response:
    x_req_id = dict(response.headers).get('X-Request-Id')
    if x_req_id:
        print(x_req_id)
