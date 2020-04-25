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


class Square(object):
   
    def __init__(self, side_length):
        try:
            self.side_length = float(side_length)    
        except:
            self.side_length = 0
   
    def get_perimeter(self):
    	return 4 * self.side_length

    def get_area(self):
    	return self.side_length ** 2


if __name__ == '__main__':