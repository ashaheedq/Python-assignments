# 
# ps1pr1.py - Problem Set 1, Problem 1
#
# Indexing and slicing puzzles
#
# name: abdulshaheed alqunber
# email: asq@bu.edu
#
# This is an individual-only problem that you must complete on your own.
#

#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [3, 7, 1] from pi and e
answer0 = [pi[0]] + e[-2:]     
print(answer0)

# Puzzle 1:
# Creating the list [1, 5, 9] from pi 
answer1 = pi[-3:]
print(answer1)

# Puzzle 2:
# Creating the list [3, 4, 5] from pi 
answer2 = pi[0::2]
print(answer2)

# Puzzle 3:
# Creating the list [5, 4, 3, 2, 1] from pi and e
answer3 = pi[-2::-2] + e[-3::2]
print(answer3)

# Puzzle 4:
# Creating the list [9, 1, 1, 1] from pi and e
answer4 = pi[-1::-2] + [e[-1]]
print(answer4)


#
# String puzzles
#

b = 'boston'
u = 'university'
t = 'terriers'

# Puzzle 5
# Creating the string 'bossy'
answer5 = b[:3] + t[-1] + u[-1]
print(answer5)

# Puzzle 6
# Creating the string 'vest'
answer6 = u[3:5] + t[-1::-7]
print(answer6)

# Puzzle 7:
# Creating the string 'revisit'
answer7 = u[-5:-9:-1] + u[-4:-1]
print(answer7)

# Puzzle 8:
# Creating the string 'booooooo'
answer8 = b[0] + (b[1] * 7)
print(answer8)

# Puzzle 9:
# Creating the string 'sobstory'
answer9 = b[-4::-1] + b[2:5] + u[5::4] 
print(answer9)

# Puzzle 10:
# Creating the string 'borris'
answer10 = b[:2] + t[2:5] + t[-1]
print(answer10)

