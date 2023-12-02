#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


req = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(req) as response:
    body = response.read()
    utf8_content = body.decode('utf-8')

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", utf8_content)
