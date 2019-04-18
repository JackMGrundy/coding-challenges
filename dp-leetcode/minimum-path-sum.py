"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
# 1st attempt: 88th percentile in speed
# Standard bottom up dp...get the best path to each square 1 by 1...build up to the final spot
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid[:][:]
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(1, n):
            dp[0][i] += dp[0][i-1]
        
        for y in range(1, m):
            dp[y][0] += dp[y-1][0]
            for x in range(1, n):
                dp[y][x] += min( dp[y-1][x], dp[y][x-1])
        
        return dp[m-1][n-1]