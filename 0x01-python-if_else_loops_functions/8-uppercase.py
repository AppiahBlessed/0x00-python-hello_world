#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in (str):  # Loop through character by chracter
        if ord(char) >= 97 and ord(char) <= 122:  # Check for lower case
            newchar = ord(char) - 32  # convert to upper
            result += chr(newchar)  # add capitalized character to new string
        else:
            result += char  # if already upper, add to new string
    print("{}".format(result))
