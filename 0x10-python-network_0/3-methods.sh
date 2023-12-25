#!/bin/bash
# This script gets all the aloowed methods in a request to a website
curl -sIX DELETE "$1" | grep "Allow" | cut -d " " -f 2-
