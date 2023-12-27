#!/usr/bin/python3
"""This script uses a POST method to send data to a site
- You don’t need to check arguments passed to the script (number or type)
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    # Get url and emal parameters
    url = sys.argv[1]
    email = sys.argv[2]
    # Request body. Just because computers cant understand human texts.
    data = f"email={email}".encode("utf-8")
    with urllib.request.urlopen(url, data=data) as resp:
        output = resp.read().decode("utf-8")
        print(output)
