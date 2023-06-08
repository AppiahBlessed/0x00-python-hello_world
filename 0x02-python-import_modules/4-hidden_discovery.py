#!/usr/bin/python3
# 4-hidden_discovery.py

if __name__ == "__main__":
    import hidden_4
    lists = dir(hidden_4)  # Derive items from module
    sorted_list = sorted(lists)  # Sort items alphabetically

    for value in (sorted_list):
        check = value
        if check[0] != "_":  # To print all but those starting with '--'
            print(value)
