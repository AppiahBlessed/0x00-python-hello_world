#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 7, 6, 12)
    print(r3)
    print(r3.width)
    Rectangle.width = 20
    print(r3.width)
    print(r3.x)
    print(r3.y)
    print(r3.id)
