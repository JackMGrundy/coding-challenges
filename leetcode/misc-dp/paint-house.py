"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.
"""
# 1st attempt: 92nd percentile in speed.
# Very happy about this. Easy DP problem but still...I've been doing hard DP problems and 
# getting my butt kicked. Feels awseome to get this one quickly and correctly with a strong result
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        dp = costs[0]
        
        for row in costs[1:]:
            temp = [0] * len(dp)
            temp[0] = row[0] + min(dp[1], dp[2])
            temp[1] = row[1] + min(dp[0], dp[2])
            temp[2] = row[2] + min(dp[0], dp[1])
            dp = temp
        
        return min(dp)
        