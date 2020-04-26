# square_class.py
#
# by:      Josh Stone
# created: 4/24/20
#
# Simple square class 

#!/bin/python3
import math
import os
import random
import re
import sys
import unittest
import string

# Square Class
# Description: Object that represents a square
# Invairants:
#      * Side lengths are rounded to the nearest integer
#      * Side lengths are always positive
#      * Side lengths at least 0 and at most 10
# Caught Exceptions:
#      * instantiating a square with a rounded side length  > 10 or < 0
#        defaults the length to 0
#      * instanting a sqaure with a side_length that is not a number
class Square(object):

    # I: int side_length
    # O: none
    # Does: instantiates square object
    def __init__(self, side_length):

        try:
            side_length = int(side_length)    
        except:
            side_length = 0

        if side_length > 10 or side_length < 0:
            self.side_length = 0
        else: 
            self.side_length = side_length
    
    # I: none
    # O: Int
    # Does: Computes perimeter of square based on side_length
    def get_perimeter(self):
        return 4 * self.side_length


    # I: none
    # O: Int
    # Does: Computes area of square based on side_lenght
    def get_area(self):
        return self.side_length ** 2

class sq_tests(unittest.TestCase):

    def test_string(self):
        for i in range(100):
            s  = randomString(i)
            sq = Square(s)
            self.assertEqual(sq.side_length, 0)

    def test_random_float(self):
        random.seed()

        for i in range(100):
            sl = random.uniform(-1000, 10000)
            sq = Square(sl)

            if int(sl) > 10 or int(sl) < 0:
                self.assertEqual(sq.side_length, 0)
            else:
                self.assertEqual(sq.side_length, int(sl))

    def test_area(self):
        random.seed()

        for i in range(100):
            sl = random.uniform(0, 10)
            sq = Square(sl)
            self.assertEqual(sq.get_area(), int(sl) ** 2)

    def test_perimeter(self):
        random.seed()

        for i in range(100):
            sl = random.uniform(0, 10)
            sq = Square(sl)
            self.assertEqual(sq.get_perimeter(), int(sl) * 4)


def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == '__main__':
    unittest.main()