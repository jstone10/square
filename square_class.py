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
            side_length = float(side_length)    
        except:
            side_length = 0

        side_length = math.round(side_length)
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


if __name__ == '__main__':