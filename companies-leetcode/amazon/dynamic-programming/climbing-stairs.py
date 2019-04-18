"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
# Many different ways to solve this. Key intuition, is that the # of ways is going to 
# equal the number of ways you get can within 2 of the end + the number of ways you can get winthin
# 1 of the end. 
# Results in a simple Fibonacci like sequence. Can get faster time using special characteristics of Fib
# sequence. 
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return(0)
        trail, lead = 1, 1
        for _ in range(n-1):
            trail, lead = lead, trail + lead
        return(lead)