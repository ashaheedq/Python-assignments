#
# ps10pr4.py (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four
#
import random
from ps10pr3 import *

class AIPlayer(Player):

    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object and call the superclass
        constructor to initialize the inherited attributes.
        two attributes that are not inherited from Player:
        • tiebreak
        • lookahead
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead


    def __repr__(self):
        """ returns a string representing an AIPlayer object. This method will override
        the __repr__ method that is inherited from Player.
        """

        return 'Player ' + self.checker + ' (' + self.tiebreak +', ' + str(self.lookahead)+ ')'


    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the board, and that returns
        the index of the column with the maximum score. If one or more columns are tied for the
        maximum score, the method should apply the called AIPlayer‘s tiebreaking strategy
        to break the tie. """

        '''max_scores = []
        scores_ind = []
        for x in range(len(scores)):
            if scores[x] == max(scores):
                max_scores += [scores[x]]
                scores_ind += [x]'''

        scores_ind = [x for x in range(len(scores)) if scores[x] == max(scores)]

        if self.tiebreak == 'RANDOM':
            return random.choice(scores_ind)

        elif self.tiebreak == 'LEFT':
            return scores_ind[0]

        else:
            return scores_ind[-1]


    def scores_for(self, board):
        """takes a Board object board and determines the called AIPlayer‘s scores for
        the columns in board. Each column should be assigned one of the four possible scores"""

        scores = [50] * board.width
        
        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100

            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0

            elif self.lookahead == 0:
                scores[col] = 50

            else:
                board.add_checker(self.checker ,col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(board)
                scores[col] = 100 - max(opp_scores)
                max_score = max(opp_scores)


                board.remove_checker(col)

        return scores


    def next_move(self, board):
        """ overrides the next_move method that is inherited from Player."""

        self.num_moves += 1
        scores = self.scores_for(board)
        col = self.max_score_column(scores)
        return col
