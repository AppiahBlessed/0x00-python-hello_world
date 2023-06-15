#!/usr/bin/python3
# 4-only_diff_elements.py

def only_diff_elements(set_1, set_2):
    exclusive = set()  # Create empty set
    for i in set_1:
        for j in set_2:
            if j == i:
                exclusive = set_1.union(set_2)  # Join both sets
                exclusive.remove(j)  # Remove that common element
    return exclusive
