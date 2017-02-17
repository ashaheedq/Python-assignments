#Abdulshaheed Alqunber
# asq@bu.edu
#
# ps10pr3.py (Problem Set 10, Problem 3)
#
# Playing the Game  
#

from ps10pr1 import Board
from ps10pr2 import Player
import random

num_moves = 0
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board

def process_move(player, board):
    ''' takes two parameters:
    • a Player
    • a Board 
    '''
    
    print( player.__repr__() +"'s turn")
    col = player.next_move(board) 
    board.add_checker(player.checker ,col)
    
    print()
    print(board)

    if board.is_win_for(player.checker) == True:
        print()
        print(player, 'wins in', player.num_moves, 'moves.')
        print('Congratulations!')
        return True

    elif board.is_full() == True and board.is_win_for(player.checker) == board.is_win_for(player.opponent_checker):        
        print()
        print("It's a tie!")
        return True
    else:
        print()
        return False

class RandomPlayer(Player):

    def next_move(self, board):
        '''overrides (i.e., replaces) the next_move method that is inherited from Player.''' 
        true_cols = []
        for x in range(board.width):
            if board.can_add_to(x) == True:
                true_cols += [x]

        while True:
            if true_cols != []:
                col = random.choice(true_cols)
                self.num_moves +=1
                return col
        
