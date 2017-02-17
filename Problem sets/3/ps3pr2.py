#
# ps3pr2.py (Problem Set 3, Problem 2)
#
# Caesar cipher / decipher
# Name: abdulshaheed alqunber
# Email: asq@bu.edu

# A template for a helper function called rot that we recommend writing
# as part of your work on the encipher function.
def rot(c, n):
    """ takes a single character c as an input and rotates it by n spots in alphabitcal order """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    # Put the rest of your code for this function below.
    if c == '':
        return ''
    
    elif 'a' <= c <= 'z':
        new_ord = ord(c) + n
        if new_ord > ord('z'):
            new_ord = new_ord - 26
            return chr(new_ord)
        else:
            return chr(new_ord)
        
    elif 'A' <= c <= 'Z':
        new_ord = ord(c) + n
        if new_ord > ord('Z'):
            new_ord = new_ord - 26
            return chr(new_ord)
        else:
            return chr(new_ord)
        
    else:
        return c

print(rot('a', 3))

#### Put your code for the encipher function below. ####
def encipher(s, n):
    """ takes a string s as an input and rotates all the characters by n spots in the alphabet
    using the helper function 'rot' """
    if s == '':
        return s
    else:
        first = rot(s[0], n)
        rest_s = encipher(s[1:], n)
        return first + rest_s 
    
print(encipher('ali', 3))


# A helper function that could be useful when assessing
# the "Englishness" of a phrase.
# You do *NOT* need to modify this function.
def letter_probability(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

#### Put your code for the decipher function below. ####
def string_probability(s):
    """ a helper function that takes a string s as an input and
    calculate the probability score for the given string"""
    if s == '':
        return 0
    else:
        score = letter_probability(s[0])
        rest_s = string_probability(s[1:])
        return score + rest_s

print(string_probability('python'))
    
def decipher(s):
    """ takes an arbitrary string s as input and which happened to be enciphered by
    a random number. This function uses helper function to decipher the string and return the best pair
    determined by its Englishness
    """
    options = [encipher(s, n) for n in range(26)]
    scored_options = [[string_probability(s), s] for s in options]
    best_pair = max(scored_options)
    return best_pair[1]
    
print(decipher('kwvozibctibqwva izm qv wzlmz nwz iv mfkmttmvb rwj'))
