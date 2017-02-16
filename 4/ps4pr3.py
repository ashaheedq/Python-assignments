# 
# ps4pr3.py - Problem Set 4, Problem 3
#
#
# name: abdulshaheed alqunber
# email: asq@bu.edu
#
#

#Function 1
def bitwise_and(b1, b2):
    """takes as inputs two strings b1 and b2 that represent binary numbers and useing recursion
    to compute the bitwise AND of the two numbers and return the result in the form of a string. """
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '' or b2 == '':
        leng = len(b2) + len(b1)
        return '0' * leng
    else:
        rest = bitwise_and(b1[:-1], b2[:-1])
        if b1[-1] == '0' or b2[-1] == '0':
            return rest + '0'
        else:
            return rest + '1' 

print(bitwise_and('1001111', '11011'))

#Function 2
def add_bitwise(b1, b2):
    """adds two binary numbers using recursion and return the result"""
    if b1 == '':
        return b2
    elif b2 == '':
        return b1
    else:
        rest = add_bitwise(b1[:-1], b2[:-1])
        carry = add_bitwise('1', rest)
        if b1[-1] == '0' and b2[-1] == '0':
            return rest + '0'
        elif b1[-1] == '1' and b2[-1] == '1':
            return carry + '0' 
        else:
            return rest + '1' 
        '''b1[-1] == '1' or b2[-1] == '1':''' 
        
print(add_bitwise('11100', '11110'))
