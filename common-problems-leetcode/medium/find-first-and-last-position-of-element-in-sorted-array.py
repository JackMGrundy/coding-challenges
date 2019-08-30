"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

# 96ms. 93th percentile.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        first = self.findLeftMost(l, r, nums, target)
        last  = self.findRightMost(l, r, nums, target)
        return [first, last]
    

    def findLeftMost(self, l, r, nums, target):
        while l <= r:
            m = (l+r)//2
            
            if (nums[m] == target) and (m == 0 or nums[m-1] != target):
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1

    def findRightMost(self, l, r, nums, target):
        while l <= r:
            m = (l+r)//2
            
            if (nums[m] == target) and (m == len(nums)-1 or nums[m+1] != target):
                return m
            elif nums[m] <= target:
                l = m+1
            else:
                r = m-1
        return -1

"""
Notes:
Two modified binary searches. Stopping condition also depends on the adjacent elements. Note 
the first elifs in each catch the case of finding target, but not the most extreme instance of it. 
"""