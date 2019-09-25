"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you 
how many days you would have to wait until a warmer temperature. If there is no future day for which this 
is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be 
[1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in 
the range [30, 100].

Accepted
90.6K
Submissions
149.2K
"""

# 528ms. 85 percentile
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0]*len(T)
        
        for today,todaysTemp in enumerate(T):
            while stack and T[stack[-1]] < todaysTemp:
                coolerPastDay = stack.pop()
                res[coolerPastDay] = today - coolerPastDay
            
            stack.append(today)
        
        return res

"""
Notes:

The most intuitive answer with a stack involves traversing the list backwards. We can speed things up
by traversing forwards. The stack maintains the invariant that the days recorded in the stack get
hotter as you go from top to bottom. 

When we see a day that is hotter than the top of the stack, then we know that we can record the answer for
that day on top of the stack...its answer is today - coolerDate. This must be the first day after the cooler
day that is hotter, because otherwise we would have popped the cooler day sooner. 

"""