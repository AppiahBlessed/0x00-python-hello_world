#!/usr/bin/python3
"""This script displays the status code of a request
- urllib.error.HTTPError
"""

if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib.error import HTTPError

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as resp:
            output = resp.read()
            print(output.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
