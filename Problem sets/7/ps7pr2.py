#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# Processing sequences with loops
#
# Computer Science 111
#

### PUT YOUR WORK FOR PROBLEM 2 BELOW. ###

# Function 1
def double(s):
    """ takes an arbitrary string s as input, and that uses a loop to construct
and return the string formed by doubling each character in the string """
    result = ''

    for c in s:
        c *= 2
        result += c
    return result

# Function 2
def weave(s1, s2):
    """ takes as inputs two strings s1 and s2 and uses a loop to construct and return a new string that
is formed by “weaving” together the characters in the strings s1 and s2 to create a single string """
    result = ''
    len_shorter = min(len(s1), len(s2))

    for i in range(len_shorter):
        result += s1[i] + s2[i]
    if len(s1) >= len(s2):
        result += s1[len_shorter:]
    elif len(s1) <= len(s2):
        result += s2[len_shorter:]
    return result
    

#Function 3
def index(elem, seq):
    index = 0
    for i in range(len(seq)):
        index+=1
        if elem == seq[i]:
            return index - 1
        elif index >= len(seq):
             index = -1
    return index



### TEST FUNCTIONS
### Below, we have provided a test function for each part of this problem.
###
### After completing a given part of the problem, you can test it by:
###    - running the program
###    - calling its test function from the Shell (e.g., test1())
###
### We encourage you to add other tests to each test function to ensure
### that your code is thoroughly tested.
###
### ** To facilitate grading, please put all of your test code in the
###    appropriate test function. Do NOT add any lines of code that
###    belong to the global scope of the program (i.e., lines that are
###    outside of any function).


def test1():
    """ test function for part 1 (the double function)
    """
    result = double('hello')
    if type(result) != str:
        print('ERROR: double should return a string')
        return
    elif result != 'hheelllloo':
        print("ERROR: incorrect return value. double('hello') -->", result)
        print("Check to make sure that you don't have an extra space.")
        return
    else:
        print("double('hello') -->", result)
        print("double('python') -->", double('python'))

def test2():
    """ test function for part 2 (the weave function)
    """
    result = weave('aaaaaa', 'bbbbbb')
    if type(result) != str:
        print('ERROR: weave should return a string')
        return
    elif result != 'abababababab':
        print("ERROR: incorrect return value. weave('aaaaaa', 'bbbbbb') -->", result)
        print("Check to make sure that you don't have an extra space.")
        return
    else:
        print("weave('aaaaaa', 'bbbbbb') -->", result)
        print("weave('abcde', 'VWXYZ') -->", weave('abcde', 'VWXYZ'))
        print("weave('aaaaaa', 'bb') -->", weave('aaaaaa', 'bb'))
        
def test3():
    """ test function for part 3 (the index function)
    """
    result = index(5, [4, 10, 8, 5, 3, 5])
    if type(result) != int:
        print('ERROR: index should return an integer')
        return
    elif result != 3:
        print("ERROR: incorrect return value. index(5, [4, 10, 8, 5, 3, 5]) -->", result)        
        return
    else:
        print("index(5, [4, 10, 8, 5, 3, 5]) -->", result)
        print("index('hi', ['well', 'hi', 'there']) --->", index('hi', ['well', 'hi', 'there']))
        print("index('b', 'banana') --->", index('b', 'banana'))
