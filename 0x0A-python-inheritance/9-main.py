#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
mine = Rectangle(10, 10)
print(r.area())
print(mine.area())
