# 
# ps2pr6.py - Problem Set 2, Problem 6
#
# Fun with recursion II
#
# name: abdulshaheed alqunber
# email: asq@bu.edu
#
# This is an individual-only problem that you must complete on your own.
#

#Recursion 1
def double(s):
    '''
    takes a string as an input and double every signle char in it 
    '''
    if s == '':
        return s
    else:
        new = double(s[1:])
        dou = s[0] * 2 
        return dou + new

print(double('python'))

#Recursion 2
def weave(s1, s2):
    '''
    takes two strings as input and it emerge them together more like "knitting" them together.
    '''

    if s2 == '':
        return s1
    elif s1 == '':
        return s2
    else:
        rest = weave(s1[1:], s2[1:])
        wea = s1[0] + s2[0]
        return wea + rest

print(weave('aaaa', 'bbbbbb'))


#Recursion 3
def index(elem, seq):
    '''
    takes a string or single character as an input 'elem' and 'seq'
    and try to look out for the first appearnce of 'elem' in 'seq'
    and return its position. if 'elem' is not in 'seq' the function returns -1
    '''

    if seq == '' or seq == []:
        return -1

    elif elem == seq[0]:
        return 0

    else:
        rest = seq[1:]
        rest_index = index(elem, rest)
        if rest_index < 0:
            return rest_index
        else:
            return rest_index + 1 

print(index('a', 'team'))

#Recursion 4
def one_dna_to_rna(c):
    '''
    takes a letter as an input and determine if its uppercase and represent a DNA
    then it convert it to a RNA
    '''
    assert(len(c) == 1)
    
    one = 'A'
    two = 'C' 
    three = 'G' 
    four = 'T'
    
    if c in one:
        return 'U'
    elif c in two:
        return 'G'
    elif c in three:
        return 'C'
    elif c in four:
        return 'A'
    else:
        return '' 

print(one_dna_to_rna('A'))

#Recursion 5
def transcribe(s):
    '''
    takes a string of DNA as input and convert it to a string of RNA
    using the 'one_dna_to_rna' function
    '''

    if s == '':
        return ''
    else:
        tran = one_dna_to_rna(s[0])
        rest = transcribe(s[1:])
        return tran + rest
    
print(transcribe('GCTAATCG'))
