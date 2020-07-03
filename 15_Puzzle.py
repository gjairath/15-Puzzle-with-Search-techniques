# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:03:35 2020

@author: garvi
"""

class PuzzleState():
    
    def __init__(self, numberArray):
        self.Array = numberArray
        self.blank, self.Cells = self.buildCells(self.Array)
        self.debugPrinter()
        
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
        '''
        actions = []
        for row, cols in Cells:
            if row != 0:
                actions.append('down')
            if row != 3:
                actions.append('up')
            
            if cols != 0:
                actions.append('right')
            if cols != 3:
                actions.append('left')
                
        return actions
        
    
    def debugPrinter(self):
        print (self.Cells)
        print (self.blank)
        
        

if __name__ == '__main__':
    
    numberArray = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    puzzle = PuzzleState(numberArray)
