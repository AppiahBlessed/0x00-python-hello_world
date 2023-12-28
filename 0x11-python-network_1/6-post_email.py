#!/usr/bin/python3
"""This script sends a POST request to the passed URL
- Uses the requests module
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    # Post in requests module handles encoding automatically
    email = sys.argv[2]
    data = {"email": email}
    resp = requests.post(url, data=data)
    print(resp.text)
