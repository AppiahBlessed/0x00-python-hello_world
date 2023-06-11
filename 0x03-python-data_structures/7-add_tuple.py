#!/usr/bin/python3
# Assign the firts elemnt of both tuples if to the variables if
# only the number of elements in the tuple is up to or more than 2
# If not give that particular index 0
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    first_element = a1 + b1
    second_element = a2 + b2
    new_tuple = (first_element, second_element)
    return new_tuple
