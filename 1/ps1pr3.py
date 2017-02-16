# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# name: abdulshaheed alqunber   
# email: asq@bu.edu
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

# function 1
def root(x):
    """ returns the the square root of input x"""
    return x**0.5

# function 2
def gap(num1, num2):
    """ returns the "gap" in positive value between the two inputs"""
    if num1 == num2:
        return 0
    elif num1 >= num2:
        return num1 - num2
    elif num1 <= num2:
        return num2 - num1
    
# function 3
def larger_gap(a1, a2, b1, b2):
    """compute the gap between a1 and a2 and the gap between b1 and b2
    and returns either gap if they are equal
    otherwise returns the larger gap"""
    gap1 = gap(a1, a2)
    gap2 = gap(b1, b2)
    if gap1 == gap2:
        return gap1
    elif gap1 >= gap2:
        return gap1
    elif gap1 <= gap2:
        return gap2
    
# function 4
import math     #to get the square root function
def distance(x1, y1, x2, y2):
    """compute and returns the distance value between
    two points in the coordinates system"""
    x = square_diff(x1,x2) 
    y = square_diff(y1,y2) 
    summation = x + y
    dist = summation ** 0.5
    return dist

def square_diff(x,y):
    s = (y - x) **2
    return s

# sample test call for function 0
print('opposite(-8) returns', opposite(-8))

# optional but encouraged: add test calls for your functions below
print("root(9) returns", root(9)) 

print("gap(11, 9) returns", gap(11, 9))

print("larger_gap(9, 4, 6, 8) returns", larger_gap(9, 4, 6, 8))

print("distance(6, 8, 9, 4) returns", distance(6, 8, 9, 4)) 
