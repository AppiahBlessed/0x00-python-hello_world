#!/bin/bash
# This script request a url and gets the size of the response
curl -sI "$1" | grep "Content-Length" | awk 'NR==1{print $2}'
