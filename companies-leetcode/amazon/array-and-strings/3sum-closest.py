"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
# 1st attempt: 87th percentile. 108ms.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[-1]
        smallestDistance = abs(closestSum - target)
        
        for first in range(len(nums)-2):
            if first > 0 and nums[first]==nums[first-1]:
                continue
            second, third = first+1, len(nums)-1
            while second < third:
                summed = nums[first] + nums[second] + nums[third]
                if summed == target:
                    return target
                distanceFromTarget = summed - target
                if abs(distanceFromTarget) < smallestDistance:
                    closestSum = summed
                    smallestDistance = abs(closestSum - target)
                
                if distanceFromTarget < 0:
                    second += 1
                    while second < third and nums[second]==nums[second-1]:
                        second += 1
                elif distanceFromTarget > 0:
                    third -= 1
                    while second < third and nums[third]==nums[third+1]:
                        third -= 1
                
        return closestSum