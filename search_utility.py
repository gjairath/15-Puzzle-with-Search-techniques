# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:43:57 2020

@author: garvi

Utility file for various search algorithms

"""



def breadthFirstSearch(problem):
    
    s = Queue()
    
    start = (problem.getStartState(), [])
    
    exploredFrontiers = set([])
    s.push(start)

    while s.isEmpty() is False:
        Actions = list()
        firstNode = s.pop()
        
        if (problem.isGoalState(firstNode[0])):
            return firstNode[1]
        
        if firstNode[0] not in exploredFrontiers:
            exploredFrontiers.add(firstNode[0])
            potentialWinners = problem.getSuccessors(firstNode[0])

            for i in range(len(potentialWinners)):
                Nodes = potentialWinners[i][0]
                Actions = list(firstNode[1])
                Actions.append(potentialWinners[i][1])
                #print(Nodes)
                s.push((Nodes, Actions))
    

def nullHeuristic(state, problem=None):
 
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    start1 = time.time()
    #print (start)
    
    s = util.PriorityQueue()
    
    start = (problem.getStartState(), [])
    
    exploredFrontiers = set([])
    s.push(start, problem.getCostOfActions(start[1]) + 0)

    while s.isEmpty() is False:
        Actions = list()
        firstNode = s.pop()
        
        if (problem.isGoalState(firstNode[0])):
            something = time.time() - start1
            print (something)
            return firstNode[1]
        
        if firstNode[0] not in exploredFrontiers:
            exploredFrontiers.add(firstNode[0])
            potentialWinners = problem.getSuccessors(firstNode[0])

            for i in range(len(potentialWinners)):
                Nodes = potentialWinners[i][0]
                Actions = list(firstNode[1])
                Actions.append(potentialWinners[i][1])
                #print(Nodes)
                s.push((Nodes, Actions), problem.getCostOfActions(Actions) + heuristic(Nodes, problem))


# Abbreviations
bfs = breadthFirstSearch
astar = aStarSearch

