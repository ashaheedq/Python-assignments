# 
# ps4pr1.py - Problem Set 4, Problem 1
#
#
# name: abdulshaheed alqunber
# email: asq@bu.edu
#
#

#Function 1
def dec_to_bin(n):
    """takes a non-negative integer n and uses recursion to convert it from decimal
    to binary – constructing and returning a string version of the binary representation of that number. """
    if n == 0:
        return '0'
    elif n == 1:
        return  '1'
    else:
        rest = dec_to_bin(n>>1)
        if n%2 != 0:
            return rest + '1'
        else:
            return rest + '0'
            
print(dec_to_bin(5))

#Function 2
def bin_to_dec(b):
    """ takes a string b that represents a binary number and uses recursion to convert
    the number from binary to decimal, returning the resulting integer"""
    if b == '0':
        return 0
    elif b == '1':
        return  1
    else:
        rest = bin_to_dec(b[:-1]) << 1
        if b[-1] == '0':
            return rest + 0
        else:
            return rest + 1
            
print(bin_to_dec('1101'))
