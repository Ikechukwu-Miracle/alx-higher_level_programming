#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
# shellcheck disable=SC2046

if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
