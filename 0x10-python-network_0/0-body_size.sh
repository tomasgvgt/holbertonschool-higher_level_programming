#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL (Using curl)
# and displays the size of the body of the response
# The size must be displayed in bytes
curl "$1" -s | wc -c
