#!/bin/bash
# This file uses POST method to send data to a serer
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
