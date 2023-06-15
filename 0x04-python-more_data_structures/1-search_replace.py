#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):
    newlist = my_list[:]  # Create copy of string immutably
    for idx, value in enumerate(newlist):
        if value == search:  # Find search item
            newlist[idx] = replace  # Replace item
    return newlist

# or
# def search_replace(my_list, search, replace):
# newlist = list(map(lambda x: replace if x == search else x, my_list))
# return newlist
