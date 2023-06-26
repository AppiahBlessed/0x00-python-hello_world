#!/usr/bin/python3
# 3-safe_print_division.py

def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {:.1f}".format(result))  # Print result at 1dm
    except Exception:
        result = None
        print("Inside result: None")
    finally:
        return result  # In whatever case
