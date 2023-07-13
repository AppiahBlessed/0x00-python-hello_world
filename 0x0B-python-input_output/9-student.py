#!/usr/bin/python3
'''Write a class, and add a special method "to_json"'''


class Student:
    '''Defines a class to hold info of students'''
    def __init__(self, first_name, last_name, age):
        '''Initialize variables on object creation'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieves a dictionary representation of a Student instance'''
        if not isinstance(self, object):
            return None
        stuff = self.__dict__
        new_dict = {
            key: value
            for key, value in stuff.items()
            if isinstance(value, (list, dict, str, bool, int))
        }
        return new_dict
