#!/usr/bin/python3

import math
import os
import random
import re
import sys
import queue


def inBounds(j, i, l, w):
    return(j>=0 and j < l and i>=0 and i < w)

# Complete the countLuck function below.
def countLuck(matrix, k):
    # Find the start spot
    l = len(matrix)
    w = len(matrix[0])

    startI = 0
    startJ = 0
    for i in range(w):
        for j in range(l):
            if matrix[j][i]=="M":
                startI = i
                startJ = j
                break
            
    
    stack = queue.LifoQueue()
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    visited = [ [0 for x in range(w)] for k in range(l)]


    # Root node
    stack.put ( (startJ, startI) )

    curCell = None
    curI = 0
    curJ = 0
    neighbI = 0
    neighbJ = 0
    wandWaves = 0
    numNewNeighbor = 0
    # oldSize = 1
    # newSize = 1
    while not stack.empty():
        curCell = stack.get()
        curJ, curI = curCell 
        visited[curJ][curI] = 1
        # print("\ncur cell", curJ, ",", curI)

        # If the stack isn't empty, then a decision was made
        if numNewNeighbor>1: 
            # print("wavewand")
            wandWaves += 1

       # If goal, break
        if matrix[curJ][curI]=="*": break
            
        # Add all valid neighbors
        numNewNeighbor = 0
        for i in range(len(dx)):
            neighbI = curI + dx[i]
            neighbJ = curJ + dy[i]
            # print("check neighbor", neighbJ, ",", neighbI)

            if inBounds(neighbJ, neighbI, l, w) and visited[neighbJ][neighbI]==0 and matrix[neighbJ][neighbI]==".":
                # print("add neighbor", neighbJ, ",", neighbI)
                numNewNeighbor += 1
                stack.put( (neighbJ, neighbI) )

    print("wandWaves: ", wandWaves)
    if k==wandWaves: return("Impressed")
    else: return("Oops!")


if __name__=="__main__":
    k = 3
    matrix = [[".","X",".","X",".",".",".",".",".",".","X"],
              [".","X","*",".","X",".","X","X","X",".","X"],
              [".","X","X",".","X",".","X","M",".",".","."],
              [".",".",".",".",".",".","X","X","X","X","."]]
    
    matrix = [['*','.','.'],
              ['X','.','X'],
              ['.','.','M']]
    
    # matrix = ['*.M', '.X.']

    res = countLuck(matrix, k)
    print(res)
