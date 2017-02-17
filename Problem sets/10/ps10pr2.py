#Abdulshaheed Alqunber
# asq@bu.edu
# ps10pr2.py (Problem Set 10, Problem 2)
#
# A Connect-Four Player class 
#

from ps10pr1 import Board

# write your class below

class Player:

    def __init__(self, checker):
        ''' constructs a new Player object by initializing the following two attributes:
    • an attribute checker
    • an attribute num_moves
    '''
        assert(checker == 'X' or checker == 'O')

        self.checker = checker
        self.num_moves = 0 

    def __repr__(self):
        ''' returns a string representing a Player object '''

        return 'Player ' +  self.checker
        
    def opponent_checker(self):
        ''' returns a one-character string representing the checker of
        the Player object’s opponent '''

        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        ''' accepts a Board object as a parameter and returns the column
        where the player wants to make the next move'''

        
        while True:
            
            col = int(input('Enter a column: '))
            if board.can_add_to(col) == True:
                self.num_moves += 1
                return col
            else:
                print('Try again!') 
            


        
        
