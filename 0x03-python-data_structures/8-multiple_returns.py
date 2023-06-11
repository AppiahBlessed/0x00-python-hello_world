#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    lenght_str = len(sentence)
    if sentence == '':
        first_char = 'None'
    else:
        first_char = sentence[0]
    new_tuple = (lenght_str, first_char)
    return new_tuple
