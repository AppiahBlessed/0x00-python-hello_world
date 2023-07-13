#!/usr/bin/python3
'''Write a function that creates an Object from a “JSON file'''
import json


def load_from_json_file(filename):
    '''
    Load is different from loads. the former takes string
    format of a json file and parses it as python object
    while the latter takes it from a file direct
    '''
    with open(filename, 'r') as f:
        obj = json.load(f)
        return obj
