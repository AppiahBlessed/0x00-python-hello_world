#!/bin/bash
# This script uses POST to send data to a site
curl -sX POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
