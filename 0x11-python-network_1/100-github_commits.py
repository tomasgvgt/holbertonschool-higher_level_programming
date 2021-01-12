#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the Github API,
here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
import sys


if __name__ == "__main__":
    resp = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]
    ))
    json_obj = resp.json()
    for i in json_obj[0:10]:
        print("{}: {}".format(i.get('sha'), i.get('commit').get(
            'author').get('name')))
