#!/usr/bin/python3
'''Test case for Rectangle class'''
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Inheriting from the unittest class'''
    def setUp(self):
        '''Fixures in a bit...'''
        pass

    def test_width(self):
        '''Tests if width has been initialized with value'''
        self.rc1 = Rectangle(1, 3)
        self.assertEqual(self.rc1.width, 1)
        '''set width'''
        self.rc1.width = 10
        self.assertEqual(self.rc1.width, 10)

    def test_height(self):
        '''Tests if height has been initialized with value'''
        self.rc1 = Rectangle(19, 3)
        self.assertEqual(self.rc1.height, 3)
        '''set height'''
        self.rc1.height = 4
        self.assertEqual(self.rc1.height, 4)

    def test_x(self):
        '''Tests if x has been initialized with value'''
        self.rc1 = Rectangle(2, 4, 0)
        self.assertEqual(self.rc1.x, 0)
        '''set x value'''
        self.rc1.x = 14
        self.assertEqual(self.rc1.x, 14)

    def test_y(self):
        '''Tests if y has been initialized with value'''
        self.rc1 = Rectangle(7, 6, 0, 7)
        self.assertEqual(self.rc1.y, 7)
        '''set height'''
        self.rc1.height = 109
        self.assertEqual(self.rc1.height, 109)

    def test_wrongwidth(self):
        '''Save the error message into e_msg
            call the class with invalid input
            compare the expected output to the gotten
        '''
        with self.assertRaises(TypeError) as e_msg:
            Rectangle('no', 7)
        self.assertEqual(str(e_msg.exception), 'width must be an integer')

    def test_negwidth(self):
        '''Takes negative input'''
        with self.assertRaises(ValueError) as e_msg:
            Rectangle(-1, 8)
        self.assertEqual(str(e_msg.exception), 'width must be > 0')

    def test_zerowidth(self):
        '''Takes zero as input'''
        with self.assertRaises(ValueError) as e_msg:
            Rectangle(0, 3)
        self.assertEqual(str(e_msg.exception), "width must be > 0")
        self.rc1 = Rectangle(1, 3)
        with self.assertRaises(ValueError) as e_msg:
            self.rc1.width = 0  # using setter
        self.assertEqual(str(e_msg.exception), "width must be > 0")

    def test_wrongheight(self):
        '''Save the error message into e_msg
            call the class with invalid input
            compare the expected output to the gotten
        '''
        with self.assertRaises(TypeError) as e_msg:
            Rectangle(6, '7')
        self.assertEqual(str(e_msg.exception), 'height must be an integer')

    def test_height(self):
        '''Takes negative input'''
        with self.assertRaises(ValueError) as e_msg:
            Rectangle(1, -8)
        self.assertEqual(str(e_msg.exception), 'height must be > 0')

    def test_zeroheight(self):
        '''Takes zero as input'''
        with self.assertRaises(ValueError) as e_msg:
            Rectangle(3, 0)
        self.assertEqual(str(e_msg.exception), "height must be > 0")
        self.rc1 = Rectangle(1, 3)
        with self.assertRaises(ValueError) as e_msg:
            self.rc1.height = 0  # using setter
        self.assertEqual(str(e_msg.exception), "height must be > 0")

    def test_wrongx(self):
        '''Save the error message into e_msg
            call the class with invalid input
            compare the expected output to the gotten
        '''
        with self.assertRaises(TypeError) as e_msg:
            Rectangle(6, 7, '0')
        self.assertEqual(str(e_msg.exception), 'x must be an integer')

    def test_negx(self):
        '''Takes negative input'''
        with self.assertRaises(ValueError) as e_msg:
            Rectangle(1, 8, -10)
        self.assertEqual(str(e_msg.exception), 'x must be >= 0')
        '''change value x'''
        self.rc1 = Rectangle(1, 3, 9)
        with self.assertRaises(ValueError) as e_msg:
            self.rc1.x = -2  # using setter
        self.assertEqual(str(e_msg.exception), "x must be >= 0")

    def test_wrongy(self):
        '''Save the error message into e_msg
            call the class with invalid input
            compare the expected output to the gotten
        '''
        with self.assertRaises(TypeError) as e_msg:
            Rectangle(6, 7, 9, '9')
        self.assertEqual(str(e_msg.exception), 'y must be an integer')

    def test_negy(self):
        '''Takes negative input'''
        with self.assertRaises(ValueError) as e_msg:
            Rectangle(1, 8, 89, -10)
        self.assertEqual(str(e_msg.exception), 'y must be >= 0')

        '''change value y'''
        self.rc1 = Rectangle(1, 3, 9, 9)
        with self.assertRaises(ValueError) as e_msg:
            self.rc1.y = -2  # using setter
        self.assertEqual(str(e_msg.exception), "y must be >= 0")

    def test_area(self):
        '''Tests for right area computed'''
        self.rc1 = Rectangle(5, 5)
        self.assertEqual((self.rc1.height * self.rc1.width), 25)

    def test_display(self):
        '''Test for the number of rectangle element
            I will dill this later
        '''
        pass

    def test_str(self):
        '''Tests the __str__ format defined'''
        self.rc1 = Rectangle(1, 5, 7, 9, 2)
        self.assertEqual(str(self.rc1), '[Rectangle] (2) 7/9 - 1/5')


if __name__ == '__main__':
    unittest.main()
