## The search algorithm itself -- it takes a problem, which will give it an initial state and the goal test,
##   the world state itself which gives it the successor states, and an evaluator that evaluates the quality
##   of a node on the search frontier

#  Priority queue code taken from Pacman project -- PriorityQueue supports
#      pop, isEmpty, and push/update
#
#  Client supplies
#    -- a WorldState; a WorldState implements the method successors()
#    -- a Problem which supplies the initial state and goal state checker
#    -- an Evaluator which supplies a method that evaluates a WorldState
#
#   The search function uses a SearchState which is a WorldState plus a sequence of 
#     actions (not examined by Search).   The search fringe is a priority 
#     queue of SearchState
#
#   Search returns a 2-tuple -- 
#    -- a sequence of actions
#    -- performance information:  process time used, number of nodes expanded, 
#         number of nodes skipped (because they were previously expanded), and 
#         the largest size of the fringe

from priorityQueue import PriorityQueue
import time

def aStarSearch(problem, evaluator, verbose=None, limit=None):
    startTime = time.process_time()
    fringe = PriorityQueue()
    max_fringe_size = 0
    visited = {}
    initialWorldState = problem.initial()
    initialValue = evaluator.value(initialWorldState, [])
    initialSearchState = SearchState(initialWorldState, [])
    fringe.update(initialSearchState, initialValue)
    numVisited = numSkipped = 0
    while (True):
        if len(fringe.heap) > max_fringe_size:
            max_fringe_size = len(fringe.heap)
        if fringe.isEmpty():
            return (None, (time.process_time() - startTime, numVisited, numSkipped, max_fringe_size))
        nextNode = fringe.pop()   # A search state (state, actions)
        numVisited += 1
        if (limit and numVisited > limit):
            return None
        if (verbose and numVisited % verbose == 0):
            print("Visited " + str(numVisited) + " world is " + str(nextNode._worldState))
            print("Skipped " + str(numSkipped) + " Fringe is size " + str(len(fringe.heap)))
            print("Evaluation is " + str(evaluator.value(nextNode._worldState, nextNode._actions)) + " with actions " + str(len(nextNode._actions)))
        if (problem.isGoal(nextNode.worldState())):
            return (nextNode._actions, (time.process_time() - startTime, numVisited, numSkipped, max_fringe_size))
        if (nextNode._worldState in visited):
            numSkipped += 1
        else:
            visited[nextNode.worldState()] = True
            successors = nextNode.worldState().successors()
            for successor in successors:
                state, action = successor
                actions = list(nextNode.actions())
                actions.append(action)
                newSS = SearchState(state, actions)
                newValue = evaluator.value(state, actions)
                fringe.update(newSS, newValue)
    raise "Impossible search execution path."

## Instances of SearchState go on the search fringe -- contains both a state and 
## list of actions so far

class SearchState:
    def __str__(self):
        return "{S " + str(self._worldState) + "/" + str(self._actions) + "}"
    
    def __init__(self, worldState, actions):
        self._worldState = worldState
        self._actions = actions
    
    def worldState(self):
        return self._worldState
    
    def actions(self):
        return self._actions

#####################################################################
##  Interfaces that must be implemented by the client

#  Method successors() returns a tuple:  (worldState, action)
class WorldState:
    def successors():
        raise "Not implemented"

# Problem must supply the initial state and a goal state checker       
class Problem:
    # Method initial returns a world state
    def initial(self):
        raise "Not implemented"
        
    # Method isGoal returns a boolean
    def isGoal(self, state):
        raise "Not implemented"

# Client provides g(s) and h*(s)        
# Evaluator provides the evaluator f(s) = g(s) + h*(s)
class Evaluator:
    def __init__(self, actionsCoster, goalEstimator):
        self._estimator = goalEstimator
        self._coster = actionsCoster
    def estimateToGoal(self, state):
        return self._estimator(state)
    def costSoFar(self, actions):
        return self._coster(actions)
    def value(self, state, actions):
        return self.estimateToGoal(state) + self.costSoFar(actions)
