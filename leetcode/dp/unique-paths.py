"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""
# 1st attempt: 78th percentile in speed. O(N^2) space
# Bottom up approach
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [ 1 for x in range(n) ] for y in range(m) ]
        
        for y in range(1, m):
            for x in range(1, n):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
        
        return dp[m-1][n-1]

# 2nd attempt: 78th percentile. O(N) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:        
        dp = [ 1 for x in range(n) ]
        
        for y in range(1, m):
            for x in range(1, n):
                dp[x] = dp[x-1] + dp[x] 
                
        
        return dp[n-1]

# 3rd attempt: Time limit exceeded
# Top down approach
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def helper(y, x):
            if y == 0 or x == 0:
                return 1
            else:
                return helper(y-1, x) + helper(y, x-1)

        return helper(m-1, n-1)