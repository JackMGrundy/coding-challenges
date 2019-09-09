"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
# 136ms. 60 percentile.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sumClosestToTarget = nums[0] + nums[1] + nums[2]
        for first in range(len(nums)):
            second, third = first + 1, len(nums)-1
            while second < third:
                curSum = nums[first] + nums[second] + nums[third]
                
                if curSum == target:
                    return target
                
                if abs(target - curSum) < abs(target - sumClosestToTarget):
                    sumClosestToTarget = curSum
                
                if curSum > target:
                    third -= 1 
                else:
                    second += 1
        
        return sumClosestToTarget