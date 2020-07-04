# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:03:35 2020

@author: garvi
"""

import search_utility
import sys
import time 

class PuzzleState():
    
    def __init__(self, numberArray):
        self.Array = numberArray
        self.blank, self.Cells = self.buildCells(self.Array)
       # self.debugPrinter()
        
    def buildCells(self, Array):
        # The matrix is 4x4
        # We can use numpy to do this in 2 steps but fuck that
        cells = []
        iterator = 0
        for rows in range(4):
            subList = []
            for cols in range(4):
                subList.append(Array[iterator])
                if Array[iterator] == 0:
                    blank = rows, cols
                iterator += 1
            cells.append(subList)
        return blank, cells
    
    def result(self, move):
        """
          Returns a new eightPuzzle with the current state and blankLocation
        updated based on the provided move.

        The move should be a string drawn from a list returned by legalMoves.
        Illegal moves will raise an exception, which may be an array bounds
        exception.

        NOTE: This function *does not* change the current object.  Instead,
        it returns a new object.
        """
        row, col = self.blank
        if(move == 'up'):
            newrow = row - 1
            newcol = col
        elif(move == 'down'):
            newrow = row + 1
            newcol = col
        elif(move == 'left'):
            newrow = row
            newcol = col - 1
        elif(move == 'right'):
            newrow = row
            newcol = col + 1
        else:
            raise RuntimeError("Illegal Move")

        # Create a copy of the current eightPuzzle
        flat_list = [item for sublist in self.Cells for item in sublist]
    


        newPuzzle = PuzzleState(flat_list)
        # And update it to reflect the move
        newPuzzle.Cells[row][col] = self.Cells[newrow][newcol]
        newPuzzle.Cells[newrow][newcol] = self.Cells[row][col]
        newPuzzle.blankLocation = newrow, newcol

        return newPuzzle
    
    def printar(self):
        """
          Returns a display string for the maze
        """
        lines = []
        horizontalLine = ('-' * (13))
        lines.append(horizontalLine)
        for row in self.Cells:
            rowLine = '|'
            for col in row:
                if col == 0:
                    col = ' '
                rowLine = rowLine + ' ' + col.__str__() + ' |'
            lines.append(rowLine)
            lines.append(horizontalLine)
        return '\n'.join(lines)
    
    def potentialActions(self, Cells):
        
        # Takes: Cells, the matrix that has the values.
        # Returns: An array of legal moves.
        
        ''' 
        For eg, if you have a tile empty on the top left, you can only move right or down,
                provided you have not reached the goal state already
                
                If row == 0, col == 0, we cannot go up or left.
                If row == 0, col == 3, we cannot go up or right.
                If row == 3, col == 0, we cannot go down or left.
                
                Instead, append negated actions.
                
                for a point, say (2,2) all actions are legal.
                for a point, say (3,3), down and right are illegal.
                                 (0,1) up is illegal
        '''
        actions = []
        row, cols = self.blank
        if row != 0:
                actions.append('up')
        if row != 3:
                actions.append('down')
            
        if cols != 0:
                actions.append('left')
        if cols != 3:
                actions.append('right')
        return actions
        
    
    def isGoalState(self, puzzle):
        current = 0
        for row in range(4):
            for col in range(4):
                if current != self.Cells[row][col]:
                    return False
                current += 1
        return True
    
    def debugPrinter(self):
        print ('new Cells', self.Cells)
        

class SearchStuff:
    
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.expanded = 0 #Just for curiousty
        
    def getStartState(self):
        return self.puzzle
    
    def getSubLists(self, puzzle):
        
        subLists = []
        actions = puzzle.potentialActions(puzzle)
        for action in actions:
            subLists.append((puzzle.result(action), action, 1))
            self.expanded += 1
        return subLists
    
    def isGoalState(self, puzzle):
        return puzzle.isGoalState(puzzle)
    
    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        return len(actions)

def progressbar(progressVal, prefix=" ", size=60, file=sys.stdout):
    
    count = len(progressVal) #number queens
    def show(j):
        x = int(size * j / count) 
        file.write("%s%s%s %i/%i\r" % (prefix, "."*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(progressVal):
        yield item
        show(i+1)
        
    file.write("\n")
    file.flush()

if __name__ == '__main__':
    
    start = time.time()
    print ('\n\nKeep in mind 15 puzzle is NP hard')
    print ('A* is heavy on memory as well.')
    
    numberArray = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    numberArray2 = [4,5,6,1,2,3,7,8,9,10,11,12,13,14,15,0]
    puzzle = [1,2,3,6,5,4,7,8,9,10,11,12,13,14,15,0]

    puzzleProblem = PuzzleState(numberArray2)
    print ('\n\nInitial Puzzle\n', puzzleProblem.printar())
    # The puzzle object interactes with the BFS algorithm with the class above.
    search = SearchStuff(puzzleProblem)
    
    # The search object is what we actually do the BFS on.
    for i in progressbar(range(10), "Finding: ", 40): 
        time.sleep(0.1)
        puzzle, paths = search_utility.astar(search)
    print('\nNodes Expanded:', search.expanded)
    print('\n\nSolution:')
    print (puzzle.printar())
    
    print ('\nTime Taken in seconds:', time.time() - start)