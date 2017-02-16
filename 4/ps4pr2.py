# 
# ps4pr2.py - Problem Set 4, Problem 2
#
#
# name: abdulshaheed alqunber
# email: asq@bu.edu
#
#
from ps4pr1 import *


#Function 1
def add(b1, b2):
    """takes as inputs two strings b1 and b2 that represent binary numbers. The function should compute
    the sum of the numbers, and return that sum in the form of a string that represents a binary number.
    """
    n1 = bin_to_dec(b1) 
    n2 = bin_to_dec(b2)
    b_sum = dec_to_bin((n1 + n2))
    return b_sum

print(add('11100', '11110'))

#Function 2
def increment(b):
    """takes an 8-character string representation of a binary number and returns the next
    larger binary number as an 8-character string
    """
    if b == '11111111':
        return '00000000'
    else:
        n = bin_to_dec(b)
        b_incr = dec_to_bin(n+1)
        leng = len(b_incr)
        if leng < 8:
            return ('0' * (8 - leng)) + b_incr
        else:
            return b_incr

print(increment('00000111'))
