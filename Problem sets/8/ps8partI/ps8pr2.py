#
# ps8pr2.py (Problem Set 8, Problem 2)
#
# Conway's Game of Life
#
# Computer Science 111  
#

# IMPORTANT: This file is for your solutions to Problem 2.
# Your solutions to Problem 1 should go in ps8pr1.py instead.

from ps8pr1 import *
from gol_graphics import *

def has_left_right_neighbor(grid):
    """takes an existing generation of cells (the 2-D list grid), and that creates and returns a new generation with the same dimensions as grid,
    but with cell values determined as follows:
    •If an inner cell in grid has an alive left neighbor or an alive right neighbor or both,
    the corresponding cell in the new grid should be 1.
    •If an inner cell in grid has neither an alive left neighbor nor an alive right neighbor,
    the corresponding cell in the new grid should be 0.
    •The cells on the outer boundary of grid should be left alone.
    """
    height = len(grid)
    width = len(grid[0])
    new_grid = copy(grid)

    for r in range(1,height-1):
        for c in range(1,width-1):
            if grid[r][c+1] == 1 or grid[r][c-1] == 1:
                new_grid[r][c] = 1
            elif grid[r][c+1] == 0 and grid[r][c-1] == 0:
                new_grid[r][c] = 0
                
    return new_grid

def count_neighbors(cellr, cellc, grid):
    """returns the number of alive neighbors of the cell at position [cellr][cellc] in the specified grid.
    assuming that the indices cellr and cellc will always represent one of the inner cells of grid,
    and thus the cell will always have eight neighbors.
    """
    
    sum = 0
    r = cellr
    c = cellc
    if grid[r][c+1] == 1:
        sum += 1
    if grid[r][c-1] == 1:
        sum += 1
    if grid[r+1][c+1] == 1:
        sum += 1
    if grid [r+1][c-1] ==1:
        sum += 1
    if grid[r+1][c] ==1:
        sum += 1
    if grid[r-1][c-1]== 1:
        sum += 1  
    if grid[r-1][c+1] ==1:
        sum += 1
    if grid[r-1][c] ==1:
        sum += 1
        
    return sum    

def next_gen(grid):
    """takes a 2-D list called grid that represents the current generation of cells,
    and uses the rules of the Game of Life to create and return a new
    2-D list representing the next generation of cells
    """

    height = len(grid)
    width = len(grid[0])
    new_grid = copy(grid)

    for r in range(1,height-1):
        for c in range(1,width-1):
            alive_neighbor = count_neighbors(r, c, grid)
            if alive_neighbor < 2:
                new_grid[r][c] = 0
            if alive_neighbor >3:
                new_grid[r][c] = 0
            if new_grid[r][c] == 0 and alive_neighbor == 3:
                new_grid[r][c] = 1
                
    return new_grid
