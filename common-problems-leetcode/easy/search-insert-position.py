"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

# 52ms. 97 percentile. 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums)-1, target)
    
    def binarySearch(self, nums, l, r, target):
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            
            if nums[m] < target:
                l = m+1
            else:
                r = m-1
        
        return l