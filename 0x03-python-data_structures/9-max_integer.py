#!/usr/bin/python3
# 9-max_integer.py
# first check for empty list
# Make 'highest' var hold the first value of the list
# for each iteration, compare the first value to the cuurent indexed
# if i is bigger than the first index, update the 'highest' var aand continue
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    highest = my_list[0]
    for i in my_list:
        if i > highest:
            highest = i
    return highest
