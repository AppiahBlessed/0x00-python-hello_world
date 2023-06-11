#!/usr/bin/python3
# 5-no_c.py
# Loop through, if you find c then take the
# letters before and after it then add them together

def no_c(my_string):
    for idx, value in enumerate(my_string):
        if value == 'c' or value == 'C':
            newstring = my_string[:idx] + my_string[idx + 1:]
            return newstring
