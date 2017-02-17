 #Problem Set 10 Problem 1
# Abdulshaheed Alqunber
# ASQ@BU.EDU
# Partner: Ali Salem
# alisalem@bu.edu


class Board:
    
    def __init__(self, height, width):
        '''constructs a new Board object by initializing the following three attributes:
    • an attribute height
    • an attribute width
    • an attribute slots that stores a reference to a two-dimensional list with height rows and width columns
        '''
        
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        for h in range(self.width*2+1):
            s += '-'
        # and the numbers underneath it.
        s += '\n'
        for n in range(self.width):
            s += ' '
            s += str(n)
        return s
    
    def add_checker(self, checker, col):
        """ accepts two inputs:
    • checker, a one-character string that specifies the checker to add to the board (either 'X' or 'O').
    • col, an integer that specifies the index of the column to which the checkershould be added
    and that adds checker to the appropriate row in column col of the board.
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
    
        # put the rest of the method here
        z = True
        for x in range(self.height):
            
            if self.slots[self.height-x-1][col] == ' ' and z == True:
                self.slots[self.height-x-1][col] = checker
                z = False

    def reset(self):
        '''
    reset the Board object on which it is called by setting all slots to contain a space character.
    '''
        self.__init__(self.height, self.width)

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """

        checker = "X"

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
                
    def can_add_to(self, col):
        ''' returns True if it is valid to place a checker in the column
    col on the calling Board object. Otherwise, it should return False.
        '''
        for x in range(self.height):
            if 0 <= col < self.width and self.slots[x][col] == ' ':
                return True
        return False


    def is_full(self):
        '''
        returns True if the called Board object is completely full of checkers,
        and returns False otherwise.
        '''
        for x in range(self.width):
            if Board.can_add_to(self, x) == True:
                return False
        return True
            
    def remove_checker(self, col):
        '''removes the top checker from column col of the called Board object.
        If the column is empty, then do nothing.'''

        if self.slots[self.height-1][col] != ' ':
            if 0 <= col < self.width and self.slots[0][col] != ' ':
                self.slots[0][col] = ' '
            else:
                z = True
                for x in range(self.height):
                    
                    if self.slots[self.height-x-1][col] == ' ' and z == True:
                        self.slots[self.height-x][col] = ' '
                        z = False

    def is_win_for(self, checker):
        '''
    accepts a parameter checker that is either 'X' or 'O',
    and returns True if there are four consecutive slots
    containing checker on the board. Otherwise, it should return False
        '''

        assert(checker == 'X' or checker == 'O')
        
        #Horizontal 
        for r in range(self.height):
            for c in range(self.width-3):
                h1 = self.slots[r][c+1]
                h2 = self.slots[r][c+2]
                h3 = self.slots[r][c+3]
                if self.slots[r][c] == checker:
                    if h1 == checker and h2 == checker and h3 == checker:
                        return True

        #Vertical
        for r in range(self.height-3):
            for c in range(self.width):
                v1 = self.slots[r+1][c]
                v2 = self.slots[r+2][c]
                v3 = self.slots[r+3][c]
                if self.slots[r][c] == checker:
                    if v1 == checker and v2 == checker and v3 == checker:
                        return True

        #up_diagonal
        for r in range(3, self.height):
            for c in range(self.width-3):
                ud1 = self.slots[r-1][c+1]
                ud2 = self.slots[r-2][c+2]
                ud3 = self.slots[r-3][c+3]
                if self.slots[r][c] == checker:
                    if ud1 == checker and ud2 == checker and ud3 == checker:
                        return True

        #down_diagonal
        for r in range(self.height-3):
            for c in range(self.width-3):
                dd1 = self.slots[r+1][c+1]
                dd2 = self.slots[r+2][c+2]
                dd3 = self.slots[r+3][c+3]
                if self.slots[r][c] == checker:
                    if dd1 == checker and dd2 == checker and dd3 == checker:
                        return True
        return False
