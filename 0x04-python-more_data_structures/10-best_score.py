#!/usr/bin/python3
# 10-best_score.py

def best_score(a_dictionary):
    if not a_dictionary:  # Checks for rmpty dictionary
        return None
    max_value = float('-inf')  # Give it an infinity negative number
    max_key = None  # Let our key hold Nothing

    for key, value in a_dictionary.items():  # To get key value pair
        if value > max_value:
            max_value = value
            max_key = key  # The above finds the maximum value
    return max_key
