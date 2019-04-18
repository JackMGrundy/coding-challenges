#!/bin/python3

import math
import os
import random
import re
import sys
import queue

def knightNeighbors(i, j, cur, n):
    x, y = cur
    return filter(lambda v : v[0] >= 0 
      and v[1] >= 0 
      and v[0] < n 
      and v[1] < n,
      [
        [x + i, y + j],
        [x + i, y - j],
        [x - i, y + j],
        [x - i, y - j],
        [x + j, y + i],
        [x + j, y - i],
        [x - j, y + i],
        [x - j, y - i],
    ])

def knightBFS(i, j, n):
    """
    knightBFS: Given a chess knight that can move i squares in one dimension and j in the otehr in
    one turn, return how many moves it takes to move from (0, 0) to (n-1, n-1) on an n by n board.

    Args:
        i (int): squares the knight can move in one direction
        j (int): squares the knight can move in the other direction
        n (int): the size of the board (n by n)
    
    Returns:
        res (int): the minimum number of moves it takes the night to move from (0,0)
                    to (n-1, n-1)
    """
    target = (n-1, n-1)
    visited = [ [False]*n for _ in range(n) ]
    # Queue
    q = queue.Queue()
    q.put( [0, 0, 0] )
  
    while not q.empty():
        x, y, d = q.get()
        cur = (x,y)
        if cur==target: return(d)
        neighbors = [
            [x_i, y_i]
            for x_i, y_i in knightNeighbors(i, j, cur, n) 
            if visited[y_i][x_i] == False
        ]
        
        for x_i, y_i in neighbors:
            visited[y_i][x_i] = True 
            q.put( [x_i, y_i, d + 1])
            
    return(-1) 


# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):
    # (n, i, j)
    dists = []
    nextLine = []
    # Iterate through knights KnightL(i, j)
    for i in range(1, n):
        for j in range(1, n):
            dist = knightBFS(i, j, n)
            nextLine.append(dist)
        dists.append(nextLine)
        nextLine = []

    return(dists)


if __name__=="__main__":
    n = 5
    result = knightlOnAChessboard(n)
    print('\n'.join([' '.join(map(str, x)) for x in result]))