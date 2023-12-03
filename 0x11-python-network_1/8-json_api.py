#!/usr/bin/python3
""" takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        param = argv[1]
    else:
        param = ""

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': param}

    try:
        response = requests.post(url, data=data)
        json_res = response.json()

        if json_res:
            user_id = json_res.get('id')
            user_name = json_res.get('name')
            print("[{}] {}".format(user_id, user_name))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
