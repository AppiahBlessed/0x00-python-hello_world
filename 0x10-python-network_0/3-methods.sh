#!/bin/bash
# This script gets all the aloowed methods in a request to a website
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
