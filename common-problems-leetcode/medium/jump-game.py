"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
Accepted
308,160
Submissions
944,912
"""
# O(N^2). Times out on the last two test cases:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        dp = [False]*len(nums)
        dp[0] = True
        
        for i in range(len(dp)):
            if dp[i]:
                for j in range(i + nums[i] + 1):
                    if j < len(nums):
                        dp[j] = True
        
        return dp[-1]


# O(N) 
# 104ms. 66 percentile.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPosition = len(nums) - 1
        
        for i in range(lastPosition, -1, -1):
            if lastPosition <= i + nums[i]:
                lastPosition = i
        
        return lastPosition == 0

"""
Notes:
There are obvious but ironically complicated dp solutions. These also timeout. They are O(N^2) in that
in the worst case scenario we scan N elements for each element. They are also O(N) space.
The first answer above times out for this reason. 


The smarter N solution is actually straightforwards...
Example:

Index	0	1	2	3	4	5	6
nums	2	4	2	1	0	2	0
memo	G	G	B	B	B	G	G

We maintain a single value called lastPosition that is initialized to the length of the array - 1. 
We iterate through the elements in reverse order. Each time we hit an element that can reach farther than last 
position, we update last position to equal that index. This way, for each element, we do at 
most a single comparison. This lets us get it down to N time. 

The intuition is that we know that lastPosition will get us to the end. At every element, this is the earliest element
we've seen so far. We want to know if we can get to the end starting as early as this. 

"""