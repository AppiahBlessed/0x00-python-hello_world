#!/usr/bin/python3
"""This script fetches the headers of a get request
- Makes use of requests module
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    resp = requests.get(url)
    X_Request_Id = resp.headers.get("X-Request-Id")
    print(X_Request_Id)
