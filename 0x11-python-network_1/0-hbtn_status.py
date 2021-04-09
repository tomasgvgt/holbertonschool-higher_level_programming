#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as resp:
        data = resp.read()
    html = data.decode("UTF-8")
    obj_type = type(data)
    print("Body response:")
    print("\t- type: {}".format(obj_type))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(html))
