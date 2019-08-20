"""
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
 

You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:

Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
 

Example 2:

Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
 

Example 3:

Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
 

Hint: size of the given matrix will not exceed 50x50.
"""

# 7680 ms. 39th percentile.
# Plain BFS approach
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        def bfsToNextTree(forest, startY, startX, targetTree) -> tuple:
            queue = deque([ (startY, startX, 0) ])
            visitedSquares = set()
            while queue:
                y, x, stepsTaken = queue.popleft()
                if (y, x) in visitedSquares:
                    continue
                elif forest[y][x] == targetTree:
                    return (y, x, stepsTaken)
                else:
                    visitedSquares.add( (y, x) )
                    if y+1 < len(forest) and forest[y+1][x] != 0:
                        queue.append( (y+1, x, stepsTaken+1) )
                    if y-1 >= 0 and forest[y-1][x] != 0:
                        queue.append( (y-1, x, stepsTaken+1) )
                    if x+1 < len(forest[0]) and forest[y][x+1] != 0:
                        queue.append( (y, x+1, stepsTaken+1) )
                    if x-1 >= 0 and forest[y][x-1] != 0:
                        queue.append( (y, x-1, stepsTaken+1) )
        
            return (-1, -1, -1)
        
        
        treesToCut = [ x for row in forest for x in row if x > 1 ]
        treesToCut.sort(key=lambda x: -x)

        y, x, stepsTaken = 0, 0, 0
        while treesToCut:
            targetTree = treesToCut.pop()
            targetY, targetX, stepsToTarget = bfsToNextTree(forest, y, x, targetTree)
            if stepsToTarget == -1:
                return -1
            else:
                stepsTaken += stepsToTarget
                y, x = targetY, targetX
        
        return stepsTaken




# 3208ms. 82nd percentile.
# A* with manhattan distance heuristic. Thank you AI studies.
from heapq import *
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        treesToCut = [ x for row in forest for x in row if x > 1 ]
        treesToCut.sort(key=lambda x: -x)
        treeLocations = { tree:(y,x) for y,row in enumerate(forest) for x,tree in enumerate(row) if tree > 1 }
        
        def aStar(forest, targetTree, startY, startX, targetTreeY, targetTreeX) -> tuple:
            heap = []
            heappush(heap, (0, 0, startY, startX))
            visitedSquares = set()
            
            while heap:
                _, stepsTaken, y, x = heappop(heap)
                if (y, x) in visitedSquares:
                    continue
                elif forest[y][x] == targetTree:
                    return stepsTaken
                else:
                    visitedSquares.add( (y, x) )
                    if y+1 < len(forest) and forest[y+1][x] != 0:
                        heuristic = abs(targetTreeY - (y+1)) + abs(targetTreeX - x) + stepsTaken + 1
                        heappush(heap, (heuristic, stepsTaken+1, y+1, x) )
                    if y-1 >= 0 and forest[y-1][x] != 0:
                        heuristic = abs(targetTreeY - (y-1)) + abs(targetTreeX - x) + stepsTaken + 1
                        heappush(heap, (heuristic, stepsTaken+1, y-1, x) )
                    if x+1 < len(forest[0]) and forest[y][x+1] != 0:
                        heuristic = abs(targetTreeY - y) + abs(targetTreeX - (x+1)) + stepsTaken + 1
                        heappush(heap, (heuristic, stepsTaken+1, y, x+1) )
                    if x-1 >= 0 and forest[y][x-1] != 0:
                        heuristic = abs(targetTreeY - y) + abs(targetTreeX - (x-1)) + stepsTaken + 1
                        heappush(heap, (heuristic, stepsTaken+1, y, x-1) )
                        
            return -1
        

        y, x, stepsTaken = 0, 0, 0
        while treesToCut:
            targetTree = treesToCut.pop()
            targetTreeY, targetTreeX = treeLocations[targetTree]
            stepsToTarget = aStar(forest, targetTree, y, x, targetTreeY, targetTreeX)
            y, x = targetTreeY, targetTreeX
            stepsTaken += stepsToTarget

            if stepsToTarget == -1:
                return -1

        return stepsTaken