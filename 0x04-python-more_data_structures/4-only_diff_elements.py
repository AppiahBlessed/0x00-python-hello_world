#!/usr/bin/python3
# 4-only_diff_elements.py

def only_diff_elements(set_1, set_2):
    exclusive = set()  # Create empty set
    for i in set_1:
        if i not in set_2:
            exclusive.add(i)
        for i in set_2:
            if i not in set_1:
                exclusive.add(i)
    return exclusive
