#!/usr/bin/python3
# 1-safe_print_integer.py

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:  # Ignore error
        pass
    if isinstance(value, int):  # Check instance of integer
        return True
    else:
        return False
