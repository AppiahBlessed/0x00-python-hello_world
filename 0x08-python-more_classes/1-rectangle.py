#!/usr/bin/python3
'''0-rectangle.py'''


class Rectangle:
    '''Defines rectangle'''
    pass

    def __init__(self, width=0, height=0):
        '''Initialise instance'''
        '''Instance Arguments'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Width method'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets rectangles width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Height method'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets rectangles width'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
