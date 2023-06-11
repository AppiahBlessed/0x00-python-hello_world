#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    mynew_list = my_list[::-1]  # Reversed string through slicing
    for i in mynew_list:
        print("{:d}".format(i))
