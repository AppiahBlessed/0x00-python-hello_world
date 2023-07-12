#!/usr/bin/python3
'''Function is meant to append'''


def append_write(filename="", text=""):
    '''Function is meant to append to either an
        existing file or create one where it doesnt exit
        Return:
        Returns the number of added characters
    '''
    with open(filename, 'a', encoding='utf-8,') as f:
        return f.write(text)
