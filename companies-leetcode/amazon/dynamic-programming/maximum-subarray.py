"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
# First attempt: 87th percentile in speed. 
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Intuition: when you consider the next element, you could either add it to the best
        #solution you've come up with so far. Or you could start anew with that element.
        #In order to include the best array seen so far, you have to include everyhing between
        #it's endpoint and the current element. If you hit a point where the next element
        #is greater than all that junk, forget trying to connect to it, because its not worth it. 
        maxSum = nums[0]
        temp = nums[0]
        for i in range(1, len(nums)):
            temp = max(nums[i], temp + nums[i])
            maxSum = max(maxSum, temp)
        return(maxSum)


# Python 3. 72ms. 92nd percentile. 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = temp = nums[0]
        for num in nums[1:]:
            temp = max(num, num+temp)
            res = max(res, temp)
        return res