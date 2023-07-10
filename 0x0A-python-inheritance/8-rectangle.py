#!/usr/bin/python3
'''Creating a class names Geometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Subclass of the parent clase BASEGEOMETRY'''
    def __init__(self, width, height):
        '''Initialization of instances'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
