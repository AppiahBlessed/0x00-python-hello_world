#!/usr/bin/python3
'''JSON is mainly used for converting computer data in any
format to another of different type'''
import json


def to_json_string(my_obj):
    '''Function returns the JSON representation of an object (string)'''
    return json.dumps(my_obj)
