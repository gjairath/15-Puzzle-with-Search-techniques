# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:43:57 2020

@author: garvi

Utility file for various search algorithms

"""

import containers_utility as C
import time
import random

def breadthFirstSearch(problem):
    
    s = C.Queue()
    
    start = (problem.getStartState(), [])
    exploredFrontiers = set([])
    s.push(start)

    while s.isEmpty() is False:
        Actions = list()
        firstNode = s.pop()
        if (problem.isGoalState(firstNode[0])):
            print ('\n Solution Found\n')
            return firstNode[0], firstNode[1]
        
        if firstNode[0] not in exploredFrontiers:
            exploredFrontiers.add(firstNode[0])
            potentialWinners = problem.getSubLists(firstNode[0])

            for i in range(len(potentialWinners)):
                Nodes = potentialWinners[i][0]
                Actions = list(firstNode[1])
                Actions.append(potentialWinners[i][1])
                #print(Nodes)
                s.push((Nodes, Actions))
                
    return 'Failure'

def h1(state, problem=None):
 
    distance = 0
    for i in range(4):
        for j in range(4):
            if state.Cells[i][j] == 0: continue
            distance += abs(i - (state.Cells[i][j]/4)) + abs(j -  (state.Cells[i][j]%4));
    return distance

def h2(state, problem=None):

    misplaced = 0
    compare = 0
    for i in range(4):
        for j in range(4):
            if state.Cells[i][j] != compare:
                misplaced += 1
            compare += 1
    return misplaced

def aStarSearch(problem):

    #start1 = time.time()
    #print (start)
    
    s = C.PriorityQueue()
    
    start = (problem.getStartState(), [])
    
    exploredFrontiers = set([])
    s.push(start, problem.getCostOfActions(start[1]) + 0)

    while s.isEmpty() is False:
        Actions = list()
        firstNode = s.pop()
        
        if (problem.isGoalState(firstNode[0])):
            #something = time.time() - start1
            #print (something)
            return firstNode[0], firstNode[1]
        
        if firstNode[0] not in exploredFrontiers:
            exploredFrontiers.add(firstNode[0])
            potentialWinners = problem.getSubLists(firstNode[0])

            for i in range(len(potentialWinners)):
                Nodes = potentialWinners[i][0]
                Actions = list(firstNode[1])
                Actions.append(potentialWinners[i][1])
                #print(Nodes)
                s.push((Nodes, Actions), problem.getCostOfActions(Actions) + h2(Nodes, problem) + h1(Nodes,problem))


bfs = breadthFirstSearch
astar = aStarSearch

