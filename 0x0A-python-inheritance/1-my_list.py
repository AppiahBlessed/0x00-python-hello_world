#!/usr/bin/python3
'''Lists the elements in a sorted format'''


class MyList(list):
    '''Class is a subclass of the in built list class'''
    def print_sorted(self):
        '''Sorts the output'''
        print(sorted(self))
