# 
# ps2pr3.py - Problem Set 2, Problem 3
#
# Fun with recursion
#
# name: abdulshaheed alqunber
# email: asq@bu.edu
#
# This is an individual-only problem that you must complete on your own.
#

#Recursion 1

def copy(s, n):
    """ takes a string s and an integer n as inputs and uses recursion 
    to return a new string in which n copies of s.
    """
    if n <= 0:
        return ''
    else:
        copy_rest = copy(s, n-1)
        return copy_rest + s


#Recursion 2
def compare(list1, list2):
    """ 
    
    """
    if len(list2) == 0:
        return 0
    elif len(list1) == 0:
        return 0
    elif len(list1) > len(list2):
        return 1
    elif len(list1) < len(list2):
        return 2 
    else:
        num1 = []
        num2 = []
        if list1[0] > list2[0]:
            return [1] + num1
        elif list1[0] < list2[0]:
            return [2] + num2
    

#Recursion 3
def letter_score(letter):
    """ takes a lowercase letter as an input and returns the value of the given letter
    in terms of scrabble value
    """
    assert(len(letter) == 1)
    one = 'aeinorstul' 
    two = 'dg' 
    three = 'bcmp' 
    four = 'fhvwy' 
    five = 'k' 
    eight = 'jx' 
    ten = 'qz' 
    
    if letter in one:
        return 1
    elif letter in two:
        return 2
    elif letter in three:
        return 3
    elif letter in four:
        return 4
    elif letter in five:
        return 5
    elif letter in eight:
        return 8
    elif letter in ten:
        return 10
    else:
        return 0 




#Recursion 4
def scrabble_score(word):
    """ takes a string word as an input and uses the letter_score function to compute
    the scrabble score of that string 
    """

    if word == '':
        return 0
    else:
        score = letter_score(word[0])
        rest = word[1:]
        return score + scrabble_score(rest)


        
#test
print(copy('ali', 3))

print(compare([1,2,3,4,5], [6,7,8])) 

print(letter_score('f'))

print(scrabble_score('faris'))

