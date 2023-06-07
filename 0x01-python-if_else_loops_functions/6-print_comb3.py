#!/usr/bin/python3
for i in range(1, 10):
    for j in range(i+1, 10):
        print("{:02d}, ".format(i), end="")
        if j == 9:
            print("{:02d}".format(j))
        else:
            print("{:02d}, ".format(j), end="")

