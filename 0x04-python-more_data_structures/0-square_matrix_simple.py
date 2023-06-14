#!/usr/bin/python3
# 0-square_matrix_simple.py
def power (num):
    return num * num

def square_matrix_simple(matrix=[]):
    new_list = list(map(lambda numb: list(map(power, numb)), matrix))
    return new_list


