#!/usr/bin/python3
# 3-common_elements.py

def common_elements(set_1, set_2):
    common = set()  # Create empty set
    for i in set_1:
        for j in set_2:
            if i == j:  # Find common character in both sets
                common.add(j)  # Add to set object
    return common
