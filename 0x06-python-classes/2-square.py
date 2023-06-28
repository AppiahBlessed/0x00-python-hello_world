#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Square that defines a square"""
    def __init__(self, __size=0):
        """Initializing new square
            Args:
        """
        self.__size = __size
        try:
            if isinstance(__size, int):
                pass
            if __size < 0:
                raise ValueError

        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
