#!/usr/bin/python#
# 9-multiply_by_2.py

def multiply_by_2(a_dictionary):
    new_dict = {}
    for i in a_dictionary:
        new_dict[i] = a_dictionary[i]  # Create new dictionary with old contents
    for i in new_dict:
        new_dict[i] = new_dict[i] * 2  # Multiply each element by 2
    return new_dict
