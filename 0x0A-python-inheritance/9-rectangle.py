#!/usr/bin/python3
'''Creating a class names Geometry'''


class BaseGeometry:
    '''Creating a class names Geometry'''

    def area(self):
        '''Empty method...'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''This method validates value'''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    '''Subclass of the parent clase BASEGEOMETRY'''
    def __init__(self, width, height):
        '''Initialization of instances'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''Determines the area of a rectangle'''
        return self.__height * self.__width

    def __str__(self):
        '''Iplementing the magic string method'''
        return f"[Rectangle] {self.__width}/{self.__height}"
