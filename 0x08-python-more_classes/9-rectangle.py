#!/usr/bin/python3
'''0-rectangle.py'''


class Rectangle:
    '''Defines rectangle'''
    '''Keep track of the number of objects'''
    number_of_instances = 0
    print_symbol = '#'
    '''New class method to return new
    Rectangle instance where width == height == size
    '''
    @classmethod
    def square(cls, size=0):
        '''returns a new instance'''
        new = Rectangle()
        new.width = size
        new.height = size
        return new

    def __init__(self, width=0, height=0):
        '''Initialise instance'''
        '''Instance Arguments'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''Defines the area of the rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''Finds the permeter of the rectangle'''
        if self.width == 0 or self.height == 0:
            perim = 0
        else:
            perim = 2 * (self.width + self.height)
        return perim

    def __str__(self):
        '''String representation of object'''
        if self.__height == 0 or self.__width == 0:
            return ''
        matrix = ''
        for i in range(self.__height):
            for j in range(self.__width):
                matrix += str(self.print_symbol)
            matrix += '\n'
        return matrix[:-1]

    def __repr__(self):
        '''Return sting format in the form that eval() can use'''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''Pops up when an instance is deleted'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Method that returns the biggest among
        the given instances
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
