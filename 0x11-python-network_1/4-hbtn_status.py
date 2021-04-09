#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    resp = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(type(resp.text), resp.text))
