#!/usr/bin/bash

#  Bash script that takes in a URL, sends a POST request to the passed URL,
# and displays the body of the response
# A variable email must be sent with the value hr@holbertonschool.com
# A variable subject must be sent with the value I will always be here for PLD
curl -s "$1" -X POST -d "email: hr@holbertonschool.com" -d "subject: I will always be here for PLD"
