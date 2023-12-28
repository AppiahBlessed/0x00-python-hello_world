#!/usr/bin/python3
"""Fetch webpage using the requests module
- What's my status?
"""

if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url).text
    print("Body response:")
    print("\t- type: {}".format(type(resp)))
    print("\t- content: {}".format(resp))
