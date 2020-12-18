#!/bin/bash
# script sends a GET request to the URL, and displays the body of the response., multiple variables must be set
curl "$1" -s -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
