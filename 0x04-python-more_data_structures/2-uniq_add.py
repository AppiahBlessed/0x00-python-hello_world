#!/usr/bin/python3
# 2-uniq_add.py

def sum_it(mylist):
    result = 0
    for i in mylist:
        result += i
    return result


def uniq_add(my_list=[]):
    my_set = set(my_list)  # To remove duplicates
    new_list = sum_it(map(int, my_set))  # Add elements
    return new_list
