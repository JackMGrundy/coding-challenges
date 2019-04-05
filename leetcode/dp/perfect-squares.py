"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

# 1st attempt: Timeout : ( can't pass the big test cases
# DP solution
"""
Intuition:

We know n. It is too time consuming to try all combinations of perfect squares that sum to n. 
We can reduce the problem to O(N^2) (loose bound), by using DP.

Idea: iterate through the integers up to n. Memoize min number of perfect squares required to sum
to the integer. For integer x, the min number must be equal to the minmium of dp[x-perfectSquare1], 
dp[x-perfectSquare2], etc. up to the largest perfectSquare less than x. Now we have bound the number
of constant operations for each number we check to O(N) (actually much less than that)...so a very
loose bound of O(N^2)
"""
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 4: return n
        dp = [float("inf")] * (n+2)
        dp[0:4] = [0, 1, 2, 3]
        
        for v in range(4, n+1):
            biggestSquare = 1
            
            while biggestSquare*biggestSquare <= v:
                dp[v] = min( dp[v], dp[v-biggestSquare*biggestSquare]+1 )
                biggestSquare += 1
        
        return dp[n]
            
            
# Attempt 2: 90th percentile in speed
# Same as above, but with a cool trick attributable to Stefan Pochmann.
# Only extend the dp array if needed...i.e. save the results between test cases
class Solution:
    dp = [0, 1, 2, 3]
    
    def numSquares(self, n: int) -> int:
        dp = self.dp
        
        while len(dp) <= n:
            for v in range(len(dp), n+1):
                biggestSquare = 1
                temp = float("inf")
        
                while biggestSquare*biggestSquare <= v:
                    temp = min( temp, dp[v-biggestSquare*biggestSquare]+1 )
                    biggestSquare += 1

                dp.append(temp)
            
        return dp[n]