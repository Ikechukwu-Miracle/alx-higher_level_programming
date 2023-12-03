#!/usr/bin/python3
""" takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    token = argv[2]

    auth = HTTPBasicAuth(username, token)

    response = requests.get(url, auth=auth)
    print(response.json().get("id"))