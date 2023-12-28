#!/usr/bin/python3
"""This script sends a post request with a ariable
-   To search
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
    data = {"q": letter}
    resp = requests.post(url, data=data)

    # Just to catch any JSON error
    try:
        json_data = resp.json()
        # if the json data is empty or valid
        if json_data and isinstance(json_data, (list, dict)):
            # get the id
            id_data = json_data.get("id")
            # get the name
            name_data = json_data.get("name")
            print(f"[{id_data}] {name_data}")
        # If data is empty
        elif not json_data:
            print("No result")
        # If it is not a valid json data
        elif not isinstance(json_data, (list, dict)):
            print("Not a valid JSON")
    # Catch exception
    except ValueError:
        print("Not a valid JSON")
