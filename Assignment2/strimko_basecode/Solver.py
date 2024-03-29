# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:46:15 2019

@author: hanks
"""

##  This method is called from Boards.py -- the two inputs are
##    -- initial cell assignments, a list of length N where N is 
##       the problem size (number of rows = number of columns = number
##       of streams = length of each stream).  For example, for a game
##       of size three,  this assigns the value i to the cells on 
##       the diagonal:   [[1,0,0], [0,2,0], [0,0,3]]   -- the value
##       of 0 means the initial value for that cell should be unassigned.
##
##    -- streams:  a list of length N, each element is a stream, which 
##       is a list of N coordinates.  For example for N=3:
##          [[(1,1), (2,2), (1,3)], [(1,2), (2,3), (3,3)], [(2,1), (3,1), (3,2)]]
##       Notice that every legal coordinate appears in a stream exactly
##       once, and that the streams are "contiguous" in the sense that 
##       every coordinate is connected to another coordinate either by
##       a row, a column or a diagonal
##
##  Indexing convention for the initial cell assignments:
##     For example for the initial [[a, b, c], [d, e, f], [g, h, i]]
##         The "a" position is column 1 row 1, the "f" position is column 3 row 2, the 
##         "g" position is column 1 row 3.
##
##  Indexing convention for the streams:  (col, row) where (1,1) is at the upper left, 
##    (2,1) is one to the right, (1,2) is one down, and (N,N) is at the 
##    lower right.   As another example, the coordinates of the first row from 
##    left to right on a 5x5 board are [(1,1), (2,1), (3,1), (4,1), (5,1)]
##
##  The return value is exactly the return value from the Python constraints library method
##   getSolutions -- a list of solutions;  each solution is a dictionary 
##   with a key being a coordinate and the value being a value assigned
##   to the cell with that coordinate

from constraint import *

def solveProblem(inits, streams):
    # When you actually solve a CSP, use this code, which calls the Python constraints library
    #     problem = Problem()
    #     buildSolution(inits, streams, problem)
    #     return problem.getSolutions()
	return dummyExampleNonSolution(len(inits))


##  DO NOT COPY THIS CODE!  It is not a solution, it is just 
##  an exmaple and will make the GUI work.  It assigns the value 1
##  to every cell in the problem, which is why it does not need
##  the problem or the inits or the streams
    
def dummyExampleNonSolution(size):
    nonSolution = {}
    for i in range(1, size+1):
        for j in range(1, size+1):
            nonSolution[(i,j)] = 1
    return [nonSolution]
    