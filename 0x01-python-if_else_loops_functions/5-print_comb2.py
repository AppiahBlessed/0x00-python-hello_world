#!/usr/bin/python3
for i in range(0, 100):
    #Set width of two. adding 0 to single numbers
    print("{:02d}, ".format(i), end='')
    if i == 99:
        #To not include the comma at the end
        print("99")
