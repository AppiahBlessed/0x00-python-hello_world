#!/usr/bin/python3
"""This script displays X-Request-Id header
- Imported sys and urllib
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    # Get command line argument as url
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        output = resp.info().get("X-Request-Id")
        print(output)

