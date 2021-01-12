#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
from urllib import request
from urllib import error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode())
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
