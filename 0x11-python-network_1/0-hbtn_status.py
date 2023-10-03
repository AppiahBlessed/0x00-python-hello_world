#!/usr/bin/python3
"""
    This file fetches data from a url
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        data = response.read()
        decoded_text = data.decode('utf-8')
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
        print(f"\t- utf8 content: {decoded_text}")
