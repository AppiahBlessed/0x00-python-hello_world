#!/bin/bash
# Display body of GET request
[ "$(curl -sI "$1" | awk 'NR==1{print $2}')" == "200" ] && curl -s $1
