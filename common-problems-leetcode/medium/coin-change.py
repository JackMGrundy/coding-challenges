"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

Accepted
185,162
Submissions
618,159
"""
# DP
# 43rd percentile 1436ms
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: 
            return 0
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        
        for i in range(len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[amount] if dp[amount] < float("inf") else -1


# DP - optimize for loops
# 81st percentile 1184 ms
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
                
        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return dp[-1] if dp[-1] < float("inf") else -1
                    