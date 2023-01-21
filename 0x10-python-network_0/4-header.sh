#!/bin/bash
# Send a GET request to the URL using curl and display the body of the response while sending the header variable X-School-User-Id with the value 98
curl -s -H "X-School-User-Id: 98" "$1"
