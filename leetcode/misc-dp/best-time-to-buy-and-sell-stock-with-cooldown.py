"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
# 93rd percentile in speed.
# Couldn't figure this out. Learned a very cool solution.
# I haven't practiced DP problems where the states are abstract like this...
# very cool and awesome learning experience.
"""
Intuition:
Like with a path finding problem, the idea is to figure out for a given time and state,
what is the best way you could possibly get to the point. If you can do this step by step
and for all possible time/state pairs, then at the end, you must have the best path and its cost
recorded.

The only thing different in this problem, is that the states are locations in a grid or list...they
are the states of holding, notholding, or being in a cooldown state. 

Given this, it is simple to identify the solution.

Note the following about a given time step:
1) Hold state: to enter this, you must be either continuing from holding in the previous step or
buying as of this step

2) notHold state: you must either be continuing to not hold or "paying" the lost step for a cooldown

3) Cooldown state: you only enter this if you sell

Given these transitions, you can identify the best time/state combinations for each step. 
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, notHold, cooldown = -float('inf'), 0, -float('inf')
        for p in prices:
            hold = max(hold, notHold-p)
            notHold = max(notHold, cooldown)
            cooldown = hold+p
        return max(notHold, cooldown)