#!/usr/bin/python3
"""This script prints the error code
- filename: 7-error_code.py
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    resp = requests.get(url)
    e_code = resp.status_code
    if e_code >= 400:
        print("Error code: {}".format(e_code))
    else:
        print(resp.text)
