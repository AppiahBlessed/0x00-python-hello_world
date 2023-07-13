#!/usr/bin/python3
'''Write a function that returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:
'''


def class_to_json(obj):
    '''Function functioned functioning'''
    if not isinstance(obj, object):  # Check if obj is an instance of any class
        return None

# Get the attributes or data structs in the class
    stuff = obj.__dict__
# Filter to get our serializables
    final_dict = {
            key: value
            for key, value in stuff.items()
            if isinstance(value, (list, dict, str, int, bool))
    }
    return final_dict
