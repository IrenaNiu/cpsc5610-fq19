#Feb-07-2014
#Developed by
# Daniel Lucas Thompson & Bikramjit Banerjee
# School of Computing
# The University of Southern Mississippi

#License
#====================================================================
#This is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with TraceGen.  If not, see <http://www.gnu.org/licenses/>. 
#===================================================================

import copy
import thread
import sys

from Solver import *

class Board():
    def __init__(self, size, gui, id):
        self.size = size
        self.pause = True
        self.solve = False
        self.gui = gui
        self.boardlist = {}
        self.loadBoards()
        self.boardLock = thread.allocate_lock()
        self.board = self.boardlist[id]
        self.killThread = False

    #  Input to this method is (a) a list of initial assignments and
    #  (b) a list of streams.   The solver must return a list of solutions,
    #  and each solution is a dictionary with key being a tuple of the 
    #  form (row, col) and the value is the number to be assigned to that
    #  cell.
    
    def resolveStrimko(self, inits, streams):
        solutions = solveProblem(inits, streams)
        if len(solutions) > 0:
            solution = solutions[0]
            for a in solution:
                self.answer((a, solution[a]))
        else:
            print "No solutions"
        return

    def answer(self, cell):
        #The answer cell is returned by the SolveStrimko algorithm.
        #The thread is paused in a loop to wait for the user to click
        #the solve or the next button.
        #The passed cell is then updated to the GUI class and the solved
        #cell is highlighted on the board.
        if self.solve:
            self.pauseGame()
        while self.pause:
            if self.killThread:
                #kills the thread if the board is reset so the object can destruct
                return
            #waits for user to click solve or next
            pass
        x = cell[0][0] - 1
        y = cell[0][1] - 1
        ans = cell[1]
        #updates the answer board while locked because the GUI can possibly be using it
        self.boardLock.acquire()
        self.board[0][y][x] = ans
        self.boardLock.release()
        #updates the currently solved cell while locked because the GUI can possibly be using it
        self.gui.cellLock.acquire()
        self.gui.currentCell = (x+1, y+1)
        self.gui.cellLock.release()
        self.gui.writeNumbers()
        self.pause = True

# =============================================================================
    def runGame(self):
        #Generates the needed conjunctions, disjunctions, and initial facts
        #and passes them into the SolveStrimko algorithm.
        #a = self.generateDisjunctions()
        #cd = self.generateChainDisjunctions()
        #b = self.getInitialFacts()
        #a.extend( cd )
        try:
            thread.start_new_thread(self.resolveStrimko, (self.board))
        except:
            print "Error running game: ", sys.exc_info()[0]

    def pauseGame(self):
        self.pause = False

    def solveGame(self):
        self.solve = True
        self.pause = False

    def resetBoard(self, id):
        self.board = self.boardlist[id]

    def loadBoards(self):
        #Loads the data for each board
        def cop(answers, chains):
            return (copy.deepcopy(answers), copy.deepcopy(chains))
        self.boardlist["4_1"] = cop(board4_1, chains4_1)
        self.boardlist["4_2"] = cop(board4_2, chains4_2)
        self.boardlist["4_3"] = cop(board4_3, chains4_3)
        self.boardlist["4_4"] = cop(board4_4, chains4_4)
        self.boardlist["4_5"] = cop(board4_5, chains4_5)
        self.boardlist["5_1"] = cop(board5_1, chains5_1)
        self.boardlist["5_2"] = cop(board5_2, chains5_2)
        self.boardlist["5_3"] = cop(board5_3, chains5_3)
        self.boardlist["5_4"] = cop(board5_4, chains5_4)
        self.boardlist["5_5"] = cop(board5_5, chains5_5)
        self.boardlist["5_6"] = cop(board5_6, chains5_6)
        self.boardlist["5_7"] = cop(board5_7, chains5_7)
        self.boardlist["5_8"] = cop(board5_8, chains5_8)
        self.boardlist["5_9"] = cop(board5_9, chains5_9)
        self.boardlist["5_10"] = cop(board5_10, chains5_10)
        self.boardlist["6_1"] = cop(board6_1, chains6_1)
        self.boardlist["6_2"] = cop(board6_2, chains6_2)
        self.boardlist["6_3"] = cop(board6_3, chains6_3)
        self.boardlist["6_4"] = cop(board6_4, chains6_4)
        self.boardlist["6_5"] = cop(board6_5, chains6_5)
        self.boardlist["7_1"] = cop(board7_1, chains7_1)
        self.boardlist["7_2"] = cop(board7_2, chains7_2)
        self.boardlist["7_3"] = cop(board7_3, chains7_3)



##############################################################
#Board Data; add your own boards if you want
##############################################################

###########
#4x4 Boards
###########

#Set 181 Easy
board4_1 = [[0,0,3,0],
            [0,0,0,0],
            [2,0,0,0],
            [0,0,0,1]]

chains4_1 = [[(1,1),(2,2),(3,3),(3,2)],
             [(2,1),(3,1),(4,1),(4,2)],
             [(2,3),(1,2),(1,3),(1,4)],
             [(2,4),(3,4),(4,4),(4,3)]]

#Set 178 Easy
board4_2 = [[0,0,1,0],
            [0,0,0,0],
            [3,0,4,0],
            [0,0,0,0]]

chains4_2 = [[(1,1),(2,2),(1,3),(2,4)],
             [(1,2),(2,1),(3,2),(4,1)],
             [(1,4),(2,3),(3,4),(4,3)],
             [(3,1),(4,2),(3,3),(4,4)]]

#Set 176 Easy
board4_3 = [[3,0,0,0],
            [0,0,4,0],
            [0,0,0,0],
            [0,1,0,0]]

chains4_3 = [[(1,1),(2,1),(2,2),(1,2)],
             [(1,3),(2,4),(3,4),(4,3)],
             [(1,4),(2,3),(3,2),(4,1)],
             [(3,1),(4,2),(3,3),(4,4)]]

#Set 180 Easy
board4_4 = [[0,0,0,1],
            [0,0,2,0],
            [0,4,0,0],
            [0,0,0,0]]

chains4_4 = [[(1,1),(2,2),(1,3),(3,1)],
             [(1,2),(2,1),(3,2),(4,1)],
             [(1,4),(2,3),(3,4),(4,3)],
             [(4,4),(3,3),(2,4),(4,2)]]

#set 169 Easy
board4_5 = [[0,0,0,2],
            [0,0,0,0],
            [0,0,0,0],
            [4,0,0,1]]

chains4_5 = [[(1,1),(2,2),(3,3),(4,4)],
             [(1,2),(2,1),(3,1),(4,2)],
             [(1,3),(2,4),(3,4),(4,3)],
             [(1,4),(2,3),(3,2),(4,1)]]

###########
#5x5 Boards
###########

#Set 143 Hard
board5_1 = [[0,4,0,2,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,0,3,0]]

chains5_1 = [[(2,2),(1,1),(2,1),(3,1),(4,2)],
             [(2,3),(1,2),(1,3),(1,4),(2,5)],
             [(1,5),(2,4),(3,3),(3,2),(4,1)],
             [(3,5),(4,4),(4,3),(5,2),(5,1)],
             [(3,4),(4,5),(5,5),(5,4),(5,3)]]

#set 144 Medium
board5_2 = [[0,0,0,0,0],
            [0,0,1,0,0],
            [0,3,5,0,0],
            [4,5,0,0,0],
            [0,0,0,0,0]]

chains5_2 = [[(1,1),(1,2),(1,3),(1,4),(2,4)],
             [(1,5),(2,5),(3,5),(4,5),(3,4)],
             [(2,3),(2,2),(2,1),(3,1),(4,1)],
             [(4,2),(3,2),(3,3),(4,4),(5,5)],
             [(5,1),(5,2),(5,3),(5,4),(4,3)]]

#set 23 Medium
board5_3 = [[0,0,4,0,0],
            [0,0,0,0,0],
            [0,0,3,0,2],
            [0,0,0,0,0],
            [0,0,1,0,0]]

chains5_3 = [[(1,1),(2,2),(3,2),(4,2),(5,3)],
             [(2,1),(1,2),(2,3),(3,3),(2,4)],
             [(1,3),(1,4),(1,5),(2,5),(3,5)],
             [(3,1),(4,1),(5,1),(5,2),(4,3)],
             [(3,4),(4,4),(5,4),(5,5),(4,5)]]

#set 23 Easy
board5_4 = [[0,0,0,0,5],
            [0,0,0,1,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,2,3,0,0]]

chains5_4 = [[(1,1),(2,2),(3,3),(4,3),(4,2)],
             [(1,3),(1,2),(2,1),(3,1),(3,2)],
             [(2,3),(1,4),(1,5),(2,4),(3,5)],
             [(2,5),(3,4),(4,5),(5,5),(5,4)],
             [(4,1),(5,1),(5,2),(5,3),(4,4)]]

#set 23 Medium
board5_5 = [[0,0,5,0,0],
            [0,4,0,1,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,3,0,0]]

chains5_5 = [[(1,1),(1,2),(1,3),(1,4),(1,5)],
             [(2,1),(3,2),(3,3),(2,4),(2,5)],
             [(2,2),(3,1),(4,2),(5,1),(4,1)],
             [(2,3),(3,4),(3,5),(4,4),(4,3)],
             [(4,5),(5,5),(5,4),(5,3),(5,2)]]

#set 142 Easy
board5_6 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [4,1,0,2,3],
            [0,0,0,0,0],
            [0,0,0,0,0]]

chains5_6 = [[(2,1),(1,1),(1,2),(2,3),(3,2)],
             [(3,1),(2,2),(1,3),(1,4),(2,5)],
             [(1,5),(2,4),(3,4),(4,4),(4,3)],
             [(3,5),(4,5),(5,5),(5,4),(5,3)],
             [(3,3),(4,2),(5,2),(5,1),(4,1)]]

#set 139 Medium
board5_7 = [[0,0,0,3,0],
            [0,0,2,0,5],
            [0,0,0,1,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]

chains5_7 = [[(1,1),(2,1),(3,1),(2,2),(2,3)],
             [(1,2),(1,3),(1,4),(2,5),(3,4)],
             [(1,5),(2,4),(3,3),(4,2),(5,1)],
             [(5,2),(4,1),(3,2),(4,3),(5,4)],
             [(5,3),(4,4),(3,5),(4,5),(5,5)]]

#set 16 Medium
board5_8 = [[0,3,0,0,0],
            [0,2,0,0,0],
            [0,0,0,4,0],
            [0,0,0,5,0],
            [0,0,1,0,0]]

chains5_8 = [[(1,1),(1,2),(1,3),(1,4),(1,5)],
             [(2,1),(3,2),(3,3),(2,4),(2,5)],
             [(3,1),(2,2),(2,3),(3,4),(3,5)],
             [(5,1),(4,1),(4,2),(4,3),(4,4)],
             [(5,2),(5,3),(5,4),(5,5),(4,5)]]

#set 22 Medium
board5_9 = [[0,0,0,0,0],
            [3,0,0,5,1],
            [0,0,0,0,0],
            [2,0,0,0,0],
            [0,0,0,4,0]]

chains5_9 = [[(1,1),(2,2),(3,3),(4,4),(5,5)],
             [(1,2),(2,3),(2,4),(3,4),(4,5)],
             [(1,3),(1,4),(1,5),(2,5),(3,5)],
             [(2,1),(3,2),(4,2),(4,3),(5,4)],
             [(3,1),(4,1),(5,1),(5,2),(5,3)]]

#set 142 Medium
board5_10 = [[0,0,0,0,0],
            [0,0,3,0,0],
            [0,5,2,1,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]

chains5_10 = [[(1,1),(2,2),(3,3),(3,4),(2,5)],
             [(1,2),(2,1),(3,1),(4,1),(5,2)],
             [(1,5),(1,4),(1,3),(2,3),(2,4)],
             [(3,5),(4,5),(5,5),(5,4),(4,4)],
             [(5,1),(4,2),(3,2),(4,3),(5,3)]]

###########
#6x6 Boards
###########

#Set 180 Hard
board6_1 = [[5,0,0,0,0,0],
            [0,0,0,0,0,6],
            [0,4,0,0,0,0],
            [0,0,3,0,0,0],
            [0,0,0,0,2,0],
            [0,0,0,1,0,0]]

chains6_1 = [[(1,1),(2,2),(3,3),(3,4),(4,4),(5,5)],
             [(2,1),(1,2),(1,3),(2,4),(2,5),(1,4)],
             [(2,3),(3,2),(3,1),(4,1),(5,2),(5,3)],
             [(5,1),(6,1),(6,2),(6,3),(6,4),(6,5)],
             [(1,5),(1,6),(2,6),(3,6),(4,6),(3,5)],
             [(4,2),(4,3),(5,4),(4,5),(5,6),(6,6)]]

#set 178 hard
board6_2 = [[0,6,0,0,0,0],
            [0,0,1,0,0,0],
            [0,0,0,4,0,0],
            [0,0,0,0,2,0],
            [0,0,0,0,0,3],
            [0,0,0,0,0,4]]

chains6_2 = [[(1,1),(2,2),(3,3),(4,4),(5,5),(6,5)],
             [(1,2),(2,1),(3,1),(4,1),(5,2),(6,3)],
             [(1,3),(2,3),(3,4),(3,5),(3,6),(4,6)],
             [(4,3),(3,2),(4,2),(5,1),(6,1),(6,2)],
             [(1,4),(1,5),(1,6),(2,6),(2,5),(2,4)],
             [(5,3),(6,4),(5,4),(4,5),(5,6),(6,6)]]

#set 169 hard
board6_3 = [[0,5,0,0,0,0],
            [0,0,0,0,2,0],
            [0,0,1,0,0,0],
            [0,0,0,0,0,0],
            [0,6,0,0,3,0],
            [0,0,0,0,0,4]]

chains6_3 = [[(1,1),(2,1),(3,2),(3,1),(4,1),(5,1)],
             [(2,2),(1,2),(1,3),(2,3),(3,4),(4,3)],
             [(1,4),(2,5),(1,6),(2,6),(3,6),(4,6)],
             [(1,5),(2,4),(3,5),(4,5),(5,6),(6,5)],
             [(3,3),(4,2),(5,2),(6,1),(6,2),(6,3)],
             [(4,4),(5,4),(5,3),(6,4),(5,5),(6,6)]]


#set 182 Hard
board6_4 = [[0,0,0,0,0,0],
            [0,3,0,5,0,0],
            [0,0,2,0,6,0],
            [0,0,1,2,0,0],
            [0,0,0,0,2,0],
            [0,0,0,0,0,0]]

chains6_4 = [[(1,1),(2,2),(3,3),(4,3),(3,4),(2,5)],
             [(1,4),(1,3),(1,2),(2,1),(3,1),(4,2)],
             [(4,1),(5,1),(6,1),(6,2),(6,3),(5,2)],
             [(3,2),(2,3),(2,4),(3,5),(4,5),(5,5)],
             [(1,5),(1,6),(2,6),(3,6),(4,6),(5,6)],
             [(5,3),(4,4),(5,4),(6,4),(6,5),(6,6)]]

#set 185 hard
board6_5 = [[1,0,5,3,0,4],
            [0,0,0,0,0,0],
            [5,0,0,0,0,3],
            [2,0,0,0,0,6],
            [0,0,0,0,0,0],
            [4,0,2,6,0,1]]

chains6_5 = [[(1,1),(2,2),(3,3),(4,4),(3,5),(2,6)],
             [(2,1),(3,2),(4,3),(3,4),(4,5),(5,6)],
             [(3,1),(4,1),(5,1),(5,2),(5,3),(4,2)],
             [(2,3),(1,2),(1,3),(1,4),(1,5),(2,4)],
             [(1,6),(2,5),(3,6),(4,6),(5,5),(5,4)],
             [(6,1),(6,2),(6,3),(6,4),(6,5),(6,6)]]

###########
#7x7 Boards
###########

#set 172 hard
board7_1 = [[0,0,0,0,0,0,0],
            [5,2,7,0,0,0,0],
            [0,0,0,0,4,2,7],
            [0,0,0,0,0,0,0],
            [6,4,1,0,0,0,0],
            [0,0,0,0,1,6,5],
            [0,0,0,0,0,0,0]]

chains7_1 = [[(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)],
             [(2,1),(3,1),(4,1),(4,2),(5,3),(6,4),(6,5)],
             [(2,2),(3,3),(3,4),(3,5),(4,4),(5,5),(6,6)],
             [(3,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,7)],
             [(5,1),(6,2),(6,3),(7,4),(7,3),(7,2),(7,1)],
             [(5,6),(4,7),(5,7),(6,7),(7,7),(7,6),(7,5)],
             [(6,1),(5,2),(4,3),(5,4),(4,5),(3,6),(4,6)]]

#set 177 hard
board7_2 = [[0,0,0,0,0,0,0],
            [0,0,3,0,4,0,0],
            [0,0,0,0,0,0,0],
            [4,0,1,5,7,0,6],
            [0,0,0,0,0,0,0],
            [0,0,2,1,5,0,0],
            [0,0,0,0,0,0,0]]

chains7_2 = [[(3,1),(2,1),(1,1),(1,2),(1,3),(2,4),(3,4)],
             [(2,3),(2,2),(3,2),(4,1),(5,1),(6,1),(7,1)],
             [(1,4),(1,5),(1,6),(2,6),(3,5),(4,4),(5,3)],
             [(4,3),(3,3),(4,2),(5,2),(6,2),(7,2),(6,3)],
             [(2,5),(3,6),(4,5),(5,4),(6,5),(7,5),(7,4)],
             [(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(5,6)],
             [(7,6),(7,7),(6,6),(5,5),(4,6),(6,4),(7,3)]]

#set 175 hard
board7_3 = [[0,0,2,0,4,0,0],
            [0,5,0,0,0,2,0],
            [0,0,0,0,0,0,6],
            [0,7,0,0,0,5,0],
            [0,0,0,0,0,0,7],
            [0,6,0,0,0,4,0],
            [0,0,1,0,2,0,0]]

chains7_3 = [[(1,1),(2,1),(3,1),(4,1),(4,2),(5,2),(5,3)],
             [(2,2),(1,2),(1,3),(1,4),(1,5),(1,6),(2,6)],
             [(1,7),(2,7),(3,7),(4,7),(5,7),(6,6),(6,7)],
             [(3,5),(2,4),(2,3),(3,2),(4,3),(3,3),(3,4)],
             [(7,1),(6,1),(5,1),(6,2),(6,3),(5,4),(4,4)],
             [(7,2),(7,3),(6,4),(7,4),(7,5),(7,6),(7,7)],
             [(2,5),(3,6),(4,5),(4,6),(5,6),(5,5),(6,5)]]


