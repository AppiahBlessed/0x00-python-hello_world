#!/usr/bin/python3
def print_last_digit(number):
    last = number % 10
    if number < 0:
        neglast = (-1 * number) % 10
        print("{}".format(neglast), end='')
        return neglast
    else:
        print("{}".format(last), end='')
