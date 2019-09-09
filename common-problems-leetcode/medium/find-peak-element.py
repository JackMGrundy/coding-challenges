"""
"""
# 52ms. 84th percentile
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        nums = [-float("inf")] + nums + [-float("inf")]
        return self.binarySearch(nums, 0, len(nums)-1) - 1
    
    def binarySearch(self, nums, l, r):
        while l <= r:
            m = l + (r-l)//2
            
            if nums[m-1] <= nums[m] >= nums[m+1]:
                return m
            elif nums[m-1] > nums[m]:
                r = m - 1
            else:
                l = m + 1
        return 0


"""
Notes:
Simple intuition. What goes up must peak. Binary search in the direction of increase.
Note the question doesn't state this, but it's ok for a value to be equal to one neighbor and greater than another. 
The [-float("inf")]'s make the edge cases easier to deal with.
"""