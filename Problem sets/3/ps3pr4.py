# 
# ps3pr4.py - Problem Set 3, Problem 4
#
#
# name: abdulshaheed alqunber
# email: asq@bu.edu
#
# This is an individual-only problem that you must complete on your own.
#

#Function 1
def index_last(c, s):
    """takes as inputs a character c and a string s and that uses recursion
    to find and return the index of the last occurrence of c.
    If the character c is not found in s, the function should return -1
    """
    if s == '':
        return -1

    elif c == s[-1]:
        return len(s) - 1

    else: 
        rest = s[:(len(s) - 1)]
        rest_index = index_last(c, rest)
        return rest_index
            
print(index_last('r', 'terriers'))

#Function 2
def rem_first(str1, str2):
    """ removes the first occurrence of elem from the list values
    """
    if str2 == '' or str1 == '':
        return ''
    elif str2[0] == str1:
        return str2[1:]
    else:
        result_rest = rem_first(str1, str2[1:])
        score = 0
        return str2[0] + result_rest
        
def jscore(s1, s2):
    """takes two strings s1 and s2 as inputs and
    returns the Jotto score of s1 compared with s2 using the helper function'rem_first'
    """
    if s2 == '' or s1 == '':
        return 0
    
    elif s1[0] in s2:
        rem = rem_first(s1[0], s2)
        rest = jscore(s1[1:], rem)
        return 1 + rest
    
    else:
        rest = jscore(s1[1:], s2)
        return rest
        
print(jscore('diner', 'syrup'))

#Function 3
def lcs(s1, s2):
    """ takes two strings s1 and s2 and returns
    the longest common subsequence they share
    """
    if s1 == s2:
        return s1
    
    elif s1 == '' or s2 == '':
        return ''

    elif s1[0] == s2[0]:
        lcs_rest = lcs(s1[1:], s2[1:])
        return s1[0] + lcs_rest 

    else:
        result1 = lcs(s1[1:], s2)
        result2 = lcs(s1, s2[1:])
        if len(result1) > len(result2):
            return result1
        else:
            return result2

print(lcs('gattaca', 'tacgaacta'))
