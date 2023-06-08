#!/usr/bin/python3
# 3-infinite_add.py

import sys
# Dont run when imported as module
if __name__ == "__main__":
    arg_list = sys.argv
    arg_len = len(arg_list)
    number = 0

    if arg_list == 1:
        print("0")
    else:
        for i in range(1, arg_len):
            number += int(arg_list[i])  # Add arguments to itself
    print("{}".format(number))
