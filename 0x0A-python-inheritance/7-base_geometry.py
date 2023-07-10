#!/usr/bin/python3
'''Creating a class names Geometry'''


class BaseGeometry:
    '''Creating a class names Geometry'''

    def area(self):
        '''Empty method...'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''This method validates value'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
