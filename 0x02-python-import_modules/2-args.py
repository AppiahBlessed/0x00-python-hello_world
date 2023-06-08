#!/usr/bin/python3
# 2-args.py

import sys
# Dont execute when exported as a module
if __name__ == "__main__":
    argslist = sys.argv
    arg_len = len(argslist) - 1  # Get lenght or num or arguements
    if arg_len == 1:
        print("{:d} arguement:".format(arg_len))
    elif arg_len == 0:
        print("{:d} arguements.".format(arg_len))
    else:
        print("{:d} arguements:".format(arg_len))
    for i in range(1, arg_len + 1):
        print("{}: {}".format(i, argslist[i]))
