#!/usr/bin/python3
''' class Rectangle that inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class that defines and
        creates a rectangle
        Private instance attributes, each with its
        own public getter and setter:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialization of instances'''
        super().__init__()  # Call the init method of Base class
        '''width validation'''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        '''height validation'''
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        '''x validation'''
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        '''y validation'''
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        self.count = 0
        if id:
            self.id = id

    @property
    def width(self):
        '''Gets the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width attribute'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Gets the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the height attribute'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Gets the x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''sets the x attribute'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Gets the y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets the y attribute'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Computes the area of thr rectangle'''
        return self.__width * self.__height

    def display(self):
        '''Draw rectangle with '#'''
        if self.__y:
            print('\n' * self.__y, end='')
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print("#" * self.__width)
            self.count += 1  # for test cases
        return self.count

    def __str__(self):
        '''Stron output when Rectangle obj is printed'''
        result = (
            f"[Rectangle] ({self.id}) "
            f"{self.__x}/{self.__y} - {self.width}/{self.height}"
        )
        return result
