"""
Given an integer matrix, find the length of the longest increasing path.        

From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is
not allowed).                                                                   

Example 1:                                                                      
Input: nums =                                                                   

[                                                                               
  [9,9,4],                                                                      
  [6,6,8],                                                                      
  [2,1,1]                                                                       
]                                                                               

Output: 4                                                                       

Explanation: The longest increasing path is [1, 2, 6, 9].                       

Example 2:                                                                      
Input: nums =                                                                   

[                                                                               
  [3,4,5],                                                                      
  [3,2,6],                                                                      
  [2,2,1]                                                                       
]                                                                               

Output: 4                                                                       

Explanation:  The  longest increasing path is [3, 4, 5, 6]. Moving diagonally is
not allowed.                                                                    

"""
# 608ms 29 percentile.
# Manual caching
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: 
            return 0
        
        dp = [ [ 0 for j in range(len(matrix[0])) ] for i in range(len(matrix)) ]
        def backtrack(i, j):
            if not dp[i][j]:
                neighbors = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
                for neighbor in neighbors:
                    nI, nJ = neighbor
                    if 0 <= nI < len(matrix) and 0 <= nJ < len(matrix[0]) and matrix[i][j] < matrix[nI][nJ]:
                        dp[i][j] = max(dp[i][j], backtrack(nI, nJ))
                dp[i][j] += 1
            
            return dp[i][j]

        return max([ backtrack(i, j) for i,_ in enumerate(matrix) for j,_ in enumerate(matrix[0]) ])


# 496ms. 73 percentile.
# Built in caching
from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: 
            return 0
        
        @lru_cache(maxsize=None)
        def backtrack(i, j):
            neighbors = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            res = 0
            for neighbor in neighbors:
                nI, nJ = neighbor
                if 0 <= nI < len(matrix) and 0 <= nJ < len(matrix[0]) and matrix[i][j] < matrix[nI][nJ]:
                    res = max(res, backtrack(nI, nJ))
            res += 1
            return res

        return max([ backtrack(i, j) for i,_ in enumerate(matrix) for j,_ in enumerate(matrix[0]) ])

"""
Notes:

Approach 1)
We can get a working answer by just using backtracking with memoization. 

To see how the memoization works:
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 

Once get to the bottom left 2, we will have already stored memo[(1, 0)] = 1. This will shorten
the process of finding memo[(2, 0)] = 2, in turn memo[(2, 1)] = 3, and finally memo[(2, 2)] = 4.

"""