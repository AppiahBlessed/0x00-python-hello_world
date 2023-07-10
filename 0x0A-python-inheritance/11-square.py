#!/usr/bin/python3
'''Creating a class names Geometry'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Subclass of Rectangle subclass'''
    def __init__(self, size):
        '''Initialises first creation of object'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Defines the area of the square'''
        return self.__size ** 2

    def __str__(self):
        '''Iplementing the magic string method'''
        return f"[Square] {self.__size}/{self.__size}"
