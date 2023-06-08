#!/usr/bin/python3
def print_last_digit(number):
    last = number % 10
    if number < 0:
        neglast = (-1 * number) % 10  # Get last number
        print("{}".format(neglast), end='')  # Handles negatives
        return neglastv  # As per task
    else:
        print("{}".format(last), end='')
