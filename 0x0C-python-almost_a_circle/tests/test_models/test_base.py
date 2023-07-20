#!/usr/bin/python3
'''This is a file containing test cases for all my modules'''
import unittest
from models.base import Base


class TestModules(unittest.TestCase):
    '''Class for all test cases'''
    def setUp(self):
        '''Run before all others'''
        self.first_obj = Base()
        self.second_obj = Base()

    def test_id(self):
        '''Test for no id parameter when called'''
        self.assertEqual(self.first_obj.id, 1)
        self.assertEqual(self.second_obj.id, 2)

    def test_none(self):
        '''Test for id parameter passed'''
        self.first_obj = Base(6)
        self.second_obj = Base(12)
        self.assertEqual(self.first_obj.id, 6)
        self.assertEqual(self.second_obj.id, 12)


if __name__ == '__main__':
    unittest.main()
