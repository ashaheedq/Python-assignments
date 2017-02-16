# 
# ps1pr4.py - Problem Set 1, Problem 4
#
# Functions with numeric inputs
#
# name: abdulshaheed alqunber   
# email: asq@bu.edu

#function 1
def front3(s):
    """takes the first 3 characters from the given string s
    and returns 3 copies of the new string"""
    if len(s) >= 3: 
      front = s[:3] * 3
      return front
    else: 
      return s * 3

#function 2
def first_and_last(values):
    """takes a given list of values and returns a list
    that contains the first and last value of the original list"""
    first = [values[0]]
    last = [values[-1]]
    return first + last

#function 3
def longer_len(s1, s2):
    """takes two strings s1 and s2 and returns the length
    of the longer string"""
    string1 = len(s1)
    string2 = len(s2)
    if string1 > string2:
        return string1
    else:
        return string2   #if both were the same length its also going to return one of them, in this case its returning string2

#function 4
def move_to_end(s, n):
    """takes s string and n integer and returns
    a new string with n first char moved to the end of the string"""
    length = len(s)
    if n > length:
        return s
    else:
        first_n = s[:n]
        rest = s[n:]
        return rest + first_n 


# sample test call for functions
print("front3(s) returns", front3("shaheed"))

print ("first_and_last(values) returns", first_and_last([11,22,33,44]))

print("longer_len(s1, s2) returns", longer_len("shaheed", "alqunber"))

print("move_to_end(s, n) returns", move_to_end("shaheed", 3))
