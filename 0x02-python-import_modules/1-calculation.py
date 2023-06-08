#!/usr/bin/python3
# 1-calculation.py
from calculator_1 import add, sub, mul, div
# Dont execute when imported as module
if __name__ == "__main__":
    a = 10
    b = 5
    # call add function
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    # call substract function
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    # call the multiplication function
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    # call the division function
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
