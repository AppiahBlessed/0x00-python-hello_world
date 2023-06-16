#!/usr/bin/python3
# 12-roman_to_int.py
def roman_to_int(roman_string):
    total = 0
    size = len(roman_string) - 1  # To not go over the range
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
            }  # Hold corresponding roman values
    for index in range(len(roman_string)):
        symbol = roman_string[index]  # String element when loop runs
        value = numerals[symbol]  # Corresponding value defined in dictionary
        if symbol not in numerals:  # If the roman_string is not string
            return 0
# Compare previous value to the next one
        if index < size and value < numerals[roman_string[index + 1]]:
            total = total - value
        else:
            total = total + value
    return total
