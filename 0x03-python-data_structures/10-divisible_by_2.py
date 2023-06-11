#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    new_list = my_list[:]  # Copy string content to become imutable
    for idx, value in enumerate(my_list):
        if value % 2 == 0:  # Checks for divisibility
            new_list[idx] = True  # Replace that number with bool
        else:
            new_list[idx] = False
    return new_list
