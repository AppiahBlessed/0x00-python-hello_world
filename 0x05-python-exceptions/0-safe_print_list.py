#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    count = 0

    for i in my_list:
        count += 1  # Get the length of list
    try:
        for i in range(x):
            print(my_list[i], end='')
    except Exception:
        pass  # Dont print any error
    print()  # Print new line
    return count
