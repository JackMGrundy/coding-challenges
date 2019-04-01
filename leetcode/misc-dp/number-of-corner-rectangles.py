"""
Given a grid where each entry is only 0 or 1, find the number of corner rectangles.

A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.

 

Example 1:

Input: grid = 
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
 

Example 2:

Input: grid = 
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
 

Example 3:

Input: grid = 
[[1, 1, 1, 1]]
Output: 0
Explanation: Rectangles must have four distinct corners.
 

Note:

The number of rows and columns of grid will each be in the range [1, 200].
Each grid[i][j] will be either 0 or 1.
The number of 1s in the grid will be at most 6000.
"""
# 1st attempt: Timeout. Correct, but too slow for the biggest test case.
import itertools

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        nRows = len(grid)
        nCols = len(grid[0])
        dpAbove = [ [0] if grid[0][i]==1 else [] for i in range(nCols)  ]
        res = 0

        for r in range(1, nRows):
            dpLeft = [0] if grid[r][0]==1 else []
            for c in range(1, nCols):
                if grid[r][c]==0: continue
                    
                posSols = list(itertools.product(dpAbove[c], dpLeft))
                for y, x in posSols:
                    if grid[y][x]: res += 1
                
                dpLeft.append(c)
                dpAbove[c].append(r)
        
        return res
                
                
# 2nd attempt: 29th percentile. Exact same as before, except using for loops instead of built in iterttols.
# I am surprised...I thought itertools would be faster. Maybe not due to having to allocate memory for
# the tuple pairs
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        nRows = len(grid)
        nCols = len(grid[0])
        dpAbove = [ [0] if grid[0][i]==1 else [] for i in range(nCols)  ]
        res = 0

        for r in range(1, nRows):
            dpLeft = [0] if grid[r][0]==1 else []
            for c in range(1, nCols):
                if grid[r][c]==0: continue
                      
                for y in dpAbove[c]:
                    for x in dpLeft:
                        if grid[y][x]: res += 1
                
                dpLeft.append(c)
                dpAbove[c].append(r)
        
        return res
                
                
# 3rd attempt: 99.6th percentile in speed
# Super cool solution
"""
Intuition:
Imagine we have two sets, one for each row in a pair. And each set contains the columns that contain
1's in its respective row. These rows give us all the info we need to get all of the rectangles that
can be formed between these two rows. Say there are two matching pairs...that means that we have 1 rectangle.
(picture one pair being one vertical side of the rectangle). Now say there are three pairs, then we 
can choose any two from this set of 3 to form a rectangle. Hence, we have pairs choose 2 different rectangles
between these rows. 

Given this simple intuition, we just itereate through the grid with two loops checking all pairs of rows. We
calculate the set's of 1's as we go, and use set operations and the n choose r forumla to add up the rectangles. 
"""
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        dp, res = [], 0
        
        for j in range(len(grid)):
            dp.append( {x for x,val in enumerate(grid[j]) if val}  )
            for i in range(j):
                pairs = len(dp[j] & dp[i])
                if pairs > 0:
                    # N choose 2
                    res += ( pairs * (pairs-1) ) // 2
        
        return res