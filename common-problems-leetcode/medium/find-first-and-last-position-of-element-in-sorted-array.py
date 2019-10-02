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

# 92ms. 99th percentile.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [ self.farthestLeft(nums, target), self.farthestRight(nums, target) ]
    
    
    def farthestLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            
            middle = left + (right - left)//2
            
            if nums[middle] == target and (middle == 0 or nums[middle - 1] != target):
                return middle
            
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return -1

                
    def farthestRight(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            
            middle = left + (right - left)//2
            
            if nums[middle] == target and (middle == len(nums) - 1 or nums[middle + 1] != target):
                return middle
            
            if nums[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1
        
        return -1

"""
Notes:
Two modified binary searches. Stopping condition also depends on the adjacent elements. Note 
the first elifs in each catch the case of finding target, but not the most extreme instance of it. 
"""