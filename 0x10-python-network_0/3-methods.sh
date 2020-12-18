#!/bin/bash
# script that takes in a URL, and displays all HTTP methods the server will accept.
curl --head "$1" | grep -e 'Allow' | cut -d ":" -f 2 | cut -d " " -f 2-
