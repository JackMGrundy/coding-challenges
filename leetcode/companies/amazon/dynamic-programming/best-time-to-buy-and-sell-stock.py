"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
import sys

# 1st attempt: 3 passes over input. 10th percentile in speed
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) in [0, 1]: return(0)
        
        mins = []
        runningMin = float("inf")
        for price in prices:
            if price < runningMin: runningMin = price
            mins.append(runningMin)
    
        maxs = []
        runningMax = -float("inf")
        for price in prices[::-1]:
            if price > runningMax: runningMax = price
            maxs.append(runningMax)
        maxs.reverse()
        
        res = 0
        profits = [ x-y for (x,y) in zip(maxs, mins) ]
        return(max(0, max(profits)))

            
       



# 2nd attempt: 2 passes over input. 62nd percentile in speed
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) in [0, 1]: return(0)
        
        mins = []
        runningMin = float("inf")
        for price in prices:
            if price < runningMin: runningMin = price
            mins.append(runningMin)
    
        # maxs = []
        res = 0
        runningMax = -float("inf")
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > runningMax: runningMax = prices[i]
            profit = runningMax-mins[i]
            if profit > res:
                res = profit
            
        return(max(0, res))




# Attempt #3: 97th percentile in speed. Almost 0 storage.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        absMin = float("inf")
        profit = 0
        for price in prices:
            if price - absMin > profit:
                profit = price - absMin
            if price < absMin:
                absMin = price
        
        return(profit)
       
