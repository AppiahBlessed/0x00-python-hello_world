#!/bin/bash
# This bash script requests to a url through http and returns the bytes
curl -sI "$1" | grep -i 'content-length:' | awk '{print $2}'
