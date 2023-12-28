#!/usr/bin/python3
"""This scriptconnects to my github using GitHub API
- 10-my_github.py
"""

if __name__ == "__main__":
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2]

    url = f"https://api.github.com/users/{username}"
    # Basic authentication where the PAT and username is used.
    header = {'Authorization': f'token {password}'}
    # Make get request
    resp = requests.get(url, headers=header)
    # Change response from JSON format, response from github, to python dict
    json_data = resp.json()
    # Get id from dictionary key
    user_id = json_data.get("id")
    # Print the id
    print(user_id)
