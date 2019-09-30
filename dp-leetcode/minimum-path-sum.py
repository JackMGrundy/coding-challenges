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
# 108ms. 91 percentile in speed
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp = grid[:][:]
        
        for j in range(1, len(grid[0])):
            dp[0][j] += dp[0][j - 1]
        
        for i in range(1, len(grid)):
            dp[i][0] += dp[i - 1][0]
            for j in range(1, len(grid[0])):
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]
            


"""
Notes:

DP problem. Fill in the memo so that we know the cheapest path to any square.
The first row and the first column are simple...the only possible path is from the preceding square.
So we can fill in the first row and the first column of the memo by adding in order.

Then we can fill in the rest by taking the min of the value above and the value to the left. 

"""