# 
# ps3pr3.py - Problem Set 3, Problem 3
#
#
# name: abdulshaheed alqunber
# email: asq@bu.edu
#
# This is an individual-only problem that you must complete on your own.
#

#Function 1
def cube_vals_lc(values):
    """ takes as input a list of numbers called values, and that uses a list
    comprehension to create and return a list containing the cubes of the numbers in values
    """
    lc = [x**3 for x in values]
    return lc

print(cube_vals_lc([-2, 5, 4, -3]))

#Function 2
def cube_vals_rec(values):
    """takes as input a list of numbers called values, and that uses recursion
    to create and return a list containing the cubes of the numbers in values
    """
    if len(values) == 0:
        return values
    
    else:
        cube = values[0] ** 3
        cube_rest = cube_vals_rec(values[1:])
        return [cube] + cube_rest
        
print(cube_vals_rec([-2, 5, 4, -3]))

#Function 3
def num_greater(threshold, values):
    """ takes a number 'threshold' and a list of numbers 'values' as inputs and return the number
    of elements of the list of numbers that are greater than the given number 'threshold'
    """
    lc = [x for x in values if x > threshold]
    leng = len(lc)
    return leng
    
print(num_greater(2, [1, 7, 3, 5, 10]))

#Function 4
def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest

def most_vowels(wordlist):
    """ takes a list of strings and using the helper function "num_vowels"
    it returns the string in the list with the most vowels
    """
    lc = [[num_vowels(s),s] for s in wordlist]
    most = max(lc)
    return most[1]

print(most_vowels(['obama', 'bush', 'clinton']))







    
    
