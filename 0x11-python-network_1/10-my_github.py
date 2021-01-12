#!/usr/bin/python3
"""
script that takes your Github credentials
(username and password) and uses the Github API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    u_p = (sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=u_p)
    json_obj = response.json()
    print(json_obj.get('id'))
