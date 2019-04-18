#!/usr/bin/python3

import math
import os
import random
import re
import sys
import queue

# Complete the connectedCell function below.
def inBounds(j, i, w, l):
    return(i<w and i>=0 and j<l and j>=0)

def connectedCell(matrix):
    l = len(matrix)
    w = len(matrix[0])

    # Mark visited cells
    global visited
    visited = [ [0 for x in range(w)] for y in range(l)  ]

    biggestRegion = 0
    curRegion = 0
    curCell = None
    curI = 0
    curJ = 0
    neighbI = 0
    neighbJ = 0

    dx = [0, 1, -1, 0, 1, 1, -1, -1]
    dy = [1, 1, 1, -1, -1, 0, 0, -1]

    # Iterate through cells
    for i in range(w):
        for j in range(l):
            # if the next cell is a 1 and has not been visited
            if visited[j][i]==0 and matrix[j][i]==1:
                curRegion = 1
                # Complete a dfs to find all neighboring 1's
                stack = queue.LifoQueue()
                # Root node
                visited[j][i]=1
                stack.put((j, i))

                while not stack.empty():
                    curCell = stack.get()
                    curJ, curI = curCell

                    # Check neighbors for 1s and put on stack
                    for k in range(len(dx)):
                        neighbI = curI + dx[k]
                        neighbJ = curJ + dy[k]
                        # If the neighbor is inbounds, has not been visited, and is a 1
                        if inBounds(neighbJ, neighbI, w, l) and visited[neighbJ][neighbI]==0 and matrix[neighbJ][neighbI]==1:
                            # Increase size of current region
                            curRegion += 1
                            
                            # Mark as visited
                            visited[neighbJ][neighbI]=1
                            
                            # Add to stack
                            stack.put( (neighbJ, neighbI) )
                
                # Check if the processed region is the new biggest region
                if curRegion > biggestRegion:
                    biggestRegion = curRegion
    
    return(biggestRegion)

                        


if __name__=="__main__":
    matrix = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
    res = connectedCell(matrix)
    print(res)

