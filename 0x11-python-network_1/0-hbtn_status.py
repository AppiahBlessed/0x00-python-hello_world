#!/usr/bin/python3
import urllib.request
"""
    This script fetches a url and displays it in a formatted way
    It fetches the url and disp[lays the type of data returned (ie class obj).
    Displays the decoded byte form of the content for more human readable out
"""
if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        output = resp.read()
        print("Body response:")
        print("\t - type: ", type(output))
        print("\t - content: ", output)
        print("\t - utf8 content: ", output.decode('utf-8'))
