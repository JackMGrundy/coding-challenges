"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

# 76ms. 25th percentile.
# Using O(triangle) space
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        dp = {(0,0):triangle[0][0]} #(level, index)
        bestVal = float("inf")
        for j in range(1, len(triangle)):
            for i in range(len(triangle[j])):
                if i == 0:
                    dp[(j,i)] = triangle[j][i] + dp[(j-1, i)]
                elif i == len(triangle[j])-1:
                    dp[(j,i)] = triangle[j][i] + dp[(j-1, i-1)]
                else:
                    dp[(j,i)] = triangle[j][i] + min(dp[(j-1,i-1)], dp[(j-1,i)])
                
                if j == len(triangle)-1:
                    bestVal = min(bestVal, dp[(j,i)])
                
        return bestVal if bestVal < float("inf") else triangle[0][0]



# 68ms. 80th percentile.
# Using O(N) space
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        
        lastRow = triangle[0]
        for j in range(1, len(triangle)):
            curRow = triangle[j]
            for i,val in enumerate(curRow):
                if i == 0:
                    curRow[i] += lastRow[i]
                elif i == len(curRow)-1:
                    curRow[i] += lastRow[i-1]
                else:
                    curRow[i] += min(lastRow[i-1], lastRow[i])
                    
            lastRow = curRow
        
        return min(curRow)