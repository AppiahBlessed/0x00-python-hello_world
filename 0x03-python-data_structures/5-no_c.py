#!/usr/bin/python3
# 5-no_c.py
# Loop through, if you find c then take the
# Create a new string but without the sad character to beremoved

def no_c(my_string):
    newstring = ''
    for value in my_string:
        if value != 'c' and value != 'C':
            newstring += value
    return newstring
