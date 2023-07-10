#!/usr/bin/python3
'''3-is_kind_of_class.py'''


def is_kind_of_class(obj, a_class):
    '''checks the object is an instance
    of, or if the object is an instance
    of a class that inherited from,
    the specified class
    '''
    return isinstance(obj, a_class)
