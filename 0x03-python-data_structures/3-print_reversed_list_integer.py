#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# Reversed the srting
def print_reversed_list_integer(my_list=[]):
    mynew_list = my_list[::-1]
    for i in mynew_list:
        print("{:d}".format(i))
