#
# ps2pr5.py - Problem Set 2, Problem 5
#
# List comprehensions
#
# name: abdulshaheed alqunber
# email: asq@bu.edu
#

# Problem 5-1: LC puzzles!
# This code won't work until you complete the list comprehensions!
# If you can't figure out how to complete one of them, please
# comment out the corresponding lines by putting a # at the start
# of the appropriate lines.

# part a
lc1 = [    x+5 for x in range(5)]
print(lc1)

# part b
lc2 = [  word + 'ing' for word in ['go', 'eat', 'read']]
print(lc2)

# part c
words = ['hello', 'world', 'how', 'goes', 'it?']
lc3 = [ w[-1] for w in words]
print(lc3)

# part d
lc4 = [ c =='a' for c in 'aardvark']
print(lc4)

# part e
lc5 = [ x for x in range(1, 21) if x % 5 == 0 ]
print(lc5)


# Problem 5-2: Put your definition of the powers_of() function below.
def powers_of(base, count):
    '''
    takes 'base' as an integer and returns a list 
    its element are the range powers of 'base' from the input 'count'
    '''
    lc = [ (base ** x) for x in range(count)]
    return lc

print(powers_of(2, 5))

# Problem 5-3: Put your definition of the longer_than() function below.
def longer_than(n, wordlist):
    '''
    takes the inputs 'n' and the list of string 'wordlist' and return
    a list that contains all words that are longer than 'n' 
    '''

    lc = [ x for x in wordlist if len(x) > n] 
    return lc

print(longer_than(3, ['ali', 'ahmed', 'shaheed', 'faris']))
