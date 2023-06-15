#!/usr/bin/python3
# 6-print_sorted_dictionary.py

def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary.keys())  # Sort the dictionaries
    for i in new_dict:
        print(i, ":", a_dictionary[i])
