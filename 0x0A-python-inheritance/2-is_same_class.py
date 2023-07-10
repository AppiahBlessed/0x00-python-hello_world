#!/usr/bin/python3
'''Exact same object'''


def is_same_class(obj, a_class):
    '''is_same_class checks
        if the object is exactly
        an instance of the specified class
    '''
    return type(obj) is a_class
