#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    data = {}
    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
    else:
        data['q'] = ""
    response = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        json_obj = response.json()
        if json_obj:
            print("[{}] {}".format(json_obj.get('id'), json_obj.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
